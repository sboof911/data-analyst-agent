# Bank Client CSV Column Guide (Condensed)

**Note:** All transactions belong to a single client.

- **transaction_id**: Unique integer ID  
- **transaction_datetime**: Date and time of transaction (YYYY-MM-DD HH:MM:SS)  
- **transaction_type**: Deposit, Withdrawal, Transfer  
- **transaction_amount**: Amount involved (float)  
- **transaction_status**: Completed, Pending, Canceled  
- **balance_after_transaction**: Balance after transaction (float)  
- **channel**: ATM, Branch, Online  
- **fee_applied**: Fee charged, subtracted from balance (float)