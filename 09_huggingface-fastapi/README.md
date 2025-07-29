# 🤖 Hugging Face + FastAPI + GitHub CI/CD

This project deploys a Hugging Face sentiment analysis model (`distilbert-base-uncased-finetuned-sst-2-english`) behind a FastAPI endpoint. It's containerized with Docker and automatically built and published via GitHub Actions.

👉 **Docker Hub**: [lucio94c/huggingface-fastapi](https://hub.docker.com/r/lucio94c/huggingface-fastapi)

---

## 📁 Project Structure

| File                      | Purpose                                                                 |
|---------------------------|-------------------------------------------------------------------------|
| `main.py`                 | FastAPI app that loads the Hugging Face pipeline and defines the `/predict` endpoint |
| `requirements.txt`        | Project dependencies: `fastapi`, `uvicorn`, `transformers`, `torch`     |
| `Dockerfile`              | Docker setup for packaging and running the FastAPI app                 |
| `.github/workflows/deploy.yml` | GitHub Actions workflow for building and pushing the Docker image to Docker Hub |

---

## 🚀 Run Locally with Docker

```bash
docker pull lucio94c/huggingface-fastapi
docker run --platform linux/amd64 -p 8000:8000 lucio94c/huggingface-fastapi
