# Agent Gatekeeper for Wells Fargo

**Candidate Name:** Vaishnavi Joshi  
**Student Enrollment Number:** PGD202572385  
**Domain Assigned:** Bank (Last Digit: `5`)  
**Enterprise Target:** Wells Fargo & Company  
**Actions Supported:** `view_balance`, `pay_bill`, `transfer_money`  

---

## Project Overview

The **Agent Gatekeeper** is an autonomous policy enforcement proxy designed for commercial banking. Built in response to the late 2026 emergence of autonomous personal AI agents executing retail transactions, the system resolves the operational and legal friction introduced by major banks:
1. **Wells Fargo Online Access Agreement §15 (Nov 24, 2026):** Mandates that customers using third-party AI agents do so at their own risk and must maintain verifiable proof if they revoke an agent's access.
2. **JPMorgan Chase Perimeter Defenses:** Outright blocking of transactional third-party agents to prevent systemic "rogue agent" attacks while allowing read-only balance aggregation.
3. **Delta Air Lines Policy:** Zero tolerance for third-party commercial booking agents.
4. **CFPB & Federal Reserve Regulation E Analysis (12 CFR Part 1005):** Navigating the legal tension between statutory shields against unauthorized electronic fund transfers and banks' contractual shifts of loss onto consumers.

---

## Key Governance Rules & Rationale

| Rule | Name | Condition | Decision | Explanation |
| :---: | :--- | :--- | :---: | :--- |
| **Rule 1** | **Unknown Agent Block** | Agent not in whitelist registry | **BLOCK** | Rejects unverified third-party software credentials. |
| **Rule 2** | **Revoked Agent Block** | Agent status is `REVOKED` | **BLOCK** | Enforces Wells Fargo Section 15 and outputs proof receipt. |
| **Rule 3** | **Read-Only Allow** | Action is `view_balance` | **ALLOW** | Read-only inspection posture with zero balance modification. |
| **Rule 4** | **Low-Value Autonomous Allow** | Amount $\le \$100.00$ | **ALLOW** | Frictionless execution of routine utility bills and subscriptions. |
| **Rule 5** | **High-Value Step-Up Confirm** | $\$100.00 < \text{Amount} \le \$1,000.00$ | **ASK CUSTOMER** | Mandates out-of-band human confirmation (OTP/Push). |
| **Rule 6** | **Excessive Ceiling Block** | Amount $> \$1,000.00$ | **BLOCK** | Hard ceiling preventing catastrophic rogue agent wire drain. |
| **Rule 7** | **Parameter Protocol Block** | Invalid action or negative amount | **BLOCK** | Integrity barrier against prompt injection or exploit attempts. |

> **Spending Limit Justification:**  
> *"The $100.00 autonomous spending limit was chosen based on consumer retail banking benchmarks where routine recurring utility bills and daily subscriptions typically fall under $100.00, providing user convenience while bounding potential financial exposure from AI agent hallucinations or drift before triggering mandatory human confirmation."*

---

## Deliverables & File Layout

```
agent-gatekeeper-PGD202572385/
├── index.html                           # Standalone responsive web dashboard (Step 3 UI)
├── gatekeeper.py                        # Core Python engine & CLI (Standard Library only)
├── test_suite.py                        # Automated test harness for the 6 Step 4 test cases
├── generate_pdf_report.py               # Generates the official 2-page PDF report
├── Agent_Gatekeeper_Report_PGD202572385.pdf # Official 2-page academic report (PDF)
├── report.md                            # Markdown transcript of the 2-page report
├── report.html                          # Print-optimized HTML layout for report
├── rules.json                           # Machine-readable rule definitions & thresholds
├── rules.md                             # Step 2 formal rules specification
├── test_results.md                      # Step 4 verification matrix & logs
├── PROMPTS.md                           # Main prompts given and student review modifications
├── VIDEO_SCRIPT.md                      # Exact 2-minute timed script for video presentation
├── GIT_GUIDE.md                         # Instructions to push repo with 3 commit dates
├── init_git_repo.ps1                    # Script creating 3 distinct dated git commits
├── agent_registry.json                  # Persistent agent directory & revocation receipts
├── audit_log.json                       # Real-time JSON audit trail
└── audit_log.csv                        # Real-time CSV audit trail
```

---

## How to Run

### 1. Web Application (Interactive Dashboard)
Simply double-click `index.html` or open it in any web browser (Google Chrome, Microsoft Edge, Firefox):
- Displays Candidate Enrollment: **`PGD202572385`**
- Interactive Request Simulator
- 1-Click "Execute 6 Tests" runner with PASS badges
- Wells Fargo Revocation Proof Generator
- Real-time Audit Log with CSV download

### 2. Python Core Engine & CLI
```bash
python gatekeeper.py
```

### 3. Automated 6-Case Test Suite
```bash
python test_suite.py
```

---

## Step 4: Verification Matrix Summary

| Case | Scenario | Input | Expected | Actual | Rule | Status |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: |
| 1 | Known agent, read-only action | FinBot-Alpha &bull; view_balance | **ALLOW** | **ALLOW** | Rule 3 | **PASS** |
| 2 | Unknown agent attempting action | RogueScraper-99 &bull; view_balance | **BLOCK** | **BLOCK** | Rule 1 | **PASS** |
| 3 | Payment above autonomous limit | FinBot-Alpha &bull; pay_bill ($350) | **ASK CUSTOMER** | **ASK CUSTOMER** | Rule 5 | **PASS** |
| 4 | Payment below autonomous limit | FinBot-Alpha &bull; pay_bill ($42.50) | **ALLOW** | **ALLOW** | Rule 4 | **PASS** |
| 5 | Revoked agent acting (Wells Fargo) | BudgetAssist-Revoked &bull; pay_bill | **BLOCK** | **BLOCK** | Rule 2 | **PASS** |
| 6 | High-risk excessive wire ceiling | FinBot-Alpha &bull; transfer ($5,000) | **BLOCK** | **BLOCK** | Rule 6 | **PASS** |
