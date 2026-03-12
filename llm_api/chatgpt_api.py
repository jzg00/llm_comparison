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
        {"role": "developer", "content": "You are a helpful assistant. Respond with raw Python code only. No markdown, no explanations."},
        {"role": "user", "content": prompt}
    ]
    # temperature control not supported for this model
)
    return completion.choices[0].message.content


def save_chatgpt(task_id: str, response: dict, run_number: int = 1):

    os.makedirs("data/raw/chatgpt", exist_ok=True)

    filename = f"data/raw/chatgpt/{task_id}_run{run_number}.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(response, f, indent=2)

    print(f"response saved to {filename}")


# quick test
if __name__ == "__main__":
    example_prompt = "Say hello"
    task_id = "example"
    response = call_chatgpt(example_prompt)
    print(response)
    save_chatgpt(task_id, response)