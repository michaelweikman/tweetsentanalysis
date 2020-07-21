import re
import nltk
from nltk.stem import WordNetLemmatizer
from string import punctuation

tokenizer = nltk.tokenize.casual.TweetTokenizer(preserve_case=False, reduce_len=True, strip_handles=True)
def custom_tokenizer(tweet):
        tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', 'url', tweet) # remove URLs
        tweet = re.sub(r'#([^\s]+)', r'\1', tweet) # remove the # in #hashtag
        doc = tokenizer.tokenize(tweet)
        stopwords = list(punctuation) + ['url', 'rt', '...']
        return [WordNetLemmatizer().lemmatize(token) for token in doc if token not in stopwords]