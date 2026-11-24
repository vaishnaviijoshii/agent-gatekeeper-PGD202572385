# Step 2: Gatekeeper Rules Specification

**Candidate Name:** Vaishnavi Joshi  
**Student Enrollment Number:** PGD202572385  
**Assigned Sector:** Bank (Last Digit: `5`)  
**Target Enterprise:** Wells Fargo & Company  
**Supported Actions:** `view_balance`, `pay_bill`, `transfer_money`  

---

## 1. Spending Limit Justification
> **Spending Limit Justification:**  
> *"The $100.00 autonomous spending limit was chosen based on consumer retail banking benchmarks where routine recurring utility bills and daily subscriptions typically fall under $100.00, providing user convenience while bounding potential financial exposure from AI agent hallucinations or drift before triggering mandatory human confirmation."*

---

## 2. Gatekeeper Rule Set (7 Rules)

| Rule ID | Rule Name | Condition | Decision | Enforcement Rationale |
| :---: | :--- | :--- | :---: | :--- |
| **Rule 1** | **Unknown Agent Rejection** | Agent name is absent from the bank's registered agent whitelist. | **BLOCK** | Unauthenticated, third-party agents attempting to interface with banking credentials represent an unverified security threat. |
| **Rule 2** | **Revoked Agent Enforcement** *(Wells Fargo Clause)* | Agent exists in database but status is marked `REVOKED`. | **BLOCK** | Addresses Wells Fargo's Nov 24, 2026 agreement update. A revoked agent must be prevented from acting, and the stored timestamp + cryptographic hash receipt serves as legal proof of revocation. |
| **Rule 3** | **Read-Only Balance Inquiry** | Action is `view_balance` and agent is `ACTIVE`. | **ALLOW** | Read-only inspection does not alter balances or move funds, aligning with JPMorgan's aggregated data sharing policies. |
| **Rule 4** | **Autonomous Low-Value Monetary Action** | Action is `pay_bill` or `transfer_money`, amount $\le \$100.00$, and agent is `ACTIVE`. | **ALLOW** | Permits frictionless automated execution of minor, recurring obligations (e.g., streaming subscriptions, water utility bills) within risk tolerance. |
| **Rule 5** | **Elevated Monetary Action (Step-Up)** | Action is `pay_bill` or `transfer_money`, amount is between $\$100.01$ and $\$1,000.00$, and agent is `ACTIVE`. | **ASK CUSTOMER** | Requires out-of-band customer confirmation (push notification or SMS OTP) before funds are disbursed, stopping runaway AI execution. |
| **Rule 6** | **Excessive Value Hard Safety Ceiling** | Action is `pay_bill` or `transfer_money`, amount $>\$1,000.00$, and agent is `ACTIVE`. | **BLOCK** | Mitigates catastrophic "rogue agent" drain. High-value wires cannot be delegated to autonomous AI agents under any circumstances. |
| **Rule 7** | **Invalid Action or Protocol Parameter** | Action is not in (`view_balance`, `pay_bill`, `transfer_money`) or transaction amount $< \$0.00$. | **BLOCK** | Ensures API integrity and protects against prompt injection or parameter tampering. |

---

## 3. Decision Matrix Flowchart

```
                 [Incoming Agent Request]
                           │
             ┌─────────────┴─────────────┐
             ▼                           ▼
      Agent Registered? ────NO─────► [BLOCK: Rule 1]
             │ YES
             ▼
      Agent Revoked? ───────YES────► [BLOCK: Rule 2 (Logs Proof)]
             │ NO (ACTIVE)
             ▼
      Action == 'view_balance'? ──YES─► [ALLOW: Rule 3]
             │ NO
             ▼
      Action in ('pay_bill', 'transfer_money')?
             ├── NO or Amount < 0 ──► [BLOCK: Rule 7]
             │
             ├── Amount <= $100 ────► [ALLOW: Rule 4]
             │
             ├── $100 < Amount <= $1000 ─► [ASK CUSTOMER: Rule 5]
             │
             └── Amount > $1000 ────► [BLOCK: Rule 6]
```
