from gemini_client import generate_text


def answer_question(question: str) -> str:
    prompt = f"""
You are EduGenie, an educational AI assistant.

Answer the student's question accurately and clearly.
Use simple language where possible.
If the question is academic, include a short example when useful.
Do not invent facts.

Student question:
{question}
"""
    return generate_text(prompt)
