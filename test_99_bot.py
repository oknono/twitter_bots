#import twython
#import sys
from random import choice
from random import randrange
#from nltk.corpus import wordnet as wn
#import json
# Run the file in cmd with 4 arguments

#json_file = open("corpora/data/animals/common.json")
#json_data = json.load(json_file)

def generate_tweet():
	# Test example, replace with larger JSON file later
	# All values should be in list, also if there's only one value
    synonym_list = {
        "amazing": ["wonderful", "great", "fantastic"], "anger": ["arouse", "angry"], "beautiful": ["handsome", "pretty"],
        "big": ["enormous", "gigantic"], "cool": ["frigid", "cold"], "dark":["unlit"]}
    # word = json_data.keys().value()
    word = choice(synonym_list.keys())
    synonym_list = synonym_list[word]
    s_index = randrange(len(synonym_list))
    synonym = synonym_list[s_index]

    #synonym = wn.synsets( word )

    print "Word is", 
    print word 
    print "Synonym is", 
    print synonym
 
    # Print the information
    #for synset in synsets:
    #    print "-" * 10
    #    print synset.name
    #tweet = "If you're having " + word + " problems (...) I got 99 problems but a " + synonym + " ain't one."
    #print tweet


#api_key, api_secret, access_token, token_secret = sys.argv[1:]

#twitter = twython.Twython(api_key, api_secret, access_token, token_secret

#twitter.update_status(status=generate_tweet)

generate_tweet()