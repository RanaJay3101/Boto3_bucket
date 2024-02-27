import logging
import boto3
from botocore.exceptions import ClientError
import os


def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
        print("Done bro")
    except ClientError as e:
        logging.error(e)
        return False
    return True

def list_files():
    """List files in an S3 bucket

    :param bucket_name: Name of the S3 bucket
    :return: List of files in the bucket. If error, return None
    """

    # Retrieve the list of bucket objects
    bucket_name='rj-bucket-trial3'
    s3_client = boto3.client('s3')
    try:
        response = s3_client.list_objects_v2(Bucket=bucket_name)
    except ClientError as e:
        logging.error(e)
        return None
    
    if 'Contents' in response:
        files = [obj['Key'] for obj in response['Contents']]
        if files is not None:
            print("Files in bucket:")
            for file in files:
                print(file)
    else:
        print(f"No files found in bucket '{bucket_name}'")
        return []



if __name__ == "__main__":
    print("Opetions")
    print("1. Upload file")
    print("2. List files")

    option = int(input("Enter option: "))
    if option == 1:
        file_name = input("Enter file name: ")
        bucket = input("Enter bucket name: ")
        upload_file(file_name, bucket)

    elif option == 2:
        list_files()
        
    else:
        print("Invalid option")