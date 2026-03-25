from llm_api.chatgpt_api import call_chatgpt, save_chatgpt
from llm_api.claude_api import call_claude, save_claude
import json

def generate_response():
    # load tasks
    with open("tasks/tasks.json", "r", encoding="utf-8") as f:
        tasks = json.load(f)

    # prompt LLMs with each task and save their raw response
    for task in tasks:
        task_id = task["task_id"]
        prompt = task["prompt"]

        chatgpt_resp = call_chatgpt(prompt)
        save_chatgpt(task_id, prompt, chatgpt_resp)
        
        claude_resp = call_claude(prompt)
        save_claude(task_id, prompt, claude_resp)

if __name__=="__main__":
    generate_response()