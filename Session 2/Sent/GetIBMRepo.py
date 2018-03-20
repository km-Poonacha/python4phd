# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 11:40:49 2018

@author: kmpoo
"""

import requests
import json
import csv

def write_csv(WRITE_CSV,mode, row):
    """This function writes a row in a csv file. It is given three parameters a) the link to the file to  be written, 
    b) the mode of wrtting the file ('at' for append or 'wt' to re-write file) and c) the row to be written (sent as a list).
    """
    with open(WRITE_CSV, mode,encoding = 'utf-8', newline='') as csv_obj: # the newline parameter prevents the blank row we saw in some laptops
        write = csv.writer(csv_obj) # Note it is csv.writer not reader
        write.writerow(row)
        
def GithubAPI(url):
    """ Make a HTTP request for the given URL and send the response body
    back to the calling function"""
    response = requests.get(url)
    if response.status_code == 200:
        print('Response status - OK ')
        return response.json()
    else:
        print('Error making the HTTP request ',response.status_code  )
        return None

def main():
    url = "https://api.github.com/orgs/ibm"
    write_csv_link = "C:/Users/kmpoo/Dropbox/HEC/Teaching/Python for PhD Mar 2018/python4phd/Session 2/ipython/Repo_csv.csv"

    txt_response = GithubAPI(url)
    
    if txt_response:
        print('The number of public repos are : ',txt_response['public_repos'])
        repo_url = txt_response['repos_url']
        repo_response = GithubAPI(repo_url)
        for repo in repo_response:
            write_csv(write_csv_link, 'at', [repo['id'],repo['name']])
        
main() 