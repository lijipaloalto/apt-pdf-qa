# app/llm_client.py

from transformers import pipeline

class LLMClient:
    def __init__(self, model_name="distilbert-base-uncased"):
        self.qa_pipeline = pipeline("question-answering", model=model_name)

    def answer(self, question, context):
        return self.qa_pipeline(question=question, context=context)["answer"]


