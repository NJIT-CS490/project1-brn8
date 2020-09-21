import flask
import os
import tweepy
import random 

app = flask.Flask(__name__)

consumer_key= os.environ['CONSUMER_KEY']
consumer_secret = os.environ['CONSUMER_SECRET']
access_token= os.environ['ACCESS_TOKEN']
access_token_secret = os.environ['ACCESS_TOKEN_SECRET']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
auth_api = tweepy.API(auth)

@app.route('/') # Python decorator 
def index():
    list_item=["Masala Dosa","Samosa","Pav Bhaji","Palak Paneer","Gulab Jamun","Papdi Chaat","Idli Sambhar","Pizza","Pasta"]
    keyword=random.choice(list_item)
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
        ) 
  
app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0')
)
