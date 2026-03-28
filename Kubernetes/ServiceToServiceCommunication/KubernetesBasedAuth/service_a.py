"""
Service A - Gateway Service with Kubernetes Service Account Authentication

This service:
1. Receives requests from clients
2. Validates the Kubernetes service account token from the request
3. Forwards authenticated requests to Service B using its own service account token
4. Returns the response from Service B
"""

from flask import Flask, request, jsonify
import requests
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

# Service B configuration
SERVICE_B_URL = os.getenv("SERVICE_B_URL", "http://service-b:5001")

def get_service_account_token():
    """Read the service account token from the mounted volume"""
    try:
        if os.path.exists(SERVICE_ACCOUNT_TOKEN_PATH):
            with open(SERVICE_ACCOUNT_TOKEN_PATH, 'r') as f:
                return f.read().strip()
        else:
            # For local development, use a mock token
            logger.warning("Service account token not found, using mock token for development")
            return "mock-development-token"
    except Exception as e:
        logger.error(f"Error reading service account token: {e}")
        return None

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
            return False, "No token provided"
        
        # For development/demo purposes, we'll do basic JWT parsing
        # In production, you should validate against Kubernetes API server
        if token == "mock-development-token":
            return True, {"sub": "system:serviceaccount:default:service-a-sa"}
        
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
                return True, decoded
            else:
                return False, f"Not a service account token. Issuer: {issuer}, Subject: {subject}"
                
        except jwt.InvalidTokenError as e:
            logger.error(f"Invalid JWT token: {e}")
            return False, f"Invalid token: {e}"
            
    except Exception as e:
        logger.error(f"Token validation error: {e}")
        return False, f"Validation error: {e}"

def require_kubernetes_auth(f):
    """Decorator to require Kubernetes service account authentication"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Get token from Authorization header
        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith('Bearer '):
            return jsonify({
                "error": "Unauthorized", 
                "message": "Bearer token required"
            }), 401
        
        token = auth_header.split(' ')[1]
        is_valid, payload = validate_kubernetes_token(token)
        
        if not is_valid:
            return jsonify({
                "error": "Unauthorized", 
                "message": f"Invalid token: {payload}"
            }), 401
        
        # Add token info to request context
        request.token_payload = payload
        return f(*args, **kwargs)
    
    return decorated_function

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "service": "service-a",
        "namespace": get_namespace()
    })

@app.route('/call-service-b', methods=['GET'])
@require_kubernetes_auth
def call_service_b():
    """
    Endpoint that calls Service B using service account authentication
    """
    try:
        # Get our own service account token to authenticate with Service B
        our_token = get_service_account_token()
        if not our_token:
            return jsonify({
                "error": "Internal Error",
                "message": "Could not retrieve service account token"
            }), 500
        
        # Prepare headers for Service B call
        headers = {
            "Authorization": f"Bearer {our_token}",
            "Content-Type": "application/json"
        }
        
        # Log the request for debugging
        logger.info(f"Calling Service B at {SERVICE_B_URL}/data")
        logger.info(f"Client token payload: {request.token_payload}")
        
        # Call Service B
        response = requests.get(f"{SERVICE_B_URL}/data", headers=headers, timeout=10)
        
        # Return the response from Service B
        return jsonify({
            "service_a_info": {
                "authenticated_client": request.token_payload.get("sub", "unknown"),
                "namespace": get_namespace()
            },
            "service_b_response": response.json() if response.headers.get('content-type', '').startswith('application/json') else response.text,
            "status_code": response.status_code
        }), response.status_code
        
    except requests.exceptions.RequestException as e:
        logger.error(f"Error calling Service B: {e}")
        return jsonify({
            "error": "Service Unavailable",
            "message": f"Could not reach Service B: {e}"
        }), 503
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return jsonify({
            "error": "Internal Server Error",
            "message": str(e)
        }), 500

@app.route('/token-info', methods=['GET'])
@require_kubernetes_auth
def token_info():
    """Get information about the authenticated token"""
    return jsonify({
        "token_payload": request.token_payload,
        "service": "service-a",
        "namespace": get_namespace()
    })

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not Found", "message": "Endpoint not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal Server Error", "message": "Something went wrong"}), 500

if __name__ == '__main__':
    logger.info("Starting Service A...")
    logger.info(f"Service B URL: {SERVICE_B_URL}")
    logger.info(f"Namespace: {get_namespace()}")
    
    # Check if running in Kubernetes
    if os.path.exists(SERVICE_ACCOUNT_TOKEN_PATH):
        logger.info("Running in Kubernetes environment")
    else:
        logger.info("Running in development environment")
    
    app.run(host='0.0.0.0', port=5000, debug=True)
