# tests/test_llm_client.py

from app.llm_client import LLMClient

def test_answer():
    llm = LLMClient(model_name="distilbert-base-uncased-distilled-squad")
    context = "Paris is the capital of France."
    question = "What is the capital of France?"

    answer = llm.answer(question, context)
    assert "Paris" in answer
