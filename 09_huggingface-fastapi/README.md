# Hugging Face + FastAPI + GitHub CI/CD

This project deploys a Hugging Face model behind a FastAPI endpoint, packaged in Docker and built via GitHub Actions.

## Run locally

```bash
docker build -t huggingface-fastapi .
docker run -p 8000:8000 huggingface-fastapi