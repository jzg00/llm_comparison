import json
from config import TASKS_FILE, RAW_DIR
from utils import get_logger
from llm_api.chatgpt_api import call_chatgpt, save_chatgpt
from llm_api.claude_api import call_claude, save_claude

logger = get_logger(__name__)

RUN_NUMBER = 1


def generate_response():
    with open(TASKS_FILE, "r", encoding="utf-8") as f:
        tasks = json.load(f)

    for task in tasks:
        task_id = task["task_id"]
        prompt = task["prompt"]

        for model_name, call_fn, save_fn in [
            ("chatgpt", call_chatgpt, save_chatgpt),
            ("claude", call_claude, save_claude),
        ]:
            output_path = RAW_DIR / model_name / f"{task_id}_run{RUN_NUMBER}.json"
            if output_path.exists():
                logger.info("Skipping %s/%s — raw response already exists", model_name, task_id)
                continue

            logger.info("Querying %s for task: %s", model_name, task_id)
            response = call_fn(prompt)
            save_fn(task_id, prompt, response, run_number=RUN_NUMBER)


if __name__ == "__main__":
    generate_response()
