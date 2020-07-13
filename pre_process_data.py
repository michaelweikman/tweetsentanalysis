import csv
import spacy
import os
import re
import pandas as pd
from string import punctuation
from spacy.lang.en.stop_words import STOP_WORDS

cur_dir = os.path.dirname(os.path.abspath(__file__))
t_data_csv = os.path.join(cur_dir, 'Resources/training_data_v2.csv')
        

#Taken from processing example github
class PreProcessTweets:
    def __init__(self):
        self._stopwords = set(list(STOP_WORDS) + list(punctuation) + ['AT_USER','URL'])
        self._nlp = spacy.load("en_core_web_sm")
        
    def processTweets(self, list_of_tweets):
        processedTweets=[]
        for tweet in list_of_tweets:
            processedTweets.append((self._processTweet(tweet["text"]),tweet["label"]))
        return processedTweets
    
    def _processTweet(self, tweet):
        tweet = tweet.lower() # convert text to lower-case
        tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', 'URL', tweet) # remove URLs
        tweet = re.sub('@[^\s]+', 'AT_USER', tweet) # remove usernames
        tweet = re.sub(r'#([^\s]+)', r'\1', tweet) # remove the # in #hashtag
        tweet = self._nlp(tweet) # Toleknize
        return [word for word in tweet if word not in self._stopwords]

tweetProcessor = PreProcessTweets()

# Reading the file
df = pd.read_csv(t_data_csv, index_col=0)

# Creating the dict
trainingData = list(df.transpose().to_dict().values())

preprocessedTrainingSet = tweetProcessor.processTweets(trainingData)

