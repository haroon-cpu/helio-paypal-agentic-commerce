# Devpost Submission Form Content: PayPal AI Hackathon 2026

**Project Title:**
HELIO: Autonomous Clinical Booking & PayPal Agentic Commerce Engine

**Elevator Pitch (One-liner):**
An autonomous multi-agent clinical front-desk engine that eliminates clinic no-shows by performing safety triage, locking doctor slots, and autonomously capturing consultation advance deposits via the PayPal Orders v2 API.

---

### What it does:
HELIO is an autonomous agentic commerce system designed for outpatient healthcare clinics. When patients initiate an appointment request via messaging, HELIO:
1. Conducts safety triage to route emergency symptoms immediately to emergency services.
2. Checks doctor calendars in real time and applies a 15-minute ACID reservation lock on the chosen slot.
3. Dynamically invokes PayPal Sandbox Orders v2 API to generate an authorized deposit checkout link.
4. Listens for payment capture webhook events to transition the slot from pending to confirmed, sending automated confirmation receipts to both patient and clinic.

### How we built it:
- **Core Engine:** Python-based multi-agent state machine utilizing deterministic guardrails and asynchronous event loops.
- **PayPal Integration:** Integrated PayPal Developer Sandbox via REST APIs (Orders v2 / Invoicing) to programmatically create, authorize, and capture consultation commitment deposits.
- **Webhook Reconciliation:** Implemented automated webhook verification to ensure idempotent database updates upon payment capture.
- **Testing:** Validated across automated scenario tests ensuring zero race conditions during simultaneous booking attempts.

### Challenges we ran into:
Ensuring that dynamic payment generation did not introduce booking latency for patients chatting in real time. We solved this by decoupling slot reservation locks from payment capture, using a 15-minute time-to-live (TTL) expiration loop that automatically releases doctor slots if the PayPal transaction is abandoned.

### Accomplishments that we're proud of:
Building a complete, production-ready Agentic Commerce workflow where an AI agent doesn't just chat, but autonomously negotiates schedules and executes financial transactions with zero human intervention.

### What we learned:
How to leverage PayPal's Sandbox APIs within an agentic workflow to transform traditional clinical administration into a streamlined, autonomous commerce experience.

### What's next for HELIO:
Expanding multi-currency payment acceptance for international medical tourism clinics across India and the UAE, and deploying our agentic commerce stack to 50+ founding clinics in 2027.

### What updated since Oct 1, 2026 (Rule Requirement):
Since October 1, 2026, we developed the entire autonomous PayPal Sandbox integration layer, implemented the dynamic Orders v2 deposit invoice generator, integrated the 15-minute ACID reservation lock, and built the webhook verification callback handler specifically for this hackathon.
