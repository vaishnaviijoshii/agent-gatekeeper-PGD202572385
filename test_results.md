# Step 4: Verification & Test Results Table

**Enrollment Number:** PGD202572385  
**Assigned Sector:** Bank (Digit 5 - Wells Fargo)  
**Overall Result:** ALL 6 TESTS PASSED (100%)  

| Case # | Test Scenario | Input Request | Expected Decision | Actual Decision | Triggered Rule | Status |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: |
| **1** | Known Agent doing Read-Only Action | `FinBot-Alpha` &bull; `view_balance` &bull; `$0.00` | **ALLOW** | **ALLOW** | Rule 3 | `PASS` |
| **2** | Unknown Agent Attempting Action | `RogueScraper-99` &bull; `view_balance` &bull; `$0.00` | **BLOCK** | **BLOCK** | Rule 1 | `PASS` |
| **3** | Payment Above Autonomous Limit | `FinBot-Alpha` &bull; `pay_bill` &bull; `$350.00` | **ASK CUSTOMER** | **ASK CUSTOMER** | Rule 5 | `PASS` |
| **4** | Payment Below Autonomous Limit | `FinBot-Alpha` &bull; `pay_bill` &bull; `$42.50` | **ALLOW** | **ALLOW** | Rule 4 | `PASS` |
| **5** | Revoked Agent Trying to Act | `BudgetAssist-Revoked` &bull; `pay_bill` &bull; `$25.00` | **BLOCK** | **BLOCK** | Rule 2 | `PASS` |
| **6** | Own Choice: Extreme High-Risk Wire Ceiling | `FinBot-Alpha` &bull; `transfer_money` &bull; `$5000.00` | **BLOCK** | **BLOCK** | Rule 6 | `PASS` |


### Detailed Log and Decision Rationale

#### Case 1: Known Agent doing Read-Only Action
- **Agent:** `FinBot-Alpha` | **Action:** `view_balance` | **Amount:** `$0.00`
- **Decision:** `ALLOW` (Rule 3)
- **Gatekeeper Reason:** Read-only balance inspection permitted for authenticated active agent 'FinBot-Alpha'.
- **Audit ID:** `AUD-20261124122808-20ED`

#### Case 2: Unknown Agent Attempting Action
- **Agent:** `RogueScraper-99` | **Action:** `view_balance` | **Amount:** `$0.00`
- **Decision:** `BLOCK` (Rule 1)
- **Gatekeeper Reason:** Agent 'RogueScraper-99' is not registered with Wells Fargo. Unauthenticated outside AI agents are strictly blocked.
- **Audit ID:** `AUD-20261124122808-B0D0`

#### Case 3: Payment Above Autonomous Limit
- **Agent:** `FinBot-Alpha` | **Action:** `pay_bill` | **Amount:** `$350.00`
- **Decision:** `ASK CUSTOMER` (Rule 5)
- **Gatekeeper Reason:** Transaction amount ($350.00) exceeds autonomous threshold ($100.00). Step-up customer out-of-band authorization required.
- **Audit ID:** `AUD-20261124122808-6C2B`

#### Case 4: Payment Below Autonomous Limit
- **Agent:** `FinBot-Alpha` | **Action:** `pay_bill` | **Amount:** `$42.50`
- **Decision:** `ALLOW` (Rule 4)
- **Gatekeeper Reason:** Transaction amount ($42.50) is within the autonomous spending threshold of $100.00.
- **Audit ID:** `AUD-20261124122808-2508`

#### Case 5: Revoked Agent Trying to Act
- **Agent:** `BudgetAssist-Revoked` | **Action:** `pay_bill` | **Amount:** `$25.00`
- **Decision:** `BLOCK` (Rule 2)
- **Gatekeeper Reason:** Agent 'BudgetAssist-Revoked' was revoked by customer on 2026-11-20T10:15:00+00:00. (Proof Receipt: WF-REV-8E12DE2FCF1AAA37). Revoked agents are blocked from all activity.
- **Audit ID:** `AUD-20261124122808-256D`

#### Case 6: Own Choice: Extreme High-Risk Wire Ceiling
- **Agent:** `FinBot-Alpha` | **Action:** `transfer_money` | **Amount:** `$5000.00`
- **Decision:** `BLOCK` (Rule 6)
- **Gatekeeper Reason:** Transaction amount ($5000.00) exceeds absolute AI safety ceiling ($1000.00). Autonomous agents cannot initiate high-risk wires.
- **Audit ID:** `AUD-20261124122808-5457`

