import json

def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from CDK 2.0 and CDK Pipelines!'')
    }

