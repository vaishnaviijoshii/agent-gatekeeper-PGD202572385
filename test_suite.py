"""
================================================================================
TEST SUITE FOR AGENT GATEKEEPER (WELLS FARGO)
Enrollment Number: PGD202572385
Executes the 6 mandatory test cases required by Step 4:
1. Known agent doing a read-only action
2. An unknown agent
3. A payment above your limit ($100.00 limit -> $350.00)
4. A payment below your limit ($100.00 limit -> $42.50)
5. A revoked agent trying to act
6. Case of own choice: High-value unauthorized wire ($5,000.00 > $1,000 safety ceiling)
================================================================================
"""

import sys
import os
import json

# Ensure gatekeeper module can be imported
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gatekeeper import AgentGatekeeper, ENROLLMENT_NO

TEST_CASES = [
    {
        "case_num": 1,
        "title": "Known Agent doing Read-Only Action",
        "description": "Authenticated active agent checks account balance",
        "customer_id": "CUST-1001",
        "agent_name": "FinBot-Alpha",
        "action": "view_balance",
        "amount": 0.00,
        "expected_decision": "ALLOW",
        "expected_rule": 3
    },
    {
        "case_num": 2,
        "title": "Unknown Agent Attempting Action",
        "description": "Unregistered external AI agent tries to inspect balance",
        "customer_id": "CUST-1001",
        "agent_name": "RogueScraper-99",
        "action": "view_balance",
        "amount": 0.00,
        "expected_decision": "BLOCK",
        "expected_rule": 1
    },
    {
        "case_num": 3,
        "title": "Payment Above Autonomous Limit",
        "description": "Active agent attempts $350.00 bill pay (exceeds $100 limit)",
        "customer_id": "CUST-1001",
        "agent_name": "FinBot-Alpha",
        "action": "pay_bill",
        "amount": 350.00,
        "expected_decision": "ASK CUSTOMER",
        "expected_rule": 5
    },
    {
        "case_num": 4,
        "title": "Payment Below Autonomous Limit",
        "description": "Active agent pays $42.50 utility bill (under $100 limit)",
        "customer_id": "CUST-1001",
        "agent_name": "FinBot-Alpha",
        "action": "pay_bill",
        "amount": 42.50,
        "expected_decision": "ALLOW",
        "expected_rule": 4
    },
    {
        "case_num": 5,
        "title": "Revoked Agent Trying to Act",
        "description": "Revoked agent attempts $25.00 transaction (Wells Fargo Nov 24 clause)",
        "customer_id": "CUST-1001",
        "agent_name": "BudgetAssist-Revoked",
        "action": "pay_bill",
        "amount": 25.00,
        "expected_decision": "BLOCK",
        "expected_rule": 2
    },
    {
        "case_num": 6,
        "title": "Own Choice: Extreme High-Risk Wire Ceiling",
        "description": "Active agent attempts $5,000 wire transfer exceeding hard $1,000 ceiling",
        "customer_id": "CUST-1001",
        "agent_name": "FinBot-Alpha",
        "action": "transfer_money",
        "amount": 5000.00,
        "expected_decision": "BLOCK",
        "expected_rule": 6
    }
]


def run_compliance_tests():
    gatekeeper = AgentGatekeeper()
    print("\n" + "=" * 90)
    print(f" AGENT GATEKEEPER COMPLIANCE TEST MATRIX (Step 4)")
    print(f" Candidate: Vaishnavi Joshi | Enrollment: {ENROLLMENT_NO} | Bank: Wells Fargo")
    print("=" * 90)

    results = []
    all_passed = True

    for tc in TEST_CASES:
        res = gatekeeper.evaluate_request(
            tc["customer_id"],
            tc["agent_name"],
            tc["action"],
            tc["amount"]
        )
        passed = (res["decision"] == tc["expected_decision"] and res["rule_id"] == tc["expected_rule"])
        if not passed:
            all_passed = False

        record = {
            "case_num": tc["case_num"],
            "title": tc["title"],
            "agent": tc["agent_name"],
            "action": tc["action"],
            "amount": tc["amount"],
            "expected_decision": tc["expected_decision"],
            "expected_rule": tc["expected_rule"],
            "actual_decision": res["decision"],
            "actual_rule": res["rule_id"],
            "passed": passed,
            "reason": res["reason"],
            "audit_id": res["audit_id"]
        }
        results.append(record)

    # Print Table Form
    header = f"{'#':<3} | {'Test Case Description':<32} | {'Input (Agent/Action/Amt)':<28} | {'Expected':<12} | {'Actual':<12} | {'Rule':<6} | {'Status'}"
    print(header)
    print("-" * 115)

    for r in results:
        status_str = "[PASS]" if r["passed"] else "[FAIL]"
        input_desc = f"{r['agent']} / {r['action']} / ${r['amount']:.2f}"
        print(f"{r['case_num']:<3} | {r['title'][:32]:<32} | {input_desc[:28]:<28} | {r['expected_decision']:<12} | {r['actual_decision']:<12} | Rule {r['actual_rule']:<1} | {status_str}")

    print("=" * 115)
    if all_passed:
        print(">>> ALL 6 MANDATORY TEST CASES PASSED WITH 100% COMPLIANCE! <<<")
    else:
        print(">>> WARNING: SOME TEST CASES FAILED! CHECK ENGINE LOGIC! <<<")
    print("=" * 115)

    # Save Markdown Report
    md_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "test_results.md")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(f"# Step 4: Verification & Test Results Table\n\n")
        f.write(f"**Enrollment Number:** {ENROLLMENT_NO}  \n")
        f.write(f"**Assigned Sector:** Bank (Digit 5 - Wells Fargo)  \n")
        f.write(f"**Overall Result:** {'ALL 6 TESTS PASSED (100%)' if all_passed else 'FAILURES DETECTED'}  \n\n")
        f.write("| Case # | Test Scenario | Input Request | Expected Decision | Actual Decision | Triggered Rule | Status |\n")
        f.write("| :---: | :--- | :--- | :---: | :---: | :---: | :---: |\n")
        for r in results:
            f.write(f"| **{r['case_num']}** | {r['title']} | `{r['agent']}` &bull; `{r['action']}` &bull; `${r['amount']:.2f}` | **{r['expected_decision']}** | **{r['actual_decision']}** | Rule {r['actual_rule']} | {'`PASS`' if r['passed'] else '`FAIL`'} |\n")
        f.write("\n\n### Detailed Log and Decision Rationale\n\n")
        for r in results:
            f.write(f"#### Case {r['case_num']}: {r['title']}\n")
            f.write(f"- **Agent:** `{r['agent']}` | **Action:** `{r['action']}` | **Amount:** `${r['amount']:.2f}`\n")
            f.write(f"- **Decision:** `{r['actual_decision']}` (Rule {r['actual_rule']})\n")
            f.write(f"- **Gatekeeper Reason:** {r['reason']}\n")
            f.write(f"- **Audit ID:** `{r['audit_id']}`\n\n")

    print(f"\n[INFO] Generated markdown test summary: {md_path}")
    return results


if __name__ == "__main__":
    run_compliance_tests()
