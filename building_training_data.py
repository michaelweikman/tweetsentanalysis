import tweepy
import csv
import time
from datetime import datetime
import os

# auth = tweepy.OAuthHandler()
# auth.set_access_token()
# api = tweepy.API(auth)

cur_dir = os.path.dirname(os.path.abspath(__file__))
corpus_csv_path = os.path.join(cur_dir, 'Resources/corpus.csv')
out_csv_path = os.path.join(cur_dir, 'Resources/training_data.csv')
log_file = os.path.join(cur_dir, "Logs/log.txt")

def build_training_data():
    c_list = []
    logs = []
    with open(corpus_csv_path, 'rt') as csvfile:
        lr = csv.reader(csvfile, delimiter=',',  quotechar="\"")
        for row in lr:
            c_list.append({"topic":row[0], "label":row[1], "tweet_id":row[2]})
    
    training_set = []
    list_len = len(c_list)
    count = int(0)

    for tw in c_list:
        tw_id = tw["tweet_id"]
        now = datetime.now()
        try:
            status = api.get_status(tw_id)
            tw['text'] = status.text
            training_set.append(tw)
            time.sleep(5)
        except:
            date = now.strftime("%d/%m/%Y %H:%M:%S")
            logs.append(f"{date} - Could Not Fetch Tweet_Id: {tw_id} \n")
            continue

        count += 1
        pcnt_done = round(((count/list_len) * 100), 2)
        print(f"...Progress: {pcnt_done}%", end="\r", flush=True)
    
    if(len(logs) > 0):
        with open(log_file, 'wt') as log:
            log.writelines(logs)

    export_to_file(training_set, out_csv_path)


def export_to_file(t_set, file_path):
    with open(file_path, 'wt') as file:
        lr = csv.writer(file, delimiter=',', quotechar="\"")
        for tw in t_set:
            try:
                lr.writerow([tw["tweet_id"], tw["text"], tw["label"], tw["topic"]])
            except Exception as e:
                print(e)
            
build_training_data()