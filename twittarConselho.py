# pip install tweepy
# pip install -U deep-translator

import tweepy
import time
import requests
from deep_translator import GoogleTranslator

api = tweepy.Client(
    consumer_key = 'SEU TOKEN',
    consumer_secret = 'SEU TOKEN',
    access_token = 'SEU TOKEN',
    access_token_secret = 'SEU TOKEN'
)

for i in range(10):
    advice = requests.get('https://api.adviceslip.com/advice')
    advice_dict = advice.json()

    text = advice_dict['slip']['advice']

    text_translate = GoogleTranslator(source='en', target='pt').translate(text)

    try:
        tweet = api.create_tweet(text = text_translate)
        print('Tweet: ', tweet)
    except: 
        print('Alguma coisa falhou!')