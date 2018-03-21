# -*- coding: utf-8 -*-
"""Code snippet with one error. can you debug and find the error?. 
    Run the code and enter the sentence " good good ". Why does it give sentiment of the sentence as  3 ? It should be 6.
   a. Use print statements to see what the variable value is 
   b. Insert breakpoint inside the loop and execute the loop one by one 
   c. Use the variable window and insert the local variable "char" and "i" in it. 
   d. Last resort, google and stackoverflow
"""   
import csv

SENTIMENT_CSV = "C:/Users/kmpoo/Dropbox/HEC/Teaching/Python for PhD Mar 2018/python4phd/Session 3/Sent/word_sentiment.csv"

def sentence_sentiment(sentence):
    """This function calculates the sentiment of the sentence given to it. 
    It splits the sentence into words and finds the sentiment of the word using the word_sentiment.csv.
    It returns the agregated sentiment of the  sentence """
    sentiment = 0
    word_list = sentence.split()
    with open(SENTIMENT_CSV,'rt',encoding='utf-8') as sentobj:
        sent_handle = csv.reader(sentobj)        
        for word in word_list:
            for row in sent_handle:
                if row[0] == word:
                    sentiment = sentiment + int(row[1])
                    break
        return sentiment

def main():
    sentence = input("Enter your sentence : ").lower()
    sentiment = sentence_sentiment(sentence)
    print("sentiment of the sentence is = ",sentiment )
    
if __name__ == '__main__':
    main()