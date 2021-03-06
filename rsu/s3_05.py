# s3에 데이터 베이스 연결하기
# s3에 데이터 베이스 연결하기
import json
import boto3
import botocore
import os
import sys
import uuid
from urllib.parse import unquote_plus
import sqlite3


s3_client = boto3.client("s3")
s3_resocuce = boto3.resource('s3')

BUCKET_NAME = 'lchy-public'
KEY = 'lchy.db'

def lambda_handler(event, context):
    if event:
        print('Start!')
        conn = sqlite3.connect('/tmp/'+KEY)
        origin_path = '/tmp/'+KEY
        cur = conn.cursor()
        conn.close()
        tmpkey = KEY.replace('/', '')

        print('tmpkey: '+tmpkey)
        #download_path = '/tmp/{}{}'.format(uuid.uuid4(), tmpkey)
        #s3_client.download_file(BUCKET_NAME, origin_path , download_path)
        s3_client.upload_file( origin_path, BUCKET_NAME, "sub/move_lchy.db")
        # s3_client.upload_file(lambda_path, BUCKET_NAME, "sub/result.txt")

        return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
        }
