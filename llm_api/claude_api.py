import os
from dotenv import load_dotenv
import anthropic
import json

load_dotenv()

client = anthropic.Anthropic() # api_key=os.environ.get("ANTHROPIC_API_KEY") is default

def call_claude(prompt: str, model: str = 'claude-sonnet-4-6') -> dict:

    message = client.messages.create(
        model = model,
        max_tokens=4096,
        system="You are a helpful assistant. Do not use markdown. Do not wrap code in triple backticks. Return only raw Python code with no formatting, no preamble, and no explanation.",
        messages =[
            {"role": "user", "content": prompt}
        ]
    )
    return message

def save_claude(task_id: str, prompt: str, message: anthropic.types.Message, run_number: int = 1):
 
    os.makedirs("data/raw/claude", exist_ok=True)
 
    data = {
        "task_id": task_id,
        "model": message.model,
        "run_number": run_number,
        "prompt": prompt,
        "response": message.content[0].text
    }
 
    filename = f"data/raw/claude/{task_id}_run{run_number}.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
 
    print(f"response saved to {filename}")
 
 
# quick test
if __name__ == "__main__":
    example_prompt = "Say hello"
    task_id = "example"
    response = call_claude(example_prompt)
    save_claude(task_id, example_prompt, response)