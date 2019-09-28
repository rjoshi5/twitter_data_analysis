# Python program for fetching tweets to csv

# importing all necessery modules

from searchtweets import ResultStream, gen_rule_payload, load_credentials

# Type credentials 
import os
os.environ["SEARCHTWEETS_ENDPOINT"] = 'https://api.twitter.com/1.1/tweets/search/fullarchive/dev.json'
os.environ["SEARCHTWEETS_BEARER_TOKEN"] = '***********************************************'   
#replace **************************** with your token
os.environ["SEARCHTWEETS_ACCOUNT_TYPE"] = 'premium'
search_args = load_credentials()
{'account_type': 'premium',
    'endpoint': 'https://api.twitter.com/1.1/tweets/search/fullarchive/dev.json',
    'bearer_token': '***************************************'}


# Rule for the search (format date YYYYMMDDHHMM)
rule = gen_rule_payload("facebook breach",  from_date = '201809280000', to_date = '201809280331', results_per_call=100)     # 100 max results per page for sandbox 
print(rule)

from searchtweets import collect_results

tweets = collect_results(rule,
                         max_results=100,
                         result_stream_args=search_args)
[print(tweet.all_text) for tweet in tweets[0:10]]           # Printing the first 10 tweets to view the tweets


# Structure data into the data frames
import pandas as pd

# Save to csv the raw file
df1 = pd.DataFrame(tweets)
df1.to_csv('tweets_facebook_ext.csv')       

dict_ = {'date': [], 'device': [], 'text': [], 'location': []}  
for tweet in tweets:  
    dict_['date'].append(tweet.created_at_datetime)
    dict_['device'].append(tweet.generator.get("name"))
    dict_['text'].append(tweet.all_text)
    dict_['location'].append(tweet.generator.get("location"))       # Location is available for paid Premium account

# Save to csv file table from Data Frame
df = pd.DataFrame(dict_) 
df.to_csv('tweets_facebook.csv')        





