# HELIO: Autonomous Clinical Appointment Booking & Deposit Engine via PayPal

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Track: Agentic Commerce](https://img.shields.io/badge/PayPal_AI_Hackathon-Best_Use_of_Agentic_Commerce-green.svg)](https://paypalaihackathon.devpost.com/)

An autonomous AI agentic commerce solution solving the $150 Billion healthcare no-show crisis. Built by **HEONIX AI**, this engine enables autonomous clinical scheduling, patient safety triage, and automated consultation advance deposit capture via PayPal Sandbox Orders v2 API.

---

## 🏥 The Problem: Clinical No-Shows & Revenue Leakage
In outpatient clinics and dental practices worldwide, **20% to 30% of scheduled appointments result in patient no-shows**, causing massive idle doctor capacity and loss of revenue. Traditional front-desk staff cannot chase deposits via manual phone calls.

## ⚡ The Solution: HELIO Agentic Commerce
HELIO is a multi-agent clinical front-desk system that interacts with patients over messaging channels (WhatsApp/Web):
1. **Safety Triage Guard:** Detects critical emergency keywords (e.g., chest pain, heavy bleeding) and immediately escalates to emergency services (dial 108/911) with zero automated delay.
2. **ACID Slot Reservation:** Queries real-time doctor availability and applies a 15-minute temporary reservation lock.
3. **Autonomous PayPal Deposit Invoice:** Dynamically generates a PayPal Orders v2 checkout link for a small commitment deposit (e.g., $15.00 USD).
4. **Instant Webhook Reconciliation:** Listens for PayPal `PAYMENT.CAPTURE.COMPLETED` events, automatically transitions the slot from `PENDING` to `CONFIRMED`, and notifies the clinic's management dashboard.

---

## 🛠️ Architecture Overview

```text
[ Patient Message ]
       │
       ▼
[ Clinical Safety Triage ] ──► (Emergency Detected? ──► Dial 108 Alert)
       │ (Safe)
       ▼
[ Slot Availability & Lock ]
       │
       ▼
[ PayPal Orders v2 Engine ] ──► Generates Dynamic Sandbox Approval Link
       │
       ▼
[ Patient Approves in Sandbox ]
       │
       ▼
[ PayPal Webhook Handler ] ──► Slot Confirmed & Doctor Calendar Locked
```

---

## 🚀 Quickstart & Live Simulation

Clone this repository and run the standalone simulation engine:

```bash
git clone https://github.com/heonixai/helio-paypal-agentic-commerce.git
cd helio-paypal-agentic-commerce
python3 paypal_agentic_booking_engine.py
```

### Sample Output:
```text
==================================================================
HELIO AGENTIC COMMERCE ENGINE - PAYPAL HACKATHON LIVE DEMO
==================================================================

[1] Patient (+919876543210): Hello, I want to book an appointment with a dentist for tomorrow morning

[2] Helio Agent Response:
Your consultation with Dr. Senthil Kumar (Dental) has been reserved for 2026-11-12 10:30 AM. To prevent no-shows and confirm your doctor's schedule, please approve the $15.0 deposit via PayPal: https://www.sandbox.paypal.com/checkoutnow?token=PAYID-B1F6C5C8EE2D

[3] Generated PayPal Order: PAYID-B1F6C5C8EE2D
    Deposit Approval Link: https://www.sandbox.paypal.com/checkoutnow?token=PAYID-B1F6C5C8EE2D

[4] Simulating Patient Completing PayPal Approval on Sandbox...
[5] Receiving PayPal Payment Capture Webhook Callback...

[6] Final Confirmation Event:
{
  "status": "SUCCESS",
  "reservation_id": "RES-9F46ACA5",
  "slot_time": "2026-11-12 10:30 AM",
  "doctor": "Dr. Senthil Kumar (Dental)",
  "confirmation_message": "Payment verified! Your appointment with Dr. Senthil Kumar (Dental) on 2026-11-12 10:30 AM is officially confirmed."
}
==================================================================
AGENTIC COMMERCE TRANSACTION COMPLETED WITH ZERO HUMAN INTERVENTION
==================================================================
```

---

## 🔒 Security & Code Moat Isolation
This repository serves as the public open-source adapter and demonstration package for the **PayPal AI Hackathon 2026**. It connects to HEONIX AI's proprietary clinical safety engine via secure REST endpoints without exposing internal database schemas or patient protected health information (PHI).

## 📄 License
This project is open-sourced under the [MIT License](LICENSE).
