import os
from dotenv import load_dotenv

load_dotenv()

COLUMNS_FILE = str(os.getenv("COLUMNS_FILE"))
BUSINESS_LOGIC_FILE = str(os.getenv("BUSINESS_LOGIC_FILE"))

class DocRetriever:
    def __init__(self):
        self.columns_guide = self.get_columns_guide()
        self.business_logic = self.get_business_logic()

    def get_columns_guide(self):
        try:
            with open(COLUMNS_FILE, "r", encoding="utf-8") as f:
                return f.read()
        except FileNotFoundError:
            raise FileNotFoundError("Columns guide not found.")

    def get_business_logic(self):
        try:
            with open(BUSINESS_LOGIC_FILE, "r", encoding="utf-8") as f:
                return f.read()
        except FileNotFoundError:
            raise FileNotFoundError("Business logic not found.")

