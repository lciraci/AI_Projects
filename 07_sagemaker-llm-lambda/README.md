# 🧠 Multi-Class News Classification with DistilBERT on AWS SageMaker + Lambda

This project builds and deploys a **DistilBERT-based text classification model** that predicts the category of a news headline. It covers the full ML pipeline from data preprocessing and training on AWS SageMaker to serving real-time predictions via AWS Lambda.

---

## 📁 Files Overview

| File | Description |
|------|-------------|
| `EDA_MultiClassTextClassification.ipynb` | Exploratory data analysis: class distribution, text length analysis, and dataset structure visualization. |
| `script.py` | SageMaker-compatible training script using `DistilBERT`. Trains a multi-class classifier and saves the model to `SM_MODEL_DIR`. |
| `aws-lambda-llm-endpoint-invoke-function.py` | AWS Lambda handler that invokes the deployed SageMaker endpoint using Boto3. Parses a JSON payload with the input headline and returns the model's prediction. |

---

## 🧾 Dataset Description

The dataset contains news article metadata and is read from a tab-separated file. We only use:

- `TITLE`: The news headline (text input)
- `CATEGORY`: The label, mapped as:
  - `b` → **Business**
  - `e` → **Entertainment**
  - `m` → **Health**
  - `t` → **Science**

---

## 🏗️ Model Architecture

- **Backbone**: `DistilBERT` (`distilbert-base-uncased`)
- **Classifier**: Fully connected layer with 4-class softmax output
- **Loss**: CrossEntropyLoss
- **Optimizer**: Adam (learning rate = `1e-5`)
- **Max Seq Length**: 512

---

## 🔧 Training Setup

- Run `script.py` as an entry point for a SageMaker training job
- Loads CSV from S3 (`s3_path` in code)
- Splits data 80/20 into train/test
- Trains for 2+ epochs
- Saves model weights and tokenizer vocab to `SM_MODEL_DIR`

Output:
- `pytorch_distilbert_news.bin`
- `vocab_distilbert_news.bin`

---

## 🚀 Deployment via AWS Lambda

The Lambda function `aws-lambda-llm-endpoint-invoke-function.py`:

- Accepts a JSON `POST` payload:
  ```json
  {
    "query": {
      "headline": "New cancer vaccine shows promising results"
    }
  }
  
---

## ✨ Author

Lucio Ciracì – Building real AI projects, one repo at a time 🇮🇹🇺🇸  
🔗 [LinkedIn](https://www.linkedin.com/in/lucio-ciraci94c) | [GitHub](https://github.com/lciraci)
