# 🔍 AI-Powered Q&A Bot with Vector Search (RAG)

This project demonstrates how to build a Retrieval-Augmented Generation (RAG) system using vector databases and open-source language models — no OpenAI required. It includes document chunking, embedding with `sentence-transformers`, similarity search using `FAISS`, and response generation using Hugging Face models.

## 📁 Notebooks

| Notebook                | Description |
|-------------------------|-------------|
| `Vector_Database.ipynb` | Basic FAISS setup with sentence embedding and text query testing. |
| `Vector_Database_PDF.ipynb` | Loads and processes PDF files, then builds a FAISS vector store for search. |
| `rag_qa_bot.ipynb`      | Full end-to-end open-source RAG pipeline — PDF loading, FAISS search, and answering questions using Hugging Face LLMs. |

## 🛠 Tech Stack

- Python
- `sentence-transformers`
- `faiss-cpu`
- `PyMuPDF` (PDF reading)
- `transformers` by Hugging Face
- Jupyter Notebook

## 🚀 Features

- PDF to vector embedding using `all-MiniLM-L6-v2`
- Chunked text retrieval using FAISS
- Question answering using local or Hugging Face-hosted models (e.g. `falcon-7b-instruct`, `mistralai/Mistral-7B`)
- 100% Open Source — no OpenAI API required

## 📦 Installation

```bash
pip install sentence-transformers faiss-cpu pymupdf transformers accelerate
