import boto3
import json

# Prompt template defined inline
PRODUCT_NORMALIZER_PROMPT = """
Human: Normalize this product name to a clean, human-readable format:
"{product_description}"

Respond with just the normalized version, no explanation.
Assistant:
"""

# Create Bedrock client
bedrock = boto3.client("bedrock-runtime")

def lambda_handler(event, context):
    try:
        # Accept both test event or API Gateway body
        if "body" in event and isinstance(event["body"], str):
            body = json.loads(event["body"])
        else:
            body = event

        raw_text = body.get("text", "").strip()

        if not raw_text:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Missing 'text' in input."})
            }

        # Format prompt
        prompt = PRODUCT_NORMALIZER_PROMPT.format(product_description=raw_text)

        # Call Bedrock Claude model
        response = bedrock.invoke_model(
            modelId="anthropic.claude-3-sonnet-20240229-v1:0",
            body=json.dumps({
                "prompt": prompt,
                "max_tokens": 200,
                "temperature": 0.2
            }),
            contentType="application/json",
            accept="application/json"
        )

        output = json.loads(response["body"].read())
        normalized = output["completion"].strip()

        return {
            "statusCode": 200,
            "body": json.dumps({"normalized": normalized})
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
