import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()

DB_PATH = str(os.getenv("DB_PATH"))

class SQLExecutor:
    def __init__(self):
        self.connection = sqlite3.connect(DB_PATH)
        self.cursor = self.connection.cursor()

    def execute(self, query):
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        self.connection.commit()

        return rows