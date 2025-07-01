# 💬 Sentiment Analysis with Hugging Face Transformers

This notebook demonstrates how to use a pre-trained transformer model from Hugging Face to perform sentiment analysis on text data.

## 🤖 What It Does

- Loads a transformer model (e.g., `distilbert-base-uncased-finetuned-sst-2-english`)
- Analyzes the sentiment of input text (positive / negative)
- Accepts batch or single-text inference
- Returns confidence scores for predictions

## 📁 Files

- `Sentimental_Analysis.ipynb`: Core notebook for performing sentiment analysis using Hugging Face Transformers.

## 🛠 Technologies Used

- Python
- Jupyter Notebook
- Hugging Face Transformers
- Datasets
- PyTorch (backend)

## ▶️ How to Run

1. Install dependencies:

```bash
pip install transformers datasets torch
