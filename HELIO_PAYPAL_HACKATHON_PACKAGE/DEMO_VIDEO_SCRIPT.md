# HELIO x PayPal AI Hackathon: 3-Minute Video Demo Script

**Target Video Duration:** 2 minutes 30 seconds to 2 minutes 50 seconds (Under 3 minutes strict limit)
**Platform:** YouTube (Public / Unlisted)

---

## 🎬 Video Storyboard & Script Breakdown

### [00:00 - 00:30] Introduction: The $150B Healthcare No-Show Crisis
- **Screen:** Show title card: "HELIO: Autonomous Clinical Booking & PayPal Agentic Commerce" with HEONIX AI logo.
- **Voiceover:**
  "Hello everyone! In outpatient healthcare and dental clinics worldwide, 20% to 30% of booked appointments result in patient no-shows. That leads to idle doctor time, administrative chaos, and billions in lost clinic revenue. Today, we introduce HELIO Agentic Commerce—an autonomous AI agent built to eliminate clinical no-shows using the PayPal developer platform."

### [00:30 - 01:15] Architecture & Clinical Safety Guard
- **Screen:** Show architecture flow diagram or the terminal running `paypal_agentic_booking_engine.py`.
- **Voiceover:**
  "HELIO isn't just a simple chatbot. It is a multi-agent deterministic system. When a patient messages the clinic over WhatsApp or web chat, HELIO first runs a clinical safety triage check. If an emergency like chest pain is detected, it instantly escalates to emergency services. But for routine bookings, it queries real-time doctor availability, locks the slot for 15 minutes, and autonomously invokes the PayPal Orders v2 API."

### [01:15 - 02:00] Live Demonstration: Dynamic PayPal Deposit Flow
- **Screen:** Split screen or sequence:
  1. Terminal showing patient message asking for dentist appointment.
  2. Helio replying with the reserved time and generating a dynamic PayPal Sandbox payment link.
  3. Browser opening the PayPal Sandbox checkout page with the $15.00 consultation deposit.
  4. Clicking "Approve Payment" in Sandbox.
- **Voiceover:**
  "Watch this live. The patient requests an appointment for tomorrow. Helio checks the calendar, reserves Dr. Senthil Kumar's 10:30 AM dental slot, and autonomously generates a personalized PayPal Sandbox deposit invoice for $15. The patient clicks the link, approves the transaction via PayPal, and completes the commitment deposit with zero front-desk friction."

### [02:00 - 02:30] Webhook Reconciliation & Automated Confirmation
- **Screen:** Terminal showing `handle_payment_webhook` receiving `PAYMENT.CAPTURE.COMPLETED`. Status changes to `CONFIRMED`.
- **Voiceover:**
  "Instantly, PayPal sends a webhook event back to Helio. The engine reconciles the transaction, verifies the capture ID, locks the doctor's calendar permanently, and issues an instant confirmation receipt. No human receptionist had to follow up, verify receipts, or manually update spreadsheets."

### [02:30 - 02:50] Conclusion & Why Agentic Commerce Wins
- **Screen:** Show `https://heonixai.in` and GitHub repository.
- **Voiceover:**
  "By combining autonomous clinical reasoning with PayPal's robust payment infrastructure, HELIO transforms how clinics operate, eliminating no-shows and securing doctor revenue autonomously. Built by HEONIX AI for the PayPal AI Hackathon 2026. Thank you!"
