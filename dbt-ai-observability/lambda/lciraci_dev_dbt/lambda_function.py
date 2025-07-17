import json
import urllib.request
import urllib.error

def lambda_handler(event, context):
    try:
        # Extract token, account_id, and job_id from event
        dbt_token = event.get("dbt_token")
        account_id = event.get("account_id")
        job_id = event.get("job_id")

        if not dbt_token or not account_id or not job_id:
            return {
                "statusCode": 400,
                "error": "Missing one or more required fields: 'dbt_token', 'account_id', 'job_id'"
            }

        run_url = f"https://xxxxxxxx.dbt.com/api/v2/accounts/{account_id}/jobs/{job_id}/run/"
        headers = {
            "Authorization": f"Token {dbt_token}",
            "Content-Type": "application/json"
        }

        payload = {"cause": "Triggered from AWS Lambda"}
        data = json.dumps(payload).encode("utf-8")

        req = urllib.request.Request(run_url, data=data, headers=headers, method="POST")
        with urllib.request.urlopen(req) as response:
            response_body = json.loads(response.read().decode("utf-8"))

        run_id = response_body["data"]["id"]
        return {
            "statusCode": 200,
            "body": json.dumps({"run_id": run_id})
        }

    except urllib.error.HTTPError as e:
        error_msg = e.read().decode()
        return {
            "statusCode": e.code,
            "error": f"HTTP Error: {e.reason}",
            "response": error_msg
        }

    except Exception as ex:
        return {
            "statusCode": 500,
            "error": str(ex)
        }
