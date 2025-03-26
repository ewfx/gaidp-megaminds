## Delete this file

Instead place your source files here

console logs

expected output 
Generated Profiling Rules:
- Transaction Amount should match Reported Amount, with a 1% tolerance for cross-currency conversions.
- Account Balance should not be negative unless marked as an overdraft (OD).
- Currency must be a valid ISO 4217 code.
- Transactions above $10,000 in cross-border transfers must have mandatory remarks.
- Transactions older than 365 days or in the future should trigger validation alerts.
- High-risk transactions (>$55,000 in high-risk countries) must be flagged.
- Round-number transactions (e.g., $1000, $5000) require additional validation for money laundering risks.

Risk scoring completed! Results saved to transactions_with_risk.csv.



result file

Customer ID,Account Balance,Transaction Amount,Reported Amount,Currency,Country,Transaction Date,Validation Status,Risk Score,Anomaly,Remediation Action
1001,15000,500,500,USD,US,2025-02-25,Valid,2,0,None
1002,32000,1200,1200,INR,IND,2025-02-20,Valid,1,0,None
1003,-5000,300,300,GBP,UK,2025-02-18,Overdraft Flag Missing,7,-1,Mark account as OD or correct balance
1004,70000,2000,1800,USD,US,2015-02-28,Amount Mismatch,4,-1,Review and reconcile reported vs actual amount
1005,200000,60000,60000,EUR,FR,2025-03-01,Future Transaction,9,-1,Check for incorrect date entry

