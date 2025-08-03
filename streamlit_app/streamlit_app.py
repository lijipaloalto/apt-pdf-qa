# streamlit_app.py

import streamlit as st
import requests

st.title("PDF Q&A Tool")

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")
question = st.text_input("Ask a question")

if uploaded_file and st.button("Upload PDF"):
    files = {"file": uploaded_file.getvalue()}
    res = requests.post("http://localhost:8000/upload/", files=files)
    st.success(res.json().get("message"))

if question and st.button("Ask a question"):
    res = requests.post("http://localhost:8000/ask/", data={"question": question})
    st.write("💬 Answer:", res.json().get("answer"))

