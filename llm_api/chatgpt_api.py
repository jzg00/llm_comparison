# functions to send prompts/tasks to chatgpt
import os
from dotenv import load_dotenv
from openai import OpenAI
import json

load_dotenv()

client = OpenAI() # api_key=os.environ.get("OPENAI_API_KEY") is default parameter
