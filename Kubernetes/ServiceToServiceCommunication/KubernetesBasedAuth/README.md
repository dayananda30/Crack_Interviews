# 🔐 Kubernetes Service Account Based Authentication

[![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)](https://kubernetes.io)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://docker.com)

## 📖 Overview

This project demonstrates **Kubernetes Service Account-based authentication** for secure service-to-service (S2S) communication in a microservices architecture. It showcases how services can authenticate each other using Kubernetes-native service account tokens while leveraging RBAC for authorization.

## 🏗️ Architecture

```mermaid
graph TB
    subgraph "Kubernetes Cluster"
        subgraph "Namespace: s2s-auth-demo"
            SA1[Service Account A]
            SA2[Service Account B]
            
            subgraph "Service A Pod"
                A[Service A :5000]
                AT[SA Token A]
            end
            
            subgraph "Service B Pod"  
                B[Service B :5001]
                BT[SA Token B]
            end
            
            RBAC[RBAC Rules]
            API[Kubernetes API Server]
        end
        
        Client[External Client] 
    end
    
    Client -->|Bearer Token| A
    A -->|Validate Token| API
    API -->|Token Valid| A
    A -->|Bearer SA Token A| B
    B -->|Validate Token| API
    API -->|Token Valid| B
    B -->|Protected Data| A
    A -->|Response| Client
    
    SA1 -.->|Mounted| AT
    SA2 -.->|Mounted| BT
    RBAC -.->|Governs| SA1
    RBAC -.->|Governs| SA2
```

## 🔑 Authentication Flow

1. **Client Request**: Client sends request to Service A with a bearer token
2. **Token Validation**: Service A validates the client token (service account token)
3. **Authorization Check**: Kubernetes RBAC determines if the service account has required permissions
4. **Service-to-Service Call**: Service A calls Service B using its own service account token
5. **Token Verification**: Service B validates Service A's token with Kubernetes API server
6. **Data Access**: Upon successful validation, Service B returns protected data
7. **Response**: Service A forwards the response back to the client

## 🚀 Quick Start

### Prerequisites
- Kubernetes cluster (Docker Desktop, minikube, kind, or cloud provider)
- Docker installed and kubectl configured

### ⚡ One-Command Setup
```bash
./deploy.sh  # Builds, deploys, and sets up everything
./test.sh    # Runs comprehensive tests
./cleanup.sh # Cleans up when done
```

### 🛠️ Step-by-Step Setup

```bash
# 1. Build Docker images
./build.sh

# 2. Deploy to Kubernetes
kubectl apply -f k8s-manifests.yaml

# 3. Wait for pods to be ready
kubectl wait --for=condition=ready pod -l app=service-a -n s2s-auth-demo --timeout=180s
kubectl wait --for=condition=ready pod -l app=service-b -n s2s-auth-demo --timeout=180s

# 4. Test the deployment
./test.sh
```

## 🧪 Testing the Authentication

### 🔓 Get Service Account Token

First, you need to get a service account token to test with:

```bash
# Get Service A token
SA_TOKEN=$(kubectl create token service-a-sa -n s2s-auth-demo)
echo "Service A Token: $SA_TOKEN"

# Or create a long-lived token (not recommended for production)
kubectl apply -f - <<EOF
apiVersion: v1
kind: Secret
metadata:
  name: service-a-token
  namespace: s2s-auth-demo
  annotations:
    kubernetes.io/service-account.name: service-a-sa
type: kubernetes.io/service-account-token
EOF

# Get the token
SA_TOKEN=$(kubectl get secret service-a-token -n s2s-auth-demo -o jsonpath='{.data.token}' | base64 -d)
```

### ✅ Test Successful Authentication

```bash
# Port forward to access Service A
kubectl port-forward svc/service-a 8080:5000 -n s2s-auth-demo &

# Test the service-to-service call
curl -H "Authorization: Bearer $SA_TOKEN" \
     -H "Content-Type: application/json" \
     http://localhost:8080/call-service-b
```

**Expected Response:**
```json
{
  "service_a_info": {
    "authenticated_client": "system:serviceaccount:s2s-auth-demo:service-a-sa",
    "namespace": "s2s-auth-demo"
  },
  "service_b_response": {
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
      "served_to": "system:serviceaccount:s2s-auth-demo:service-a-sa",
      "namespace": "s2s-auth-demo",
      "service": "service-b"
    }
  },
  "status_code": 200
}
```

### ❌ Test Failed Authentication

```bash
# Test with invalid token
curl -H "Authorization: Bearer invalid-token" \
     -H "Content-Type: application/json" \
     http://localhost:8080/call-service-b
```

**Expected Response:**
```json
{
  "error": "Unauthorized",
  "message": "Invalid token: Invalid token: ..."
}
```

### 🏥 Health Check Endpoints

```bash
# Service A health check
curl http://localhost:8080/health

# Service B health check (via port forward)
kubectl port-forward svc/service-b 8081:5001 -n s2s-auth-demo &
curl http://localhost:8081/health
```

## 📂 File Structure

```
KubernetesBasedAuth/
├── README.md                    # This documentation
├── service_a.py                 # Gateway service with K8s auth
├── service_b.py                 # Data service with token validation
├── k8s-manifests.yaml          # Complete Kubernetes deployment
├── requirements.txt             # Python dependencies
├── Dockerfile.service-a         # Service A container
├── Dockerfile.service-b         # Service B container
├── build.sh                    # Build Docker images
├── deploy.sh                   # Complete deployment script
├── test.sh                     # Comprehensive test script
└── cleanup.sh                  # Cleanup deployed resources
```

## 🔧 Configuration Details

### Service Accounts

| Service Account | Namespace | Purpose | RBAC Permissions |
|----------------|-----------|---------|------------------|
| `service-a-sa` | `s2s-auth-demo` | Service A authentication | Token review, Service access |
| `service-b-sa` | `s2s-auth-demo` | Service B authentication | Token review |

### Environment Variables

| Variable | Service | Description | Default |
|----------|---------|-------------|---------|
| `SERVICE_B_URL` | Service A | URL for Service B | `http://service-b:5001` |
| `LOG_LEVEL` | Both | Logging level | `INFO` |
| `AUTHORIZED_SERVICE_ACCOUNTS` | Service B | Comma-separated list of authorized SAs | See ConfigMap |

### Endpoints

#### Service A Endpoints

| Endpoint | Method | Auth Required | Description |
|----------|--------|---------------|-------------|
| `/health` | GET | No | Health check |
| `/call-service-b` | GET | Yes | Calls Service B with authentication |
| `/token-info` | GET | Yes | Returns token information |

#### Service B Endpoints

| Endpoint | Method | Auth Required | Description |
|----------|--------|---------------|-------------|
| `/health` | GET | No | Health check |
| `/data` | GET | Yes | Returns protected data |
| `/admin/users` | GET | Yes | Returns admin data (role-based) |
| `/token-info` | GET | Yes | Returns token information |
| `/public` | GET | No | Public endpoint |

## 🔒 Security Features

### ✅ Implemented Security Measures

- **Service Account Tokens**: Native Kubernetes authentication
- **RBAC Authorization**: Fine-grained permission control
- **Token Validation**: Proper JWT token verification
- **Network Policies**: Controlled network access
- **Non-root Containers**: Security-hardened container execution
- **Resource Limits**: Prevent resource exhaustion
- **Health Checks**: Proper liveness and readiness probes

### 🛡️ Production Security Recommendations

1. **Token Validation**: 
   ```python
   # Use proper token validation against K8s API server
   from kubernetes import client, config
   
   def validate_token_with_k8s_api(token):
       v1 = client.AuthenticationV1Api()
       body = client.V1TokenReview(
           spec=client.V1TokenReviewSpec(token=token)
       )
       response = v1.create_token_review(body=body)
       return response.status.authenticated
   ```

2. **Certificate Validation**: Use mounted CA certificates
3. **RBAC Policies**: Implement least-privilege access
4. **Network Segmentation**: Use network policies effectively
5. **Audit Logging**: Enable Kubernetes audit logs
6. **Secret Management**: Use external secret management systems

## 🚦 Local Development

### Running Services Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Terminal 1: Start Service B
python service_b.py

# Terminal 2: Start Service A  
export SERVICE_B_URL="http://localhost:5001"
python service_a.py

# Terminal 3: Test locally
curl -H "Authorization: Bearer mock-development-token" \
     http://localhost:5000/call-service-b
```

### Development vs Production Differences

| Aspect | Development | Production |
|--------|-------------|------------|
| Token Validation | Mock tokens accepted | Full K8s API validation |
| TLS | HTTP allowed | HTTPS required |
| Certificates | Self-signed OK | Valid CA certificates |
| Logging | Debug level | Info/Warn levels |
| Resource Limits | Relaxed | Strict limits enforced |

## 🔍 Troubleshooting

### Common Issues

#### 1. Pod Startup Issues
```bash
# Check pod logs
kubectl logs -f deployment/service-a -n s2s-auth-demo
kubectl logs -f deployment/service-b -n s2s-auth-demo

# Check events
kubectl get events -n s2s-auth-demo --sort-by='.lastTimestamp'
```

#### 2. Authentication Failures
```bash
# Verify service account exists
kubectl get serviceaccount -n s2s-auth-demo

# Check RBAC permissions
kubectl auth can-i create tokenreviews --as=system:serviceaccount:s2s-auth-demo:service-a-sa

# Test token creation
kubectl create token service-a-sa -n s2s-auth-demo
```

#### 3. Network Connectivity Issues
```bash
# Test service connectivity
kubectl exec -it deployment/service-a -n s2s-auth-demo -- curl http://service-b:5001/health

# Check network policies
kubectl get networkpolicy -n s2s-auth-demo
```

### Debug Commands

```bash
# Get detailed pod information
kubectl describe pod <pod-name> -n s2s-auth-demo

# Check service endpoints
kubectl get endpoints -n s2s-auth-demo

# View service account details
kubectl describe serviceaccount service-a-sa -n s2s-auth-demo

# Check RBAC bindings
kubectl describe clusterrolebinding service-a-rolebinding
```

## 🌟 Advanced Use Cases

### 1. Multi-Namespace Communication

```yaml
# Cross-namespace service account access
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: cross-namespace-access
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: service-communication-role
subjects:
- kind: ServiceAccount
  name: service-a-sa
  namespace: namespace-a
- kind: ServiceAccount
  name: service-b-sa
  namespace: namespace-b
```

### 2. Service Mesh Integration

This example can be extended with service mesh solutions like Istio:

```yaml
# Istio AuthorizationPolicy
apiVersion: security.istio.io/v1beta1
kind: AuthorizationPolicy
metadata:
  name: service-b-policy
  namespace: s2s-auth-demo
spec:
  selector:
    matchLabels:
      app: service-b
  rules:
  - from:
    - source:
        principals: ["cluster.local/ns/s2s-auth-demo/sa/service-a-sa"]
```

### 3. External Service Integration

```python
# Integration with external OAuth/OIDC providers
def validate_external_token(token):
    # Validate against external identity provider
    response = requests.post(
        "https://oauth-provider.com/tokeninfo",
        headers={"Authorization": f"Bearer {token}"}
    )
    return response.status_code == 200
```

## 📊 Monitoring and Observability

### Metrics to Monitor

- Token validation success/failure rates
- Service-to-service call latency
- Authentication error patterns
- RBAC permission denials

### Prometheus Metrics Example

```python
from prometheus_client import Counter, Histogram, generate_latest

auth_attempts = Counter('auth_attempts_total', 'Total authentication attempts', ['service', 'status'])
request_duration = Histogram('request_duration_seconds', 'Request duration')

@app.route('/metrics')
def metrics():
    return generate_latest()
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Test your changes with a local Kubernetes cluster
4. Commit your changes (`git commit -m 'Add amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

## 📚 Additional Resources

### Kubernetes Documentation
- [Service Accounts](https://kubernetes.io/docs/concepts/security/service-accounts/)
- [RBAC Authorization](https://kubernetes.io/docs/reference/access-authn-authz/rbac/)
- [Network Policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/)

### Security Best Practices  
- [Kubernetes Security Best Practices](https://kubernetes.io/docs/concepts/security/)
- [OWASP Kubernetes Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Kubernetes_Security_Cheat_Sheet.html)

### Related Patterns
- [Service Mesh Authentication](https://istio.io/latest/docs/concepts/security/)
- [Zero Trust Architecture](https://www.nist.gov/publications/zero-trust-architecture)

---

<div align="center">

**🚢 Ready to sail the Kubernetes seas with secure service communication! 🚢**

<sub>Made with ❤️ for secure microservices | Follow cloud-native security best practices!</sub>

</div>