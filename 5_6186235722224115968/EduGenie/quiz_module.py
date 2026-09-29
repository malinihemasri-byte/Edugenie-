import json
import re
from typing import Any

from gemini_client import generate_text


def _clean_json_block(text: str) -> str:
    text = text.strip()
    text = re.sub(r"^```(?:json)?\s*", "", text, flags=re.IGNORECASE)
    text = re.sub(r"\s*```$", "", text)
    return text.strip()


def generate_quiz(passage: str) -> list[dict[str, Any]]:
    prompt = f"""
Create exactly 3 multiple-choice questions from the passage below.

Rules:
- Each question must have exactly 4 options.
- Exactly one option must be correct.
- Questions must test understanding of the passage.
- Keep wording clear for students.
- Return ONLY valid JSON.
- Do not use Markdown code fences.

Required JSON format:
[
  {{
    "question": "Question text",
    "options": ["A", "B", "C", "D"],
    "answer": "A"
  }}
]

Passage:
{passage}
"""
    raw = _clean_json_block(generate_text(prompt))

    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise ValueError(f"Could not parse quiz JSON: {exc}") from exc

    if not isinstance(data, list) or len(data) != 3:
        raise ValueError("Gemini did not return exactly 3 quiz questions.")

    for item in data:
        if not isinstance(item, dict):
            raise ValueError("Invalid quiz question format.")
        if not all(k in item for k in ("question", "options", "answer")):
            raise ValueError("Quiz question is missing required fields.")
        if len(item["options"]) != 4:
            raise ValueError("Each quiz question must have 4 options.")

    return data
