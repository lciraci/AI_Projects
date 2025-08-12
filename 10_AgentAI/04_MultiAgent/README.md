# Multi-Agent Customer Service Workflow

This project demonstrates a **minimal multi-agent system** for handling customer service requests using two specialized AI agents:
- **Triage Agent** – Collects essential details from the customer and proposes **exactly one actionable next step**.
- **Concierge QA Agent** – Acts as a quality gate, approving or requesting refinements to ensure clarity, policy compliance, and optimal customer experience.

The agents operate in a **round-robin loop** until the Concierge QA Agent returns `"APPROVE"` or a termination condition is met.

---

## Features

- **Minimal Roles** for clarity and faster iteration:
  1. **Triage Agent** – Gathers the issue, urgency, and next step.
  2. **Concierge QA Agent** – Validates and approves/refines.
- **Termination Condition** – Stops when QA outputs `"APPROVE"`.
- **Structured Output** – JSON contract for triage to make responses machine-checkable.
- **Refinement Loop** – QA can request improvements with short guidance (`REFINE: ...`).
- **Async Streaming** – Process results as they arrive.

---

## Example Flow

1. **Customer Input**:  
   `"My order #A123 arrived damaged and I need a replacement."`
   
2. **Triage Agent Output**:  
   ```json
   {
     "issue": "Order #A123 arrived damaged",
     "user_id": "A123",
     "urgency": "high",
     "next_action": "Offer a prepaid return label and create RMA",
     "user_reply": "I'm sorry your order arrived damaged. I will send a return label and start a replacement."
   }
