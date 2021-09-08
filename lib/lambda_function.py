import requests
import boto3

dynamo_db = boto3.resource('dynamodb')
table = dynamo_db.Table("AppReviews")

def lambda_handler(event, context):
    def get_app_reviews(app_id, page_id):
        app_review_url = "https://itunes.apple.com/jp/rss/customerreviews/id={}/sortBy=mostRecent/page={}/json".format(app_id, page_id)
        headers = {"content-type": "application/json"}
        r = requests.get(app_review_url, headers=headers)
        return r.json()["feed"]["entry"]
    reviews = get_app_reviews("1325457827", "1")
    # return reviews[0]
    for review in reviews:
        response = table.put_item(
            Item={
                "id": review["id"]["label"],
                "info":{
                    "date": review["updated"]["label"],
                    "app_version": review["im:version"]["label"],
                    "name": review["author"]["name"]["label"],
                    "title": review["title"]["label"],
                    "rating": review["im:rating"]["label"],
                    "content": review["content"]["label"]
                }
            }
        )
        
    return response
    # put_movie(app_review_data)
# if __name__ == "__main__":
#     get_app_reviews("1325457827", "1")