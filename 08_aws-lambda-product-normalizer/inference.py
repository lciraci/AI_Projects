import boto3
import json

bedrock = boto3.client("bedrock-runtime")
#sets up the connection to send prompts to LLMs hosted on Amazon Bedrock.

def lambda_handler(event, context):
    try:
        if "body" in event and isinstance(event["body"], str):
            body = json.loads(event["body"])
        else:
            body = event

        raw_text = body.get("product", "").strip()

        if not raw_text:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Missing 'product' in input."})
            }

        # Correct payload format for Claude 3 (Messages API)
        request_body = {
            "anthropic_version": "bedrock-2023-05-31",
            "messages": [
                {
                    "role": "user",
                    "content": f"Normalize this product name to a clean, human-readable format:\n\"{raw_text}\"\nRespond with just the normalized version, no explanation."
                }
            ],
            "max_tokens": 200,
            "temperature": 0.2
        }
        #This builds the exact instruction that gets sent to Claude 3 Haiku — in the right format — and tells it to return a clean, normalized product name.

        response = bedrock.invoke_model(
            modelId="anthropic.claude-3-haiku-20240307-v1:0",
            body=json.dumps(request_body),
            contentType="application/json",
            accept="application/json"
        )

        result = json.loads(response["body"].read())
        normalized = result["content"][0]["text"].strip()

        return {
            "statusCode": 200,
            "body": json.dumps({"normalized": normalized})
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }