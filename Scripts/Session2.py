#Installations required -  $pip install tweepy, 
#Installed $ pip install yahoo-finance. However before i could do it i needed to export $ CC=gcc
# Initialize tweepy and authorize

import tweepy
from tweepy import OAuthHandler
import json
import csv
from yahoo_finance import Share
from pandas_datareader import data, wb
import pandas_datareader.data as web

from datetime import date
from datetime import datetime
from datetime import time

consumer_key = 'XXX'
consumer_secret = 'XXX'
access_token = 'XXX'
access_secret = 'XXX'

DONTWEETS_CSV = '/Users/medapa/Dropbox/HEC/Teaching/Python Sep 2016/Data/DONTWEETS.csv'
DONTWEETS_WORDS_CSV = '/Users/medapa/Dropbox/HEC/Teaching/Python Sep 2016/Data/DONTWEETSWRDS.csv'

def get_index(index):
#This function searches yahoo finance and gets the index values 
#Trump anounced his candidacy for president on June 16 2015. So we start the tweet analysis fro mthe 16th. 
    start = datetime(2015,06,16)
    end = date.today()
    index_data = web.DataReader(str(index), 'yahoo', start, end)
    return index_data
    
    
def collect_tweets(no_tweets):
#This function finds the donald trump tweets and stores the collected data in a CSV file
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)  
    api = tweepy.API(auth)
#get index data and store in respective lists 
    DOW30 = get_index("^DJI")
    NASDAQ = get_index("^IXIC") 
#    FTSE100 = get_index("^FTSE")
    CAC40 = get_index("^FCHI")
#    EURO50 = get_index("^STOXX50E")
    MEXBOL = get_index("^MXX")   
    prev_tweet_date = ''
    tweet_count = 1
# Get the tweets from realDonaldTrump
    for status in tweepy.Cursor(api.user_timeline, id= 'realDonaldTrump').items(no_tweets):
#Encode to utf8
        if status._json['text'] is None:
            tweet_text = ''                    
        else: 
            tweet_text = status._json['text'].encode('utf8', 'replace')  
        
        reply_uid = status._json['in_reply_to_user_id'] 
        reply_stateid = status._json['in_reply_to_status_id']
#Reformat tweet date using datetime
        date1 =  str(status._json['created_at'])        
        tweet_date = datetime.strptime(date1[:20]+date1[26:30],'%a %b %d %H:%M:%S %Y')  
        
# Get the stock index data specific to the tweet date       
        if (date1[:3] != 'Sun' and date1[:3] != 'Sat') and (str(tweet_date.date()) != prev_tweet_date):
            print date1[:3] 
            prev_tweet_date = str(tweet_date.date())
            print "current tweet date", tweet_date.date()
            print "prev tweet", prev_tweet_date
            
            try:
                DOW30_val = (DOW30.Close[str(tweet_date.date())] - DOW30.Open[str(tweet_date.date())])/DOW30.Open[str(tweet_date.date())]
            except:
                print "EXCEPTION KEY ERROR AT DOW30_val date",str(tweet_date.date())
                DOW30_val = ''
                
            try:
                NASDAQ_val = (NASDAQ.Close[str(tweet_date.date())] - NASDAQ.Open[str(tweet_date.date())])/NASDAQ.Open[str(tweet_date.date())]
            except:
                print "EXCEPTION KEY ERROR AT NASDAQ_val date",str(tweet_date.date())
                NASDAQ_val = ''
                
#            try:
#                FTSE100_val = FTSE100.ix[str(tweet_date.date())]
#            except:
#                print "EXCEPTION KEY ERROR AT FTSE100_val date",str(tweet_date.date())
#                FTSE100_val = '' 
                
            try: 
                CAC40_val = (CAC40.Close[str(tweet_date.date())] - CAC40.Open[str(tweet_date.date())])/CAC40.Open[str(tweet_date.date())]
            except:
                print "EXCEPTION KEY ERROR AT CAC40_val date",str(tweet_date.date())
                CAC40_val = ''
                
#            try: 
#                EURO50_val= (EURO50.Close[str(tweet_date.date())] - EURO50.Open[str(tweet_date.date())])/EURO50.Open[str(tweet_date.date())]
#            except:
#                print "EXCEPTION KEY ERROR AT EURO50_val date",str(tweet_date.date())
#                EURO50_val = ''
            
            try:
                MEXBOL_val = (MEXBOL.Close[str(tweet_date.date())] -MEXBOL.Open[str(tweet_date.date())])/MEXBOL.Open[str(tweet_date.date())]
            except:
                print "EXCEPTION KEY ERROR AT MEXBOL_val date",str(tweet_date.date())
                MEXBOL_val =''
            day_tweet_count = tweet_count
            tweet_count = 1
            
        else:
            DOW30_val = ''
            NASDAQ_val = ''
#            FTSE100_val = ''
            CAC40_val = ''
 #           EURO50_val= ''
            MEXBOL_val = ''
            day_tweet_count = ''
            tweet_count = tweet_count + 1
            

#Store relavent information in csv        
        with open(DONTWEETS_CSV , 'ab') as don_tweets:
            tweet_write = csv.writer(don_tweets)
            tweet_write.writerow([status._json['created_at'],tweet_text,status._json['favorite_count'],status._json['retweet_count'],DOW30_val,NASDAQ_val,CAC40_val,MEXBOL_val,day_tweet_count ])
                   
    return
    
def word_count(word): 
# This function counts the number of times a word has been used 
    with open(DONTWEETS_CSV , 'rb') as don_tweets:
        tweet_read = csv.reader(don_tweets)
        no_words = 0

        for tweet_row in tweet_read:
            word_list = str.split(tweet_row[1].lower())
            for tweet_words in word_list:
                if tweet_words == word:
                    no_words = no_words +1

        return no_words

def word_index():
# This function finds the words used and its count and stores them in a CSV
 
    with open(DONTWEETS_CSV , 'rb') as don_tweets:
        tweet_read = csv.reader(don_tweets)
        counting_words = [''] 
        del counting_words[:]  
        for tweet_row in tweet_read:
            word_list = str.split(tweet_row[1].lower())
            for word_list_i in word_list:
                word_done = 0
                for counting_words_i in counting_words:
                    if word_list_i == counting_words_i:
                        word_done = 1
                        break
                    else:
                        word_done = 0
                        continue
                if word_done == 0:
                    counting_words.append(word_list_i)
                    count = word_count(word_list_i)
                    if count > 100:
                        with open(DONTWEETS_WORDS_CSV , 'ab') as don_tweets_words:
                            tweet_words_write = csv.writer(don_tweets_words)
                            tweet_words_write.writerow([word_list_i,count])
                    
        
                                  
def main():        
# mention the number of tweets required
    tweets = 15000
#    collect_tweets(tweets)
    print word_count('you')
#    word_index()

if __name__ == '__main__':
  main()