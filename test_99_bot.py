#import twython
#import sys
from random import choice
# Run the file in cmd with 4 arguments

def generate_tweet():
    synonym_list = {
        "amazing": "wonderful", "anger": "arouse", "beautiful": "handsome",
        "big": "enormous", "cool": "frigid", "dark":"unlit"}
    word = choice(synonym_list.keys())
    synonym = synonym_list[word]
    tweet = "If you're having " + word + " problems (...) I got 99 problems but a " + synonym + " ain't one."
    print tweet


#api_key, api_secret, access_token, token_secret = sys.argv[1:]

#twitter = twython.Twython(api_key, api_secret, access_token, token_secret

#twitter.update_status(status=generate_tweet)

generate_tweet()