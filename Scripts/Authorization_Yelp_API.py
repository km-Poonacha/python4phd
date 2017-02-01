TOKEN = 'XXX'
TOKEN_SECRET = 'XXX'
CONSUMER_KEY = 'XXX'
CONSUMER_SECRET = 'XXX'

import json
import requests
import oauth2

# This function performs a Yelp API request, taken from Yelp's python example
def search_yelp(url):
    ''' USE OAuth to authenticate the application. Make a request with Yelp's 
    API and return the result in JSON format'''
    consumer = oauth2.Consumer(CONSUMER_KEY, CONSUMER_SECRET)
    token = oauth2.Token(TOKEN, TOKEN_SECRET)

    oauth_request = oauth2.Request(method="GET", url=url)
    oauth_request.update({'oauth_nonce': oauth2.generate_nonce(),
                          'oauth_timestamp': oauth2.generate_timestamp(),
                          'oauth_token': TOKEN,
                          'oauth_consumer_key': CONSUMER_KEY})

    oauth_request.sign_request(oauth2.SignatureMethod_HMAC_SHA1(), 
                               consumer, token)
    signed_url = oauth_request.to_url()
    print(signed_url)
    try:
        response = requests.get(signed_url) 
        print(response.status_code)
        if response.status_code == 200:
            return json.loads(response.text)
        else: 
            print('HTTP status code not ok: ',response.status_code)
            return 0
    
    except:
        print('Error running the search, see if everything within the "try" statement is working')
        return 0
    