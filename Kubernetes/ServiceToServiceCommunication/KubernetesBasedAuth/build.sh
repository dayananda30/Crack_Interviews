#!/bin/bash

# Build script for Service A and Service B Docker images

set -e

echo "🚀 Building Docker images for Kubernetes Service-to-Service Authentication Demo"

# Build Service A
echo "📦 Building Service A image..."
docker build -f Dockerfile.service-a -t service-a:latest .

# Build Service B  
echo "📦 Building Service B image..."
docker build -f Dockerfile.service-b -t service-b:latest .

echo "✅ Docker images built successfully!"
echo ""
echo "Images created:"
echo "  - service-a:latest"
echo "  - service-b:latest"
echo ""
echo "🚀 Next steps:"
echo "   1. Deploy: ./deploy.sh"
echo "   2. Test: ./test.sh"