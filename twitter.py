# pylint: disable=trailing-whitespace
# pylint: disable=line-too-long
# pylint: disable=superfluous-parens
# pylint: disable=too-many-locals
# pylint: disable=no-else-return
# pylint: disable=wrong-import-order
# pylint: disable=missing-module-docstring
# pylint: disable=invalid-envvar-default
# pylint: disable=missing-function-docstring

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
    list_item=["sdfsdf","Samosas","Gulab Jamun","Gajar Ka Halwa","Falafel", "Lassi", "Cake","Ice Cream","Tomato Soup","Bagel"]
    keyword=random.choice(list_item)
    response = requests.get(
    "https://api.spoonacular.com/recipes/search?query=" + keyword +
    "&apiKey=" + spoonacular_key)
    json_body = response.json()
    if json_body['results'] == []:
        return flask.render_template("error.html")
    else:
        title=(json.dumps(json_body['results'][0]["title"], indent=2))
        food_title=title.replace('"','')
        item_id=(json.dumps(json_body['results'][0]["id"], indent=2))
        serving=(json.dumps(json_body['results'][0]["servings"], indent=2))
        prep_time=(json.dumps(json_body['results'][0]["readyInMinutes"], indent=2))
        link=(json.dumps(json_body['results'][0]["sourceUrl"], indent=2))
        food_link=link.replace('"','')
        ingredients = requests.get(
            "https://api.spoonacular.com/recipes/extract?url="+food_link+
            "&apiKey=" + spoonacular_key)
        lst=ingredients.json()
        lst_ingredients=[]
        for i in (lst["extendedIngredients"]):
            lst_ingredients.append(i["original"])
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
            serving=serving,
            prep_time=prep_time,
            food_link=food_link,
            len=len(lst_ingredients),
            lst_ingredients=lst_ingredients
        ) 
  
app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0')
)
