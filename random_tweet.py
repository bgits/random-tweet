import random
import sys

from requests_oauthlib import OAuth1Session


class TwitterApi(object):
    BASE_URL = 'https://api.twitter.com/1.1/search/tweets.json'
