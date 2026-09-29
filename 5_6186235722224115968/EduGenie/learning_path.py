from gemini_client import generate_text


def get_learning_recommendations(topic: str) -> str:
    prompt = f"""
Create a structured learning path for: {topic}

Organize it from beginner to advanced.
Include:
- Prerequisites
- Beginner topics
- Intermediate topics
- Advanced topics
- Suggested practice/projects
- Useful resource types such as videos, articles, books or documentation
- A realistic sequence for learning

Keep it practical and easy to follow.
"""
    return generate_text(prompt)
