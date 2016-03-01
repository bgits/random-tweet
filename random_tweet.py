import random
import sys

from requests_oauthlib import OAuth1Session


class TwitterApi(object):
    BASE_URL = 'https://api.twitter.com/1.1/search/tweets.json'

    def __init__(self, consumer_key,
                 consumer_secret,
                 access_token,
                 token_secret):
        self._session = OAuth1Session(consumer_key,
                                      consumer_secret,
                                      access_token,
                                      token_secret)


if __name__ == '__main__':
    from credentials import API_KEY, API_SECRET, ACCESS_TOKEN, TOKEN_SECRET

    try:
        keyword = sys.argv[1]
    except IndexError:
        keyword = None
        exit('please provide a keyword')
