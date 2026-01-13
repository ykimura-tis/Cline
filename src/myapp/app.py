import boto3
from common.config import load_config

s3_client = boto3.client("s3")


def lambda_handler(event, context):
    config = load_config(s3_client)
    return {
        "statusCode": 200,
        "db_host": config["DB_HOST"]
    }
