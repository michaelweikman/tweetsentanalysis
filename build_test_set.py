import tweepy
import csv
import time
from datetime import datetime
import os

auth = tweepy.OAuthHandler("y5kEUkqCvnpKlRQ85c9eZbRMc", "9MokzV6ul6WeM5RoepwfxlQGKFrz9H7rC4zoSIVhjzcQhOgXm9")
auth.set_access_token("45267411-FhzWglS57UHEi1nnOevZ3KNMYYpj283BBGoirgaJa", "bikoa1GJehmW3LVmc7gKbCR153FpB6LtacaLmhFMDKDyj")
api = tweepy.API(auth)

cur_dir = os.path.dirname(os.path.abspath(__file__))
out_csv_path = os.path.join(cur_dir, 'Resources/test_data.csv')


def buildTestSet(search_keyword):
    try:
        tweets_fetched = api.search(search_keyword, count = 5)
        
        print("Fetched " + str(len(tweets_fetched)) + " tweets for the term " + search_keyword)
        
        return [{"text":status.text, "label":None} for status in tweets_fetched]
    except:
        print("Unfortunately, something went wrong..")
        return None

print(buildTestSet('trump'))

