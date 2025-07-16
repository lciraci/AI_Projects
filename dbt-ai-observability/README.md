# dbt AI Observability with AWS Lambda & Bedrock

This repo demonstrates how to monitor and analyze dbt Cloud job errors using AWS services like Lambda, S3, and Bedrock (Claude v2).

## 🧩 Components

| Component                        | Description |
|----------------------------------|-------------|
| `lciraci_dev_dbt`                | Triggers dbt job via API |
| `lciraci_dev_webhook_listener_dbt` | Handles webhook, logs result, saves to S3 |
| `lciraci_dbt_error_analyzer`    | Triggered by S3 → analyzes error via Bedrock |
| `S3://lciraci-dev/dbt_runs/`    | Stores job result JSONs |
| `S3://lciraci-dev/dbt_analysis/`| Stores AI-generated explanations |

## ✅ Flow Overview

1. **Trigger dbt Job**
2. **Webhook receives job status**
3. **Save result to S3**
4. **S3 triggers Lambda → Bedrock AI explanation**
5. **Save analysis in S3**

See `architecture/POC_Lambda_dbt_Bedrock_Analysis.pdf` for the full diagram.

## 🔐 IAM Permissions Required

- `s3:GetObject`, `s3:PutObject` on your S3 bucket
- `bedrock:InvokeModel` for `anthropic.claude-v2`

## 🧪 Testing Locally

Each Lambda has a `test_event.json` file under `/utils/` to simulate the payload.
Use the AWS Console or `sam local invoke` to run.

## 📦 Deployment

You can deploy using:
- Manual upload
- [Optional] Terraform or AWS SAM

## 📌 Author

Lucio Ciracì — 2025 AI Engineer Journey ✨
