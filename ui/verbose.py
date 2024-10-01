from langchain_google_genai import GoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv
import os

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

model = GoogleGenerativeAI(model="gemini-pro")
question_parser = [
    SystemMessage(content="""Given the context of required information for a survey questionary provide a user interactive question to post in the form.
                  Adhere to following protocol for forming question: Do not repeat same questions. No more than 40 words. Should be easy to understand."""),
    HumanMessage(content="Need a rating between 1 to 5 to understand users eating habit on Fruits and Vegetable."),
]

print(model.invoke(question_parser))