from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import tweepy
import numpy as np
import pandas as pd

auth = tweepy.OAuthHandler("y5kEUkqCvnpKlRQ85c9eZbRMc", "9MokzV6ul6WeM5RoepwfxlQGKFrz9H7rC4zoSIVhjzcQhOgXm9")
auth.set_access_token("45267411-FhzWglS57UHEi1nnOevZ3KNMYYpj283BBGoirgaJa", "bikoa1GJehmW3LVmc7gKbCR153FpB6LtacaLmhFMDKDyj")

class TweetModel:
    def __init__(self, myModel):
        self.model = myModel
        self.api = tweepy.API(auth)
        self.vadarAnalyzer = SentimentIntensityAnalyzer()

    def Process_Cursor(self):
        texts = []
        for page in self.cursor:
            for status in page:
                texts.append(status.full_text)

        return texts

    def Search(self, query, pages=1):
        self.cursor = tweepy.Cursor(self.api.search, q=f'{query} -filter:retweets"', count=100, lang="en", tweet_mode="extended").pages(pages)
        return self.Process_Cursor()

    def Compare_Models(self):
        text_arr = []
        for page in self.cursor:
            for status in page:
                text_arr.append(status.text)
        print(text_arr)

    def Custom_Predict(self, texts):
        if(not isinstance(texts, list)):
            texts = [texts]

        custom_prediction = self.model.predict(texts)
        custom_prediction = list(map((lambda x: 'Positive' if (x == 1) else 'Negative'), custom_prediction))
        return custom_prediction
    
    def Vader_Predict(self, texts):
        if(not isinstance(texts, list)):
            texts = [texts]

        senti_arr = []
        for text in texts:
            try:
                vader_prediction = self.vadarAnalyzer.polarity_scores(text)['compound']
                sentiment = ""
                if (vader_prediction <= -0.05):
                    sentiment = 'Negative'
                elif (vader_prediction > -0.05 and vader_prediction < 0.5):
                    sentiment = 'Neutral'
                else:
                    sentiment = 'Positive'
                
                senti_arr.append(sentiment)
            except: continue
        return senti_arr