import tweepy

consumer_key = 'REPLACE_WITH_CONSUMER_KEY'

consumer_secret = 'REPLACE_WITH_CONSUMER_SECRET'

access_token = 'REPLACE_WITH_ACCESS_TOKEN_NOT_BEARER'

access_token_secret = 'REPLACE_WITH_ACCESS_TOKEN_SECRET_NOT_BEARER'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# change this for the shit yuou wanna tweet 
tweet = 'AHHHHHHHHHHHHHHHHHH'

api.update_status(status=tweet)
