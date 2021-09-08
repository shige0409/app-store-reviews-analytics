import requests

def lambda_handler(event, context):
    def get_app_reviews(app_id, page_id):
        app_review_url = "https://itunes.apple.com/jp/rss/customerreviews/id={}/sortBy=mostRecent/page={}/json".format(app_id, page_id)
        headers = {"content-type": "application/json"}
        r = requests.get(app_review_url, headers=headers)
        return r.json()

    return get_app_reviews("1325457827", "1")

# if __name__ == "__main__":
#     get_app_reviews("1325457827", "1")