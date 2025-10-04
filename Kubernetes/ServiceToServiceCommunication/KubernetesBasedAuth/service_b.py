"""
Service B - Data Service with Kubernetes Service Account Authentication

This service:
1. Provides protected data endpoints
2. Validates Kubernetes service account tokens
3. Only allows access from authorized service accounts
4. Returns protected data for valid requests
"""

from flask import Flask, request, jsonify
import jwt
import os
import json
import logging
from functools import wraps

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Kubernetes service account token paths
SERVICE_ACCOUNT_TOKEN_PATH = "/var/run/secrets/kubernetes.io/serviceaccount/token"
SERVICE_ACCOUNT_CA_PATH = "/var/run/secrets/kubernetes.io/serviceaccount/ca.crt"
SERVICE_ACCOUNT_NAMESPACE_PATH = "/var/run/secrets/kubernetes.io/serviceaccount/namespace"

# Authorized service accounts (in production, this could be managed via RBAC)
AUTHORIZED_SERVICE_ACCOUNTS = [
    "system:serviceaccount:default:service-a-sa",
    "system:serviceaccount:default:service-b-sa",
    # Add more authorized service accounts as needed
]

def get_namespace():
    """Read the current namespace from the mounted volume"""
    try:
        if os.path.exists(SERVICE_ACCOUNT_NAMESPACE_PATH):
            with open(SERVICE_ACCOUNT_NAMESPACE_PATH, 'r') as f:
                return f.read().strip()
        else:
            return "default"
    except Exception as e:
        logger.error(f"Error reading namespace: {e}")
        return "default"

def validate_kubernetes_token(token):
    """
    Validate Kubernetes service account token
    In a real implementation, this would validate against the Kubernetes API server
    """
    try:
        if not token:
            return False, "No token provided", None
        
        # For development/demo purposes, we'll do basic JWT parsing
        # In production, you should validate against Kubernetes API server
        if token == "mock-development-token":
            return True, "Mock token validation successful", {
                "sub": "system:serviceaccount:default:service-a-sa",
                "iss": "kubernetes/serviceaccount"
            }
        
        # Decode JWT without verification for demo (DO NOT do this in production)
        # In production, use the CA certificate to verify the token
        try:
            decoded = jwt.decode(token, options={"verify_signature": False})
            logger.info(f"Token payload: {decoded}")
            
            # Check if it's a service account token - updated for real K8s tokens
            issuer = decoded.get("iss", "")
            subject = decoded.get("sub", "")
            
            # Real Kubernetes tokens have different issuers
            valid_issuers = [
                "kubernetes/serviceaccount",
                "https://kubernetes.default.svc.cluster.local",
                "https://kubernetes.default.svc"
            ]
            
            if any(issuer.startswith(vi) for vi in valid_issuers) or subject.startswith("system:serviceaccount:"):
                service_account = decoded.get("sub")
                if service_account in AUTHORIZED_SERVICE_ACCOUNTS:
                    return True, "Token validation successful", decoded
                else:
                    return False, f"Service account not authorized: {service_account}", decoded
            else:
                return False, f"Not a service account token. Issuer: {issuer}, Subject: {subject}", decoded
                
        except jwt.InvalidTokenError as e:
            logger.error(f"Invalid JWT token: {e}")
            return False, f"Invalid token: {e}", None
            
    except Exception as e:
        logger.error(f"Token validation error: {e}")
        return False, f"Validation error: {e}", None

def require_kubernetes_auth(f):
    """Decorator to require Kubernetes service account authentication"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Get token from Authorization header
        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith('Bearer '):
            return jsonify({
                "error": "Unauthorized", 
                "message": "Bearer token required",
                "required_format": "Authorization: Bearer <service-account-token>"
            }), 401
        
        token = auth_header.split(' ')[1]
        is_valid, message, payload = validate_kubernetes_token(token)
        
        if not is_valid:
            return jsonify({
                "error": "Unauthorized", 
                "message": message,
                "authorized_service_accounts": AUTHORIZED_SERVICE_ACCOUNTS
            }), 401
        
        # Add token info to request context
        request.token_payload = payload
        request.validation_message = message
        return f(*args, **kwargs)
    
    return decorated_function

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint - no authentication required"""
    return jsonify({
        "status": "healthy",
        "service": "service-b",
        "namespace": get_namespace(),
        "authorized_service_accounts": AUTHORIZED_SERVICE_ACCOUNTS
    })

