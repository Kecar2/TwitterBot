import tweepy
import time
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')
BEARER_TOKEN = os.getenv('BEARER_TOKEN')

client = tweepy.Client(BEARER_TOKEN, API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

auth = tweepy.OAuthHandler(API_KEY,API_SECRET)
auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
print('Authentication successful')

api = tweepy.API(auth)


''' 
Crear Tweet
'''
#client.create_tweet(text='Prueba2')

'''
Dar Like a tweet
'''
#client.like(1583926410602758144)

'''
Dar retweet
'''
#client.retweet(1583926410602758144)

'''
Responder un tweet
'''
#client.create_tweet(in_reply_to_tweet_id=1583926410602758144, text='funciona?')

'''
Obtener informacion de una cuenta
'''

'''
person = client.get_user(username='').data.id

for tweet in client.get_users_tweets(person).data:
    print(tweet.text)
'''

'''
#Buscar tweets por palabras

search_terms = ['twitch', 'ibai', 'pokemon']

class MyStream(tweepy.StreamingClient):
    def on_connect(self):
        print('Connected')

    def on_tweet(self, tweet):
        if tweet.referenced_tweets == None:
            print(tweet.text)

            time.sleep(0.2)
        
stream = MyStream(bearer_token=BEARER_TOKEN)

for term in search_terms:
    stream.add_rules(tweepy.StreamRule(term))

stream.filter(tweet_fields=['referenced_tweets'])

'''
################################################################################
'''
# Dar Likes a tweets

class MyStream(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        try:
            print(tweet.text)
            client.like(tweet.id)
        except Exception as error:
            print(error)

        time.sleep(1)

stream = MyStream(bearer_token=BEARER_TOKEN)

stream.add_rules(tweepy.StreamRule('#Python OR #programming -is:retweet -is:reply'), dry_run=True)

stream.filter()
'''

# Get Trend por Ubicacion

lat = 41.38879
lon = 2.15899
trends = api.closest_trends(lat,lon)
woeid = trends[0]['woeid']
top_trends = api.get_place_trends(woeid)
for item in top_trends[0]['trends']:
    print('\n')
    print(item)
