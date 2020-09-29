import flask
import os
import tweepy
import random 
import requests
import json
from os.path import join, dirname
from dotenv import load_dotenv

app = flask.Flask(__name__)

dotenv_path = join(dirname(__file__), 'spoonacular.env')
load_dotenv(dotenv_path)

dotenv_path = join(dirname(__file__), 'tweepy.env')
load_dotenv(dotenv_path)

consumer_key= os.environ['CONSUMER_KEY']
consumer_secret = os.environ['CONSUMER_SECRET']
access_token= os.environ['ACCESS_TOKEN']
access_token_secret = os.environ['ACCESS_TOKEN_SECRET']

spoonacular_key = os.environ['SPOONACULAR_KEY']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
auth_api = tweepy.API(auth)

@app.route('/') # Python decorator 
def index():
    list_item=["Samosas","Gulab Jamun","Gajar Ka Halwa","Falafel", "Lassi", "Cake","Ice Cream"]
    keyword=random.choice(list_item)
    response = requests.get(
    "https://api.spoonacular.com/recipes/search?query=" + keyword +
    "&apiKey=" + spoonacular_key)
    json_body = response.json()
    title=(json.dumps(json_body['results'][0]["title"], indent=2))
    food_title=title.replace('"','')
    item_id=(json.dumps(json_body['results'][0]["id"], indent=2))
    tweets = auth_api.search(q=keyword, lang="en", tweet_mode='extended')
    for tweet in tweets:
        result=(tweet.full_text)
        screen_name=(tweet.user.screen_name)
        date_time=(tweet.created_at)
    
    return flask.render_template(
        "index.html",
        keyword=keyword,
        result=result,
        screen_name=screen_name,
        date_time=date_time,
        food_title=food_title,
        item_id=item_id,
        ) 
  
app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0')
)
