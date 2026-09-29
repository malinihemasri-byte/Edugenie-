from gemini_client import generate_text


def summarize_text(text: str) -> str:
    prompt = f"""
Summarize the educational passage below for quick revision.

Requirements:
- Preserve the important information.
- Remove repetition and unnecessary detail.
- Use concise, student-friendly language.
- Prefer short paragraphs or bullet points.
- Do not add information that is not in the passage.

Passage:
{text}
"""
    return generate_text(prompt)
