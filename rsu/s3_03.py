# 코드로 파일 올리기

import json
import boto3

s3_client = boto3.client("s3")

BUCKET_NAME = 'lchy-public'
KEY = 'check.txt'

def lambda_handler(event, context):

    print("I'm triggered !!")

    if event:
        data = s3_client.get_object(Bucket=BUCKET_NAME, Key=KEY)
        
        file_content = data["Body"].read().decode("utf-8")
        print("File content : ", file_content)
        
        lambda_path = "/tmp/1.txt"

        with open(lambda_path, 'w+') as file:
            file.write(file_content+" ...YOLO!")
            file.close()
        
        s3_client.upload_file(lambda_path, BUCKET_NAME, "sub/result.txt") # 자동적으로 sub에 파일이 생기는 것
        
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }