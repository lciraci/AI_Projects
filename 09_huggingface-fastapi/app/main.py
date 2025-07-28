from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

# Load a pretrained Hugging Face pipeline (sentiment analysis)
classifier = pipeline("sentiment-analysis")

class InputText(BaseModel):
    text: str

@app.post("/predict")
def predict(input: InputText):
    result = classifier(input.text)
    return {"result": result}