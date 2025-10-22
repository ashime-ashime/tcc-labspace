#!/bin/bash

# Start the Mock TCC API Server

echo "🔧 Starting TCC Diagnostic API Server..."
echo "==========================================="
echo ""

# Start the mock API server in the background
python3 mock-tcc-api.py > /tmp/mock-api.log 2>&1 &

# Give it a moment to start
sleep 2

# Check if it's running
if curl -s http://localhost:8080/v1/health > /dev/null; then
    echo "✅ TCC Diagnostic API is running on http://localhost:8080"
    echo ""
    echo "📋 Available Endpoints:"
    echo "   GET  /v1/health                    (Health check - no auth)"
    echo "   GET  /v1/account                   (Account details - requires auth)"
    echo "   GET  /v1/usage                     (Usage statistics - requires auth)"
    echo ""
    echo "🔑 Available Tokens:"
    echo "   tcc-lab-token-12345   (Service account token)"
    echo "   tcc-lab-org-12345     (Organization token)"
    echo ""
    echo "📖 Example Usage:"
    echo "   curl http://localhost:8080/v1/health"
    echo "   curl -H \"Authorization: Bearer tcc-lab-token-12345\" http://localhost:8080/v1/account"
    echo "   curl -H \"Authorization: Bearer tcc-lab-token-12345\" http://localhost:8080/v1/usage"
    echo ""
    echo "💡 This API simulates real TCC API responses for investigation."
else
    echo "❌ Failed to start TCC Diagnostic API"
    echo "📋 Check logs: cat /tmp/mock-api.log"
    exit 1
fi

