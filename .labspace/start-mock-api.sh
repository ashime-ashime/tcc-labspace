#!/bin/bash

# Auto-start Mock TCC API Server
# This script starts the mock API server in the background
# so TSEs can run curl commands directly during investigation

echo "🚀 Starting Mock TCC API Server (Background)"
echo "============================================="

# Start the mock API server in the background
cd /workspace/labspace-exercises/quota-mystery/customer-report
python3 mock-tcc-api.py > /tmp/mock-api.log 2>&1 &

# Give it a moment to start
sleep 2

# Check if it's running
if curl -s http://localhost:8080/v1/health > /dev/null; then
    echo "✅ Mock TCC API Server is running on http://localhost:8080"
    echo ""
    echo "🧪 Ready for diagnostic commands:"
    echo "   curl http://localhost:8080/v1/health"
    echo '   curl -H "Authorization: Bearer tcc-lab-token-12345" http://localhost:8080/v1/account'
    echo '   curl -H "Authorization: Bearer tcc-lab-token-12345" http://localhost:8080/v1/usage'
    echo ""
    echo "🔑 Valid tokens: tcc-lab-token-12345, tcc-lab-org-12345"
    echo "📊 Expected: quota exceeded (52/50 minutes)"
else
    echo "❌ Failed to start mock API server"
    echo "📋 Check logs: cat /tmp/mock-api.log"
fi

echo ""
echo "💡 The mock API is now running in the background."
echo "   You can run curl commands directly during your investigation!"
echo ""
