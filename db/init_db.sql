CREATE TABLE IF NOT EXISTS client (
    transaction_id INTEGER PRIMARY KEY,
    transaction_datetime TEXT,
    transaction_type TEXT,
    transaction_amount REAL,
    transaction_status TEXT,
    balance_after_transaction REAL,
    channel TEXT,
    fee_applied REAL
);
