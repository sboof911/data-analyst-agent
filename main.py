import os
from utils.preprocessing import prepare_data
from db.seed_db import seed_db, DB_PATH
from agents import Agent
from dotenv import load_dotenv

load_dotenv()

CSV_FILE = str(os.getenv("CSV_FILE"))

if __name__ == "__main__":
    if not os.path.exists(DB_PATH):
        processed_file_path = prepare_data(CSV_FILE)
        seed_db(processed_file_path)

    agent = Agent()
    # Use the agent for further processing
    answer = agent.ask("I want yesterday's transactions.")
    print(answer)
    agent.delete()
