import boto3
import json
from urllib.parse import unquote_plus

# S3 + Bedrock clients
s3 = boto3.client('s3')
bedrock = boto3.client('bedrock-runtime')  # make sure Lambda has access to Bedrock

def lambda_handler(event, context):
    try:
        # Extract bucket and key from S3 event
        s3_info = event['Records'][0]['s3']
        bucket = s3_info['bucket']['name']
        key = unquote_plus(s3_info['object']['key'])

        print(f"📥 New file uploaded: s3://{bucket}/{key}")

        # Get the file content
        response = s3.get_object(Bucket=bucket, Key=key)
        job_data = json.loads(response['Body'].read().decode('utf-8'))

        # Check if job status is Error
        if job_data.get("status") != "Error":
            print("✅ Job was successful, no need to analyze.")
            return {
                "statusCode": 200,
                "body": json.dumps({"message": "No error detected, skipping analysis"})
            }

        # Build prompt for Bedrock
        prompt = f"""Human: A dbt job has failed. Here is the job metadata:\n\n{json.dumps(job_data, indent=2)}\n\n
        What is the likely cause of failure and how can a developer fix it?

        Assistant:"""


        print("🧠 Sending prompt to Bedrock...")

        # Call Bedrock (Claude v2 example)
        bedrock_response = bedrock.invoke_model(
            modelId="anthropic.claude-v2",
            contentType="application/json",
            accept="application/json",
            body=json.dumps({
                "prompt": prompt,
                "max_tokens_to_sample": 300,
                "temperature": 0.2,
                "stop_sequences": ["\n\n"]
            })
        )

        response_body = json.loads(bedrock_response['body'].read().decode('utf-8'))
        explanation = response_body.get("completion", "").strip()

        print(f"📄 Explanation: {explanation}")

        # Prepare output key
        output_key = key.replace("dbt_runs/", "dbt_analysis/")

        # Write AI output to S3
        s3.put_object(
            Bucket=bucket,
            Key=output_key,
            Body=json.dumps({
                "run_id": job_data.get("run_id"),
                "job_id": job_data.get("job_id"),
                "status": "Error",
                "ai_analysis": explanation
            }),
            ContentType="application/json"
        )

        print(f"📤 Saved analysis to: s3://{bucket}/{output_key}")

        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Analysis saved"})
        }

    except Exception as e:
        print(f"❌ Error in Lambda: {str(e)}")
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
