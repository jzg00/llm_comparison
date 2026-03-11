import os
from dotenv import load_dotenv
from openai import OpenAI
import json

load_dotenv()

client = OpenAI() # api_key=os.environ.get("OPENAI_API_KEY") is default parameter



def call_chatgpt(prompt: str, model: str = 'gpt-5.3-chat-latest') -> dict:
    """
    Send task prompts to chatgpt and return raw responses as dict
    """
    completion = client.chat.completions.create(
    model = model,
    messages=[
        {"role": "developer", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ]
    # temperature control not supported for this model
)
    return completion.choices[0].message.content

# write function to save response in data/raw/chatgpt


# quick test
if __name__ == "__main__":
    example_prompt = "Say hello"
    task_id = "001"
    response = call_chatgpt(example_prompt)
    print(response)