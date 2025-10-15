#!/bin/bash

# Auto-start Mock TCC API Server (Silent)
# This script starts the mock API server in the background
# so TSEs can run curl commands directly during investigation

# Start the mock API server in the background silently
cd /workspace/labspace-exercises/quota-mystery/customer-report
python3 mock-tcc-api.py > /tmp/mock-api.log 2>&1 &

# Give it a moment to start
sleep 2

# Silently verify it's running (no output)
curl -s http://localhost:8080/v1/health > /dev/null 2>&1
