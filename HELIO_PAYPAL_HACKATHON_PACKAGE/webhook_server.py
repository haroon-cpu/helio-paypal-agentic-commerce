"""
HELIO Agentic Commerce HTTP Webhook Server
Lightweight REST endpoint handler for live WhatsApp and PayPal Sandbox callbacks
Author: Mohammed Haroon J, HEONIX AI
"""

import json
from http.server import HTTPServer, BaseHTTPRequestHandler
from paypal_agentic_booking_engine import MockPayPalClient, HelioClinicalAgent

# Initialize singleton engine
paypal_client = MockPayPalClient()
clinical_agent = HelioClinicalAgent(paypal_client)

class HelioWebhookHandler(BaseHTTPRequestHandler):
    
    def _set_headers(self, status_code=200):
        self.send_response(status_code)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()

    def do_GET(self):
        """Health check endpoint"""
        if self.path == "/health":
            self._set_headers(200)
            response = {
                "service": "HELIO Agentic Commerce Gateway",
                "status": "HEALTHY",
                "provider": "PayPal Sandbox Orders v2",
                "security_mode": "Clinical Triage Guard Active"
            }
            self.wfile.write(json.dumps(response).encode('utf-8'))
        else:
            self._set_headers(404)
            self.wfile.write(json.dumps({"error": "Endpoint not found"}).encode('utf-8'))

    def do_POST(self):
        """Processes incoming patient messages and PayPal payment webhooks"""
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)
        
        try:
            payload = json.loads(post_data.decode('utf-8'))
        except Exception:
            self._set_headers(400)
            self.wfile.write(json.dumps({"error": "Invalid JSON"}).encode('utf-8'))
            return

        # 1. Incoming Patient WhatsApp Message Route
        if self.path == "/webhook/patient-message":
            phone = payload.get("phone", "+919876543210")
            message = payload.get("message", "")
            result = clinical_agent.process_patient_message(phone, message)
            self._set_headers(200)
            self.wfile.write(json.dumps(result).encode('utf-8'))

        # 2. Incoming PayPal Payment Capture Webhook Route
        elif self.path == "/webhook/paypal-callback":
            order_id = payload.get("order_id", "")
            result = clinical_agent.handle_payment_webhook(order_id)
            self._set_headers(200)
            self.wfile.write(json.dumps(result).encode('utf-8'))

        else:
            self._set_headers(404)
            self.wfile.write(json.dumps({"error": "Unknown webhook route"}).encode('utf-8'))

def run_server(port=8080):
    server_address = ('', port)
    httpd = HTTPServer(server_address, HelioWebhookHandler)
    print(f"HELIO Agentic Commerce Webhook Server listening on port {port}...")
    return httpd

if __name__ == "__main__":
    # Test server initialization
    run_server(8080)
