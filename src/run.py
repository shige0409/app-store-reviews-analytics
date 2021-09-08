import requests
import json

def get_app_reviews(app_id, page_id):
    app_review_url = "https://itunes.apple.com/jp/rss/customerreviews/id={}/sortBy=mostRecent/page={}/json".format(app_id, page_id)
    headers = {"content-type": "application/json"}
    r = requests.get(app_review_url, headers=headers)
    reviews_dict = r.json()


if __name__ == "__main__":
    get_app_reviews("1325457827", "1")