from utils.preprocessing import prepare_data
from db.seed_db import seed_db, DB_PATH
import os

CSV_FILE = "D:/Projects/data-analyst-agent/data/bank_client.csv"

if __name__ == "__main__":
    if not os.path.exists(DB_PATH):
        processed_file_path = prepare_data(CSV_FILE)
        seed_db(processed_file_path)
