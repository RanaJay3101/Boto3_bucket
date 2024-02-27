""" 
              created by Rana Jay
"""

import boto3
import os

s3_client = boto3.client('s3')

bucket_name = 'rj-bucket-trial3'
response = s3_client.create_bucket(Bucket=bucket_name)
print(response)



























