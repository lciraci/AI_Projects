import json
import boto3
from datetime import datetime

s3 = boto3.client('s3')
bucket_name = 'lciraci-dev'

def lambda_handler(event, context):
    try:
        # Log raw event for debug
        print("🧾 Full event:")
        print(json.dumps(event))

        # Parse body safely
        body = json.loads(event["body"]) if isinstance(event["body"], str) else event["body"]

        # Log parsed body
        print("📦 Parsed body:")
        print(json.dumps(body))

        # Extract values from body["data"]
        data = body.get("data", {})

        run_id = data.get("runId")
        job_id = data.get("jobId")
        status_code = data.get("runStatusCode")

        status_map = {
            1: "Queued",
            2: "Starting",
            3: "Running",
            10: "Success",
            20: "Error",
            30: "Cancelled"
        }
        status = status_map.get(status_code, "Unknown")

        print(f"✅ dbt Run ID {run_id} (Job ID: {job_id}) finished with status: {status}")

        # Build the result object
        result = {
            "run_id": run_id,
            "job_id": job_id,
            "status": status,
            "timestamp": datetime.utcnow().isoformat()
        }

        # Define S3 key
        s3_key = f"dbt_runs/dbt_job_{run_id}.json"

        # Upload to S3
        s3.put_object(
            Bucket=bucket_name,
            Key=s3_key,
            Body=json.dumps(result),
            ContentType='application/json'
        )

        print(f"📤 Saved job result to S3: s3://{bucket_name}/{s3_key}")

        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Webhook received and saved to S3"})
        }

    except Exception as ex:
        print(f"❌ Error: {str(ex)}")
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(ex)})
        }
