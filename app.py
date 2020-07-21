from flask import Flask, render_template, redirect, request, jsonify
from startModel import TweetModel
from custom_tokenizer import custom_tokenizer
from joblib import load

app = Flask(__name__)
tweetModel = TweetModel(load("sentiment_model.joblib"))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search/<term>")
def search(term):
    texts = tweetModel.Search(term, pages=20)
    data = {
        'tweets': texts,
        'custom_predictions': tweetModel.Custom_Predict(texts),
        'vader_predictions': tweetModel.Vader_Predict(texts)
    }
    return jsonify(data)

@app.route("/predict/<tweet>")
def predict(tweet):
    prediction = tweetModel.Custom_Predict(tweet)
    return jsonify(prediction)

@app.route("/vaderpredict/<tweet>")
def vader_predict(tweet):
    prediction = tweetModel.Vader_Predict(tweet)
    return jsonify(prediction)
    
if __name__ == "__main__":
    app.run(debug=True)