import re
import json
import urllib.parse
from datetime import timedelta

import pandas as pd
import boto3

s3 = boto3.resource("s3")
sns_client = boto3.client("sns")

def lambda_handler(event, context):
    # appstore-reviews/json/*.jsonが作られたのをトリガーに
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    file_name = key.split("/")[1].split(".")[0]
    app_id = file_name.split("-")[0]
    most_recent_date = "-".join(file_name.split("-")[3:])
    
    res = s3.Bucket(bucket).Object(key).get()
    
    csv_arr = [
            [
                rv["id"]["label"], app_id, rv["updated"]["label"],
                rv["im:version"]["label"],rv["author"]["name"]["label"],
                rv["im:rating"]["label"],rv["title"]["label"],rv["content"]["label"]
            ] for rv in json.loads(res["Body"].read())
        ]
    
    df = pd.DataFrame(
        csv_arr,
        columns=[
            "id", "app_id", "date", "app_version", "user_name",
            "rating", "title", "content"
        ]
    )
    # 時刻を日本時間に修正
    df["date"] = (pd.to_datetime(df.date) + timedelta(hours=7)).dt.strftime("%Y-%m-%d %H:%M:%S")
    # json => csv
    obj = s3.Object("appstore-reviews", "csv/{}.csv".format(file_name))
    obj.put(Body=df.to_csv(index=None, quotechar="'", quoting=1).encode("utf-8"))
    
    # managed_dict更新用のpub発行
    res = sns_client.publish(
        TopicArn = "arn:aws:sns:ap-northeast-1:988546486743:update_manage_dict",
        Message = "{}<SEP>{}".format(app_id, most_recent_date),
    )
    return res