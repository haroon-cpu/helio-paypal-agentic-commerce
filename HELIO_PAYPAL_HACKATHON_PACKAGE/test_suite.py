"""
Automated Test Suite for HELIO Agentic Commerce Engine
PayPal AI Hackathon 2026 Verification Harness
Author: Mohammed Haroon J, HEONIX AI
"""

import sys
import unittest
from paypal_agentic_booking_engine import MockPayPalClient, HelioClinicalAgent

class TestHelioPayPalAgenticCommerce(unittest.TestCase):
    
    def setUp(self):
        self.paypal = MockPayPalClient()
        self.agent = HelioClinicalAgent(self.paypal)

    def test_01_emergency_triage_bypass(self):
        """Verify that emergency symptoms bypass booking and trigger immediate 108 alert"""
        emergency_cases = [
            "Doctor, I have severe chest pain and dizziness",
            "Emergency, my father has heavy bleeding",
            "Unconscious patient needs urgent help",
            "Patient is having severe breathing trouble"
        ]
        for msg in emergency_cases:
            res = self.agent.process_patient_message("+919988776655", msg)
            self.assertEqual(res["action"], "EMERGENCY_ESCALATION")
            self.assertFalse(res["booking_created"])
            self.assertIn("108", res["response"])

    def test_02_routine_booking_deposit_generation(self):
        """Verify that routine appointment booking generates a dynamic PayPal sandbox order"""
        msg = "Hi, I need an appointment with a dental doctor tomorrow"
        res = self.agent.process_patient_message("+919876543210", msg)
        
        self.assertEqual(res["action"], "PAYMENT_REQUESTED")
        self.assertTrue(res["booking_created"])
        self.assertIn("PAYID-", res["order_id"])
        self.assertTrue(res["payment_url"].startswith("https://www.sandbox.paypal.com/"))
        self.assertEqual(res["deposit_amount"], "$15.0 USD")
        
        # Verify slot is locked
        slot = res["slot_time"]
        self.assertEqual(self.agent.clinic_slots[slot]["status"], "LOCKED_PENDING_PAYMENT")

    def test_03_webhook_payment_confirmation(self):
        """Verify that payment webhook capture permanently confirms the reservation"""
        # Step 1: Request booking
        res = self.agent.process_patient_message("+919123456780", "Book dentist appointment")
        order_id = res["order_id"]
        slot = res["slot_time"]
        
        # Step 2: Handle PayPal capture webhook
        webhook_result = self.agent.handle_payment_webhook(order_id)
        self.assertEqual(webhook_result["status"], "SUCCESS")
        self.assertEqual(webhook_result["slot_time"], slot)
        
        # Verify slot is permanently confirmed
        self.assertEqual(self.agent.clinic_slots[slot]["status"], "CONFIRMED")

    def test_04_capacity_exhaustion_waitlist(self):
        """Verify that when all clinic slots are booked, agent routes to waitlist"""
        # Fill all available slots
        self.agent.process_patient_message("+919000000001", "Book appointment")
        self.agent.process_patient_message("+919000000002", "Book appointment")
        
        # Third request should trigger waitlist
        res = self.agent.process_patient_message("+919000000003", "Book appointment")
        self.assertEqual(res["action"], "WAITLIST")
        self.assertFalse(res["booking_created"])

    def test_05_general_inquiry_handling(self):
        """Verify non-booking general messages receive friendly guidance"""
        res = self.agent.process_patient_message("+919000000004", "What are your clinic timings?")
        self.assertEqual(res["action"], "GENERAL_INQUIRY")
        self.assertFalse(res["booking_created"])

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestHelioPayPalAgenticCommerce)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    if not result.wasSuccessful():
        sys.exit(1)
