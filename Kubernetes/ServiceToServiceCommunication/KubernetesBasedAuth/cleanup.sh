#!/bin/bash

# Cleanup script to remove the deployed resources

echo "🧹 Cleaning up Kubernetes Service-to-Service Authentication Demo"
echo "==============================================================="

# Check what's currently deployed
echo "Current deployments:"
kubectl get all -n s2s-auth-demo 2>/dev/null || echo "No resources found in s2s-auth-demo namespace"
kubectl get all -n default -l app=service-a,app=service-b 2>/dev/null || echo "No labeled resources found in default namespace"

echo ""
read -p "Do you want to delete all demo resources? (y/N): " confirm

if [[ $confirm =~ ^[Yy]$ ]]; then
    echo "🗑️  Deleting resources..."
    
    # Try to delete from s2s-auth-demo namespace first
    kubectl delete -f k8s-manifests.yaml 2>/dev/null || echo "Resources from k8s-manifests.yaml not found"
    
    # Clean up from default namespace if deployed there
    kubectl delete deployment,service,serviceaccount,role,rolebinding,configmap -l app=service-a -n default 2>/dev/null || true
    kubectl delete deployment,service,serviceaccount,role,rolebinding,configmap -l app=service-b -n default 2>/dev/null || true
    
    # Kill any running port-forwards
    pkill -f "kubectl port-forward" 2>/dev/null || true
    
    echo "✅ Cleanup completed!"
else
    echo "❌ Cleanup cancelled"
fi