@app.route('/data', methods=['GET'])
@require_kubernetes_auth
def get_protected_data():
    """
    Return protected data - requires valid service account token
    """
    try:
        # Get caller information
        caller = request.token_payload.get("sub", "unknown")
        namespace = request.token_payload.get("kubernetes.io/serviceaccount/namespace", get_namespace())
        
        logger.info(f"Serving protected data to: {caller}")
        
        # Return protected data with metadata
        return jsonify({
            "data": {
                "message": "This is protected data from Service B",
                "timestamp": "2024-10-04T12:00:00Z",
                "sensitive_info": {
                    "database_connection": "postgresql://db:5432/app",
                    "api_keys": ["key1", "key2", "key3"],
                    "internal_endpoints": [
                        "http://internal-api:8080",
                        "http://metrics:9090"
                    ]
                }
            },
            "metadata": {
                "served_to": caller,
                "namespace": namespace,
                "service": "service-b",
                "validation_message": request.validation_message,
                "access_granted_at": "2024-10-04T12:00:00Z"
            }
        })
        
    except Exception as e:
        logger.error(f"Error serving protected data: {e}")
        return jsonify({
            "error": "Internal Server Error",
            "message": str(e)
        }), 500

@app.route('/admin/users', methods=['GET'])
@require_kubernetes_auth
def get_users():
    """
    Return user data - requires admin service account token
    This demonstrates role-based access within service accounts
    """
    try:
        caller = request.token_payload.get("sub", "unknown")
        
        # Check if caller has admin privileges (simplified check)
        # In production, this would be handled by Kubernetes RBAC
        if "admin" in caller or "service-a-sa" in caller:
            logger.info(f"Serving admin data to: {caller}")
            
            return jsonify({
                "users": [
                    {"id": 1, "name": "Alice", "role": "developer"},
                    {"id": 2, "name": "Bob", "role": "admin"},
                    {"id": 3, "name": "Charlie", "role": "viewer"}
                ],
                "metadata": {
                    "served_to": caller,
                    "endpoint": "/admin/users",
                    "access_level": "admin"
                }
            })
        else:
            return jsonify({
                "error": "Forbidden",
                "message": f"Service account {caller} does not have admin privileges"
            }), 403
            
    except Exception as e:
        logger.error(f"Error serving admin data: {e}")
        return jsonify({
            "error": "Internal Server Error",
            "message": str(e)
        }), 500

@app.route('/token-info', methods=['GET'])
@require_kubernetes_auth
def token_info():
    """Get detailed information about the authenticated token"""
    return jsonify({
        "token_payload": request.token_payload,
        "service": "service-b",
        "namespace": get_namespace(),
        "validation_message": request.validation_message,
        "authorized": True
    })

@app.route('/public', methods=['GET'])
def public_endpoint():
    """Public endpoint that doesn't require authentication"""
    return jsonify({
        "message": "This is a public endpoint",
        "service": "service-b",
        "namespace": get_namespace(),
        "note": "No authentication required for this endpoint"
    })

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "error": "Not Found", 
        "message": "Endpoint not found",
        "available_endpoints": [
            "/health",
            "/data",
            "/admin/users", 
            "/token-info",
            "/public"
        ]
    }), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({
        "error": "Internal Server Error", 
        "message": "Something went wrong"
    }), 500

if __name__ == '__main__':
    logger.info("Starting Service B...")
    logger.info(f"Namespace: {get_namespace()}")
    logger.info(f"Authorized service accounts: {AUTHORIZED_SERVICE_ACCOUNTS}")
    
    # Check if running in Kubernetes
    if os.path.exists(SERVICE_ACCOUNT_TOKEN_PATH):
        logger.info("Running in Kubernetes environment")
    else:
        logger.info("Running in development environment")
    
    app.run(host='0.0.0.0', port=5001, debug=True)
