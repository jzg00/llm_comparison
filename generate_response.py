from llm_api.chatgpt_api import call_chatgpt, save_chatgpt
import json

# load tasks
with open("tasks/tasks.json", "r", encoding="utf-8") as f:
    tasks = json.load(f)

# prompt LLMs with each task and save their raw response
for task in tasks:
    task_id = task["task_id"]
    prompt = task["prompt"]
    # extract code

    chatgpt_resp = call_chatgpt(prompt)
    save_chatgpt(task_id, chatgpt_resp) # responses are wrapped in markdown fences. need to extract / clean raw responses before linting, etc.