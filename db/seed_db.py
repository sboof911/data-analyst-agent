import sqlite3
import pandas as pd
import os

# Paths
DB_PATH = os.path.join(os.path.dirname(__file__), 'bank_client.db')
SQL_PATH = os.path.join(os.path.dirname(__file__), 'init_db.sql')

def create_db(cursor):
	with open(SQL_PATH, 'r') as f:
		sql_script = f.read()
	cursor.executescript(sql_script)

def seed_db(csv_path):
	if not os.path.exists(csv_path):
		return

	df = pd.read_csv(csv_path)
	conn = sqlite3.connect(DB_PATH)
	cursor = conn.cursor()
	create_db(cursor)
	for _, row in df.iterrows():
		cursor.execute(
			"""
			INSERT INTO client (
				transaction_id, transaction_datetime, transaction_type, transaction_amount,
				transaction_status, balance_after_transaction, channel, fee_applied
			) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
			""",
			(
				int(row['transaction_id']),
				row['transaction_datetime'],
				row['transaction_type'],
				float(row['transaction_amount']),
				row['transaction_status'],
				float(row['balance_after_transaction']),
				row['channel'],
				float(row['fee_applied'])
			)
		)
	conn.commit()
	conn.close()
	os.remove(csv_path)
