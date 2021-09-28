import json
import boto3
import time

s3 = boto3.resource("s3")
sns_client = boto3.client("sns")

def lambda_handler(event, context):
    def get_managed_dict():
        res = s3.Bucket("appstore-reviews").Object("managed.json").get()
        return json.loads(res["Body"].read())
    
    managed_dict = get_managed_dict()
    print(managed_dict)
    # LambdaでスクレイピングするためのPubの発行
    res = sns_client.publish(
            TopicArn = "arn:aws:sns:ap-northeast-1:988546486743:fetch_reviews_status",
            Message = json.dumps(managed_dict["app_status"])
    )
    return res
