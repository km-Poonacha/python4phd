# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 18:45:46 2018

@author: kmpoo
"""

import requests
import json
    
def GithubAPI(url):
    """ Make a HTTP request for the given URL and send the response body
    back to the calling function"""
    reponse = requests.get(url)
    if response.status_code == 200:
        print('Response status - OK ')
        return response.text
    else:
        print('Error making the HTTP request ',response.status_code  )
        return None

def main():
    url = "https://api.github.com/users/km-poonacha"
    txt_response = GithubAPI(url)
    
    if txt_response:
        print(txt_response)
        json_repsonse = json.loads(txt_response)
        print(json_response)

main() 