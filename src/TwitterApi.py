import tweepy
import os
from dotenv import load_dotenv

class TwitterApi:

    def __init__(self):
        load_dotenv()
        self.client = tweepy.Client(consumer_key=os.environ['CONSUMER_KEY'], consumer_secret=os.environ['CONSUMER_SECRET'], access_token=os.environ['USER_TOKEN'], access_token_secret=os.environ['USER_SECRET'], wait_on_rate_limit=True)

    def tweet(self, text):
        self.client.create_tweet(text=text)