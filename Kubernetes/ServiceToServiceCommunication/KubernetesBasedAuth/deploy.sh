#!/bin/bash

# Simple deployment script for Kubernetes Service-to-Service Authentication Demo

set -e

echo "🚀 Deploying Kubernetes Service-to-Service Authentication Demo"
echo "============================================================="

# Check if kubectl is available
if ! command -v kubectl &> /dev/null; then
    echo "❌ kubectl not found. Please install kubectl first."
    exit 1
fi

# Check if cluster is available
if ! kubectl cluster-info &> /dev/null; then
    echo "❌ No Kubernetes cluster found. Please ensure your cluster is running."
    echo "   Options: Docker Desktop, minikube, kind, or cloud provider"
    exit 1
fi

echo "✅ Kubernetes cluster detected"

# Build images
echo "📦 Building Docker images..."
docker build -f Dockerfile.service-a -t service-a:latest .
docker build -f Dockerfile.service-b -t service-b:latest .

# Load images (for local clusters)
if kubectl config current-context | grep -q "kind\|minikube"; then
    echo "📥 Loading images into local cluster..."
    if command -v kind &> /dev/null && kind get clusters &> /dev/null; then
        kind load docker-image service-a:latest
        kind load docker-image service-b:latest
    elif command -v minikube &> /dev/null; then
        minikube image load service-a:latest
        minikube image load service-b:latest
    fi
fi

# Deploy to Kubernetes
echo "🚀 Deploying to Kubernetes..."
kubectl apply -f k8s-manifests.yaml

# Wait for deployment
echo "⏳ Waiting for pods to be ready..."
kubectl wait --for=condition=ready pod -l app=service-a -n s2s-auth-demo --timeout=180s
kubectl wait --for=condition=ready pod -l app=service-b -n s2s-auth-demo --timeout=180s

echo "✅ Deployment successful!"
echo ""
echo "🧪 To test the deployment, run:"
echo "   ./test.sh"