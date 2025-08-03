## create virtual environment
python3.11 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# run backend
uvicorn app.main:app --reload

# run frontend
streamlit run streamlit_app.py

## Run Program 
# 1. Activate env
source .venv/bin/activate

# 2. Start FastAPI backend
uvicorn app.main:app --reload

# 3. Start Streamlit frontend
streamlit run streamlit_app.py


# run test
pytest tests

## TODO
# future scaling
# 1. app/routes/ to modularize FastAPI endpoints
# 2. Add SQLite or Postgres if you want to persist PDF metadata
# 3. Switch from transformers pipeline to vLLM, Ollama, or LangChain for RAG enhancements
