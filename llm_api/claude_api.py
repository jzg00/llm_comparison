import os
from dotenv import load_dotenv
from anthropic import Anthropic
import json

load_dotenv()

client = Anthropic() # api_key=os.environ.get("ANTHROPIC_API_KEY") is default

def call_claude():
    pass

def save_claude():
    pass