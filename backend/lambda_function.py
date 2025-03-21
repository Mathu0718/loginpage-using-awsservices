import json
import boto3
from datetime import datetime

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("AttendanceRecords")

def lambda_handler(event, context):
    try:
        # Handle CORS preflight request
        if event.get("httpMethod") == "OPTIONS":
            return {
                "statusCode": 200,
                "headers": {
                    "Access-Control-Allow-Origin": "*",
                    "Access-Control-Allow-Methods": "POST, OPTIONS",
                    "Access-Control-Allow-Headers": "Content-Type"
                },
                "body": json.dumps({"message": "CORS preflight response"})
            }

        # Parse request body
        body = json.loads(event["body"])
        action = body.get("action")
        email = body.get("email")

        if not email or action not in ["login", "logout"]:
            return {
                "statusCode": 400,
                "headers": {"Access-Control-Allow-Origin": "*"},
                "body": json.dumps({"message": "Invalid request. Email and action are required."})
            }

        timestamp = str(datetime.utcnow())

        # Update or create a new record
        response = table.update_item(
            Key={"email": email},
            UpdateExpression="""
                SET #s = :new_status,
                    timestamps = list_append(if_not_exists(timestamps, :empty_list), :new_timestamp)
            """,
            ExpressionAttributeNames={"#s": "status"},
            ExpressionAttributeValues={
                ":new_status": action,
                ":new_timestamp": [{"status": action, "timestamp": timestamp}],
                ":empty_list": []
            },
            ReturnValues="UPDATED_NEW"
        )

        return {
            "statusCode": 200,
            "headers": {"Access-Control-Allow-Origin": "*"},
            "body": json.dumps({
                "message": f"{action.capitalize()} successful!",
                "updated_status": response["Attributes"]["status"],
                "updated_timestamps": response["Attributes"]["timestamps"]
            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {"Access-Control-Allow-Origin": "*"},
            "body": json.dumps({"message": "Internal Server Error", "error": str(e)})
        }
