# s3에 버킷에 저장된 파일 가져오는 코드

import json
import boto3
import botocore


BUCKET_NAME = 'lchy-public'
KEY = 'check.txt'

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    data = s3_client.get_object(Bucket=BUCKET_NAME, Key=KEY)
    content = data['Body'].read()
    print(content)
    return {
        'statusCode': 200,
        'body': json.dumps(content.decode('UTF-8'))
    }
