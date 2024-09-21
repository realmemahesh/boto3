import boto3
import json

# Initialize the S3 client
s3 = boto3.client("s3")

def lambda_handler(event, context):
    # List all S3 buckets
    response = s3.list_buckets()
 
    # Extract bucket names with list comprehension
    bucket_list = [bucket['Name'] for bucket in response['Buckets']]

    # Print bucket names for logging/debugging
    print("Buckets:", bucket_list)

    # Return the bucket names in the response
    return {
        "statusCode": 200,
        "body": json.dumps(bucket_list)  # Include bucket list in response
    }
