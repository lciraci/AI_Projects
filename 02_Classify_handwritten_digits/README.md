# 🧠 Vector Database RAG Demo

This project demonstrates a simple Retrieval-Augmented Generation (RAG) pipeline using vector databases to retrieve and answer questions from custom documents like PDFs.

## 🚀 What It Does

- Loads a PDF document.
- Splits it into meaningful text chunks.
- Converts chunks into vector embeddings using `sentence-transformers`.
- Stores vectors in a FAISS index (in-memory vector database).
- Enables querying: relevant document chunks are retrieved based on the input question.
- Passes the retrieved content to an LLM (e.g. Falcon or OpenAI) for answer generation.

## 🛠 Technologies Used

- Python
- Jupyter Notebook
- FAISS
- SentenceTransformers (`all-MiniLM-L6-v2`)
- PyMuPDF (`fitz`) for PDF parsing
- Langchain (for chaining embedding + retrieval)
- HuggingFace Transformers (or OpenAI via Langchain)

## 📁 Files

- `Vector_Database.ipynb`: Core demo with text-based input.
- `Vector_Database_PDF.ipynb`: RAG pipeline applied to a PDF document.

## 📦 Installation

Create a virtual environment and install the required libraries:

```bash
pip install faiss-cpu sentence-transformers pymupdf langchain
