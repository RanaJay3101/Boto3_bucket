import boto3

# Create an S3 client
s3_client = boto3.client('s3')
bucket_name = 'rj-bucket-trial3'

new_bucket_name = 'rj-bucket-trial2'

response = s3_client.put_bucket_tagging(
    Bucket=bucket_name,
    Tagging={
        'TagSet': [
            {
                'Key': 'Name',
                'Value': new_bucket_name
            },
        ]
    }
)