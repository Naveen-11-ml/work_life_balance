from langchain_aws.chat_models import ChatBedrock
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import json
import os
from work_life_balance.config import *

load_dotenv()

model = ChatBedrock(model_id=os.getenv("AWS_BEDROCK_MODEL_ID"),
                    model_kwargs={"temperature":0.78, "top_p":0.9, "max_gen_len":100},
                    region_name=os.getenv("AWS_REGION"))

question_prompt = """Given the context of required information for a survey questionary provide a user interactive question to post in the form.
Adhere to following protocol for forming question: Do not repeat same questions. No more than 40 words. Should be easy to understand."""

parser = StrOutputParser()

question_template = ChatPromptTemplate.from_messages(
    [("system", question_prompt), ("user", "{text}")]
)

question = question_template | model | parser

def get_question(text):
    response = question.invoke({"text": text})
    return response

with open(f"{UI_PATH}/form.json", "r") as file:
    question_json = json.load(file)

for var, ques in question_json.items():
    print(f"{var}:  {get_question(ques)}")