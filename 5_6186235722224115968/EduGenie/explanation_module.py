import os

try:
    from transformers import pipeline
except ImportError:
    pipeline = None


_local_explainer = None


def _get_local_explainer():
    global _local_explainer

    if _local_explainer is not None:
        return _local_explainer

    if pipeline is None:
        return None

    model_name = os.getenv(
        "LOCAL_EXPLANATION_MODEL",
        "MBZUAI/LaMini-Flan-T5-783M",
    )

    _local_explainer = pipeline(
        "text2text-generation",
        model=model_name,
        device=-1,
    )
    return _local_explainer


def explain_concept(topic: str) -> str:
    """
    Primary implementation follows the project document's local
    LaMini-Flan-T5 concept-explanation approach.

    If transformers/model loading is unavailable, fall back to Gemini
    so the rest of the application remains usable.
    """
    prompt = (
        "Explain this educational topic in simple language for a beginner. "
        "Give a short definition, key points, and one simple example.\n\n"
        f"Topic: {topic}"
    )

    try:
        explainer = _get_local_explainer()
        if explainer is not None:
            result = explainer(
                prompt,
                max_new_tokens=180,
                do_sample=False,
            )
            if result and result[0].get("generated_text"):
                return result[0]["generated_text"].strip()
    except Exception:
        pass

    from gemini_client import generate_text
    return generate_text(
        f"""
Explain the following topic to a beginner using simple language.
Include:
1. Meaning
2. Key points
3. One easy example

Topic: {topic}
"""
    )
