# 2-Minute Screen Recording Script & Demonstration Guide

**Candidate Name:** Vaishnavi Joshi  
**Student Enrollment Number:** PGD202572385  
**Assigned Sector:** Bank (Last Digit: `5`) &bull; Wells Fargo  
**Target Time:** Under 2 minutes (approx. 1 min 45 sec to 1 min 55 sec)  
**Tools to Show on Screen:** Web Interface (`index.html`) in your browser OR Terminal running `test_suite.py` / `gatekeeper.py`.

---

## Preparation Before Recording:
1. Double-click `index.html` to open it in Microsoft Edge or Google Chrome.
2. (Optional side-by-side): Have a PowerShell or Command Prompt open in the project folder with `python test_suite.py` ready.
3. Start your screen recorder (OBS, Windows Game Bar `Win + G`, or Loom).

---

## Timed Voiceover Script (Read this while performing actions):

### [0:00 - 0:20] Introduction & Problem Setup
> *"Hello, my name is **Vaishnavi Joshi**, and my enrollment number is **PGD202572385**.  
> Because the last digit of my enrollment number is **5**, my assigned enterprise category is a **commercial bank**, and I have built the **Agent Gatekeeper prototype for Wells Fargo**.  
> In November 2026, Wells Fargo updated Section 15 of its Online Access Agreement, mandating that customers using third-party AI agents do so at their own risk, and must retain verifiable proof if they revoke an agent's access. Our Gatekeeper solves this problem."*

### [0:20 - 0:45] Explaining the Rules & Spending Limit
> *"Here on screen, you can see my enrollment number **PGD202572385** displayed on the dashboard.  
> Our system enforces 7 clear governance rules:  
> - **Rule 1** blocks unknown or unregistered AI agents.  
> - **Rule 2** blocks revoked agents and produces cryptographic proof of revocation.  
> - **Rule 3** allows read-only balance inquiries.  
> - **Rule 4** allows low-value autonomous payments up to **$100.00**. We chose $100 because standard consumer utility bills and subscriptions fall under this limit, balancing convenience with low fraud risk.  
> - **Rule 5** requires customer step-up confirmation for amounts between **$100.01 and $1,000.00**.  
> - And **Rule 6** places a hard ceiling blocking any automated transfer above **$1,000.00** to stop catastrophic rogue agent drain."*

### [0:45 - 1:25] Running the 6 Compliance Tests (Click "Execute 6 Tests" Button)
> *(Click the green **"Execute 6 Tests"** button in `index.html`)*  
> *"Now let's execute the 6 required test cases on screen:  
> 1. **Case 1:** Known agent `FinBot-Alpha` viewing balance &rarr; The result is **ALLOW** under **Rule 3**.  
> 2. **Case 2:** Unknown agent `RogueScraper-99` attempting an action &rarr; The result is **BLOCK** under **Rule 1**.  
> 3. **Case 3:** Active agent paying a $350 bill, which is above our $100 limit &rarr; The result is **ASK CUSTOMER** under **Rule 5**.  
> 4. **Case 4:** Active agent paying a $42.50 utility bill, below our limit &rarr; The result is **ALLOW** under **Rule 4**.  
> 5. **Case 5:** Revoked agent `BudgetAssist-Revoked` trying to act &rarr; The result is **BLOCK** under **Rule 2**, referencing the exact revocation timestamp.  
> 6. **Case 6 (Own Choice):** An extreme transfer of $5,000 &rarr; The result is **BLOCK** under **Rule 6** because it exceeds our hard safety ceiling.  
> As you can see, all 6 test cases show **100% PASS**."*

### [1:25 - 1:45] Demonstrating Agent Revocation & Proof Receipt (The Wells Fargo Problem)
> *(Click **"View Proof"** or click **"Revoke Access"** on an active agent)*  
> *"Finally, here is the solution to the Wells Fargo problem: when a customer revokes an agent, our Gatekeeper instantly logs the UTC timestamp and generates this verifiable **Cryptographic Proof of Revocation Certificate** with a SHA-256 receipt ID. This provides the exact legal documentation Wells Fargo requires to protect customers from post-revocation liability.  
> Every request and decision is also recorded in our immutable audit log."*

### [1:45 - 2:00] Conclusion
> *"In summary, the Wells Fargo Agent Gatekeeper provides safe autonomous banking automation while guarding against unauthorized transfers and rogue agents.  
> Thank you! Enrollment Number: **PGD202572385**."*
