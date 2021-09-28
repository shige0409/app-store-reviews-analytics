import json
import boto3

s3 = boto3.resource('s3')

def lambda_handler(event, context):
    def get_managed_dict():
        res = s3.Bucket("appstore-reviews").Object("managed.json").get()
        return json.loads(res["Body"].read())
    
    managed_dict = get_managed_dict()
    app_id, most_recent_date = event["Records"][0]["Sns"]["Message"].split("<SEP>")
    # 最新習得日に更新
    managed_dict["app_status"][app_id] = most_recent_date
    # json書き込み
    obj = s3.Object("appstore-reviews", "managed.json")
    obj.put(Body=json.dumps(managed_dict, ensure_ascii=False, indent=4))
    
    return "update managed.json success"
    