# PROMPTS.md: Development Interaction & Verification Log

**Candidate Name:** Vaishnavi Joshi  
**Student Enrollment Number:** PGD202572385  
**Project:** Agent Gatekeeper for Wells Fargo  
**Domain:** Bank (Enrollment Last Digit: `5`)  
**AI Coding Agent Used:** Google Antigravity (Powered by Gemini 3.8 Flash High)  

---

## 1. Main Instructions Given to the Coding Agent

Below is the chronological sequence of core engineering instructions provided to build the Agent Gatekeeper system:

### Prompt 1: Domain Mapping & Regulatory Rule Formulation
> *"My enrollment number is `PGD202572385`. The last digit is 5, which assigns me to a commercial bank enterprise. I choose Wells Fargo because of their landmark updated Online Access Agreement (Section 15, effective 24 Nov 2026) regarding customer liability for third-party AI agents and proof-of-revocation mandates. Formulate 7 to 8 clear, deterministic rules covering:
> 1. Blocking unregistered/unknown AI agents.
> 2. Enforcing revoked agent status with proof retention.
> 3. Allowing read-only balance checks (`view_balance`).
> 4. Allowing low-value monetary actions (`pay_bill`, `transfer_money`) up to an autonomous spending limit.
> 5. Requiring customer step-up confirmation (`ASK CUSTOMER`) for mid-tier transactions.
> 6. Blocking catastrophic excessive transfers above a hard safety ceiling.
> 7. Rejecting invalid actions or negative values.
> Provide a clear, one-line justification for the autonomous spending limit."*

### Prompt 2: Prototype Core Engine Architecture (`gatekeeper.py`)
> *"Implement the prototype in Python 3 using standard library modules (zero external pip dependencies for maximum portability). The prototype must:
> - Display my enrollment number `PGD202572385` prominently on start and in every audit entry.
> - Take a request tuple: `(customer_id, agent_name, action, amount)`.
> - Return decisions: `ALLOW`, `ASK CUSTOMER`, or `BLOCK` along with the specific triggered `rule_id` and explanatory `reason`.
> - Persist an append-only audit trail in both JSON and CSV format recording UTC timestamps, request payloads, and verdict metadata.
> - Implement agent registration and a revocation mechanism (`revoke_agent`) that creates a cryptographic proof receipt with a SHA-256 fingerprint and timestamp to solve Wells Fargo's legal burden of proof.
> - Provide an interactive CLI for testing."*

### Prompt 3: Compliance Test Harness Formulation (`test_suite.py`)
> *"Construct a rigorous test suite executing the 6 mandatory operational test cases:
> 1. Known agent doing a read-only action (`view_balance`).
> 2. An unknown agent trying to act.
> 3. A payment above the autonomous limit ($350.00).
> 4. A payment below the autonomous limit ($42.50).
> 5. A revoked agent attempting to act (Wells Fargo Section 15 check).
> 6. An own-choice scenario: catastrophic high-value wire transfer ($5,000.00 > $1,000 ceiling).
> Assert that Expected equals Actual for all cases, output a clear ASCII matrix, and export `test_results.md`."*

### Prompt 4: Modern Interactive Web Application (`index.html`)
> *"Create a standalone, responsive, single-file HTML5/CSS/JavaScript web dashboard:
> - Display Wells Fargo branding and my candidate enrollment number `PGD202572385` at the top.
> - Include an interactive Request Simulator with real-time colored decision badges (Green for `ALLOW`, Amber for `ASK CUSTOMER`, Red for `BLOCK`).
> - Include an Agent Registry with live status tags and a 'Revoke Access' button that pops up an 'Official Proof of Revocation Certificate' that can be copied or printed.
> - Add a 1-click 'Run 6 Required Tests' button that renders the complete test matrix with PASS/FAIL badges.
> - Include an Audit Log table with real-time updates and CSV export."*

### Prompt 5: Academic Report & PDF Generation
> *"Generate a strict 2-page publication-quality executive report in PDF format (`Agent_Gatekeeper_Report_PGD202572385.pdf`) covering:
> 1. Problem understanding and sources (Wells Fargo agreement, JPMorgan Chase, Delta, and a 4th source: CFPB & Federal Reserve Regulation E analysis).
> 2. The 7 rules and spending limit rationale.
> 3. The 6-case test results table.
> 4. The Wells Fargo revocation proof resolution.
> 5. A critical business paragraph on what the company gains and loses by blocking agents completely."*

---

## 2. Things Checked and Changed Myself (Student Verification & Modifications)

To ensure technical rigor, legal fidelity, and code correctness, I conducted hands-on review and implemented the following critical adjustments:

1. **Enforced UTC ISO-8601 Timestamps & Digital Receipt Verification:**
   - *Review finding:* Initially, local machine timestamps without timezone offsets were being recorded.
   - *Modification:* In `gatekeeper.py` and `index.html`, I modified the timestamp generation to strictly utilize `timezone.utc.isoformat()` (e.g., `2026-11-24T12:00:00+00:00`). This is crucial because Wells Fargo's Section 15 dispute arbitrations require unambiguous, non-repudiable proof of the exact moment an agent was revoked relative to transaction attempts.
   - *Cryptographic Receipt:* I verified that the revocation receipt uses a deterministic SHA-256 digest (`WF-REV-YYYYMMDD-<HASH>`) combining `agent_name`, `customer_id`, and `revocation_timestamp`.

2. **Edge-Case Validation for Malformed & Negative Amounts:**
   - *Review finding:* If an external agent passed a negative payment amount (e.g., `-$150.00` to simulate a refund exploit) or an arbitrary string, the engine did not cleanly trap it before rule evaluation.
   - *Modification:* Added **Rule 7** (`Invalid Action or Parameter Block`) as the first perimeter check. It validates that the requested action belongs to `['view_balance', 'pay_bill', 'transfer_money']` and that `amount >= 0.0`. Any exploit attempt receives an immediate `BLOCK` verdict.

3. **Autonomous Limit Boundary Precision:**
   - *Review finding:* Verified exact boundary condition behavior:
     - An amount of exactly `$100.00` evaluates to **Rule 4 (`ALLOW`)**.
     - An amount of `$100.01` properly transitions to **Rule 5 (`ASK CUSTOMER`)**.
     - An amount of `$1,000.01` properly transitions to **Rule 6 (`BLOCK`)**.
   - Tested edge amounts to guarantee zero off-by-one errors in threshold comparisons.

4. **Self-Contained Offline Web App Resilience:**
   - *Review finding:* In an air-gapped test environment without internet access, external Tailwind CDN styling might not load.
   - *Modification:* Added embedded fallback CSS rules for `.wf-red`, `.badge-allow`, `.badge-ask`, `.badge-block`, and custom container layouts in `index.html`, ensuring the web dashboard renders with full fidelity both online and offline.
