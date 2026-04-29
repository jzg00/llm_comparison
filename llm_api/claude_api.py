from dotenv import load_dotenv
import anthropic
from config import RAW_DIR
from utils import get_logger, save_json

load_dotenv()

logger = get_logger(__name__)
client = anthropic.Anthropic()

_SYSTEM_PROMPT = (
    "You are a helpful assistant. Do not use markdown. "
    "Do not wrap code in triple backticks. "
    "Return only raw Python code with no formatting, no preamble, and no explanation."
)


def call_claude(prompt: str, model: str = "claude-sonnet-4-6") -> anthropic.types.Message:
    return client.messages.create(
        model=model,
        max_tokens=4096,
        system=_SYSTEM_PROMPT,
        messages=[{"role": "user", "content": prompt}],
    )


def save_claude(task_id: str, prompt: str, message: anthropic.types.Message, run_number: int = 1) -> None:
    data = {
        "task_id": task_id,
        "model": message.model,
        "run_number": run_number,
        "prompt": prompt,
        "response": message.content[0].text,
    }
    filepath = RAW_DIR / "claude" / f"{task_id}_run{run_number}.json"
    save_json(data, filepath)
    logger.info("Saved %s", filepath)
