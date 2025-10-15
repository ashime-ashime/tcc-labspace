#!/usr/bin/env python3
"""
Mock TCC API Server for Lab Testing
Simulates Testcontainers Cloud API responses for TSE investigation
"""

import json
import http.server
import socketserver
import urllib.parse
from datetime import datetime

# Mock customer data (based on the customer report)
CUSTOMER_DATA = {
    "account": {
        "org_id": "3294",
        "plan_type": "trial_legacy",
        "status": "active",
        "billing_model": "separate_tcc_billing",
        "docker_pro_plan": "legacy_subscription",
        "tcc_included": False
    },
    "usage": {
        "free_tier_minutes": 50,
        "current_month_usage": 52,
        "quota_exceeded": True,
        "quota_reset": "never",
        "last_successful_ci": "2025-01-08T14:22:00Z",
        "quota_exhausted_date": "2025-01-09T00:00:00Z"
    },
    "health": {
        "status": "operational",
        "timestamp": datetime.now().isoformat(),
        "version": "1.0.0"
    }
}

# Valid tokens for testing
VALID_TOKENS = {
    "tcc-lab-token-12345": "customer_token",
    "tcc-lab-org-12345": "org_token"
}

class MockTCCHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        """Handle GET requests to mock TCC API"""
        parsed_path = urllib.parse.urlparse(self.path)
        path = parsed_path.path
        
        # Extract token from Authorization header
        auth_header = self.headers.get('Authorization', '')
        token = None
        if auth_header.startswith('Bearer '):
            token = auth_header[7:]  # Remove 'Bearer ' prefix
        
        # Route requests
        if path == '/v1/health':
            self.handle_health()
        elif path == '/v1/account':
            self.handle_account(token)
        elif path == '/v1/usage':
            self.handle_usage(token)
        else:
            self.send_error(404, "Endpoint not found")
    
    def handle_health(self):
        """Handle health check endpoint"""
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        response = {
            "status": "operational",
            "timestamp": datetime.now().isoformat(),
            "version": "1.0.0"
        }
        self.wfile.write(json.dumps(response, indent=2).encode())
    
    def handle_account(self, token):
        """Handle account endpoint"""
        if not token or token not in VALID_TOKENS:
            self.send_error(401, "Unauthorized - Invalid or missing token")
            return
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        response = CUSTOMER_DATA["account"]
        self.wfile.write(json.dumps(response, indent=2).encode())
    
    def handle_usage(self, token):
        """Handle usage endpoint"""
        if not token or token not in VALID_TOKENS:
            self.send_error(401, "Unauthorized - Invalid or missing token")
            return
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        response = CUSTOMER_DATA["usage"]
        self.wfile.write(json.dumps(response, indent=2).encode())
    
    def log_message(self, format, *args):
        """Suppress default logging"""
        pass

def main():
    """Start the mock TCC API server"""
    PORT = 8080
    
    print("🚀 Starting Mock TCC API Server...")
    print(f"📍 Server running on http://localhost:{PORT}")
    print("🔑 Valid tokens:")
    for token in VALID_TOKENS:
        print(f"   - {token}")
    print("\n🧪 Test commands:")
    print("   curl http://localhost:8080/v1/health")
    print('   curl -H "Authorization: Bearer tcc-lab-token-12345" http://localhost:8080/v1/account')
    print('   curl -H "Authorization: Bearer tcc-lab-token-12345" http://localhost:8080/v1/usage')
    print("\n⏹️  Press Ctrl+C to stop")
    
    with socketserver.TCPServer(("", PORT), MockTCCHandler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n🛑 Server stopped")

if __name__ == "__main__":
    main()
