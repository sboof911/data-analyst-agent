from .tools.sql_executor import SQLExecutor
from .tools.doc_retriever import DocRetriever
from agents.memory.conversation_memory import ConversationMemory
import os
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

HUGGINGFACEHUB_API_TOKEN = str(os.getenv("HUGGINGFACEHUB_API_TOKEN"))
SQLPROMPT_PATH = str(os.getenv("SQLPROMPT_PATH"))
CLIENTPROMPT_PATH = str(os.getenv("CLIENTPROMPT_PATH"))

class Agent:
    def __init__(self, llm_model="meta-llama/Llama-3.1-8B-Instruct:fireworks-ai"):
        self.sql_executor = SQLExecutor()
        self.doc_retriever = DocRetriever()
        self.memory = ConversationMemory()
        self.llm_model = llm_model
        self.model = OpenAI(
            base_url="https://router.huggingface.co/v1",
            api_key=HUGGINGFACEHUB_API_TOKEN)

    def get_sql_query(self, user_input):
        prompt = None
        try:
            with open(SQLPROMPT_PATH, "r", encoding="utf-8") as f:
                prompt = f.read()
        except FileNotFoundError:
            raise FileNotFoundError("SQL prompt file not found.")
        prompt = prompt.format(
            columns_guide=self.doc_retriever.get_columns_guide(),
            business_logic=self.doc_retriever.get_business_logic(),
            user_input=user_input
        )

        return prompt

    def get_user_response_prompt(self, rows, user_input):
        prompt = None
        try:
            with open(CLIENTPROMPT_PATH, "r", encoding="utf-8") as f:
                prompt = f.read()
        except FileNotFoundError:
            raise FileNotFoundError("Client prompt file not found.")
        prompt = prompt.format(
            results=rows,
            user_input=user_input
        )

        return prompt

    def ask(self, user_input : str):
        sql_answer = self.model.chat.completions.create(
            model=self.llm_model,
            messages=[
                {
                    "role": "user",
                    "content": self.get_sql_query(user_input)
                }
            ],
        )
        
        query = sql_answer.choices[0].message.content
        rows = self.sql_executor.execute(query)

        user_response = self.model.chat.completions.create(
            model=self.llm_model,
            messages=[
                {
                    "role": "user",
                    "content": self.get_user_response_prompt(rows, user_input)
                }
            ],
        )

        self.memory.add(user_input, user_response.choices[0].message.content)

        return user_response.choices[0].message.content

    def set_sql_executor(self, sql_executor : SQLExecutor):
        self.sql_executor = sql_executor

    def set_doc_retriever(self, doc_retriever : DocRetriever):
        self.doc_retriever = doc_retriever

    def delete(self):
        self.sql_executor.connection.close()
        self.sql_executor = None
        self.doc_retriever = None
        self.conversation_memory = None
