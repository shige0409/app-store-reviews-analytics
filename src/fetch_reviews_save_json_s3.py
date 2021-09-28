import requests
import boto3
import json
import time

s3 = boto3.resource('s3')

def lambda_handler(event, context):
    # 特定のアプリレビューのページ1つ(50件)をスクレイピング
    def get_app_reviews(app_id, page_id):
        app_review_url = "https://itunes.apple.com/jp/rss/customerreviews/id={}/sortBy=mostRecent/page={}/json".format(app_id, page_id)
        headers = {"content-type": "application/json"}
        r = requests.get(app_review_url, headers=headers)
        # スクレイピングするため
        time.sleep(10)
        return r.json()["feed"]["entry"]
    
    # {"app_id": "date", ..., ...}で入ってくる
    managed_dict = json.loads(event["Records"][0]["Sns"]["Message"])
    # アプリごとにスクレイピング+jsonファイルを保存
    for app_id, fetch_date in managed_dict.items():
        reviews_for_saves3 = []
        # appレビューのページ分
        for page_idx in range(1, 5):
            reviews = get_app_reviews(app_id, page_idx)
            # 過去のスクレイピングしたことがない場合
            if fetch_date == "null":
                reviews_for_saves3 += reviews
                continue
            # fetch_dateまでスクレイピングしている場合
            else:
                reviews = [rv for rv in reviews if rv["updated"]["label"] > fetch_date]
                reviews_for_saves3 += reviews
                # 余分にスクレイピングしている場合
                if len(reviews) < 50:
                    break
        
        obj = s3.Object(
            "appstore-reviews",
            "json/{}-reviews-by-{}.json".format(
                app_id, reviews_for_saves3[0]["updated"]["label"]
            )
        )
        obj.put(Body=json.dumps(reviews_for_saves3, ensure_ascii=False, indent=4))
        print("app_id: {}を{}レビュー保存しました。".format(app_id, len(reviews_for_saves3)))
    
    return "Success"