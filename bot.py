import random
import tweepy
from twython import Twython

from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)
twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


link = 'Any link you want posted goes here'

messages = [
        "Message goes here"]

message = random.choice(messages)
#with open('/home/pi/Downloads/image.jpg', 'rb') as photo:
#   twitter.update_status_with_media(status=message, media=photo)

twitter.update_status(status=message)
print("Tweeted: {}".format(message))