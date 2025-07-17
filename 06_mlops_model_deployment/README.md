# 🚀 FastAPI Projects - `summarizer_and_student_api`

This folder contains two FastAPI projects:

1. **Text Summarization API** (built and deployed in Google Colab using `ngrok`)
2. **Student API** (CRUD app running locally with in-memory data)

---

## 📚 Description

- `API_serving_text_summarization_model.ipynb` contains a summarization model deployed as an API using Hugging Face's `facebook/bart-large-cnn` model and FastAPI inside Google Colab.
- `myapi.py` defines a classic student API that supports CRUD operations using FastAPI and Pydantic.

---

## 🛠️ Techniques

- FastAPI for backend development  
- Hugging Face Transformers for text summarization  
- Pyngrok to expose the Colab API to the web  
- Uvicorn to serve locally  
- Pydantic for input validation  
- Swagger UI for interactive docs (`/docs`)

---

## 🔗 Summarization API (Colab)

- `POST /summarize` — Summarizes a long text  
  Example payload:
  ```json
  {
    "text": "Artificial Intelligence is transforming industries, from healthcare to finance, with its ability to learn and adapt."
  }
