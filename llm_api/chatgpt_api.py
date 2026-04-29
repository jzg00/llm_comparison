from dotenv import load_dotenv
from openai import OpenAI
from config import RAW_DIR
from utils import get_logger, save_json

load_dotenv()

logger = get_logger(__name__)
client = OpenAI()

_SYSTEM_PROMPT = (
    "You are a helpful assistant. Do not use markdown. "
    "Do not wrap code in triple backticks. "
    "Return only raw Python code with no formatting, no preamble, and no explanation."
)


def call_chatgpt(prompt: str, model: str = "gpt-5.3-chat-latest") -> object:
    return client.chat.completions.create(
        model=model,
        max_completion_tokens=4096,
        messages=[
            {"role": "developer", "content": _SYSTEM_PROMPT},
            {"role": "user", "content": prompt},
        ],
    )


def save_chatgpt(task_id: str, prompt: str, completion, run_number: int = 1) -> None:
    data = {
        "task_id": task_id,
        "model": completion.model,
        "run_number": run_number,
        "prompt": prompt,
        "response": completion.choices[0].message.content,
    }
    filepath = RAW_DIR / "chatgpt" / f"{task_id}_run{run_number}.json"
    save_json(data, filepath)
    logger.info("Saved %s", filepath)
