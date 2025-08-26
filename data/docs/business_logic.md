# Bank Client Transactions — Business Logic (Condensed)

## Transaction Types
- Deposit: Add money to the account
- Withdrawal: Subtract money from the account
- Transfer: Send money to another account

## Status
- Only **Completed** transactions affect balance
- Pending and Canceled transactions are ignored

## Balance
- `balance_after_transaction` reflects updated balance after Completed transactions
- Fees (`fee_applied`) are subtracted from the balance but not included in `transaction_amount`

## Channels
- ATM, Branch, Online

## Calculations
- Spending by month: sum of Withdrawals
- Income by month: sum of Deposits
- Net change: last balance minus first balance in a period

## Agent Notes
- All data is for a single client
- Consider `transaction_datetime` for trend analysis (daily, weekly, monthly)
