import tweepy

# Authentication
api_key = ''
api_secret = ''
bearer_token = '' 
access_token = ''
access_token_secret = ''



auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)
auth.secure = True
api = tweepy.API(auth, wait_on_rate_limit=True)



# Create Tweepy API object

api.wait_on_rate_limit_notify = True


class MyStream(tweepy.StreamingClient):
    def on_connect(self):
        print('Now connected')

    def on_status(self, status):
        if status.referenced_tweets is None:
            print(status.text)

            time.sleep(0.2)

    def on_tweet(self, tweet):
        if tweet != 0:
            print(tweet)



stream = MyStream(bearer_token)
rule1 = tweepy.StreamRule("from:elonmusk")



# Add rules to StreamingClient object


stream.add_rules(rule1)

stream.filter()
