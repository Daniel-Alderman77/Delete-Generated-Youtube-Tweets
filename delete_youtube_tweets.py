# Based upon https://gist.github.com/yanofsky/5436496

import sys
import tweepy #https://github.com/tweepy/tweepy


class DeleteYoutubeTweets:

    def __init__(self):
        self.name = self

        # Twitter API credentials
        self.consumer_key = ""
        self.consumer_secret = ""
        self.access_key = ""
        self.access_secret = ""

    def get_tweets(self, screen_name):
        print "Now attempting to retrieve tweets for " + screen_name

        # authorize twitter, initialize tweepy
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_key, self.access_secret)
        api = tweepy.API(auth)

        # initialize a list to hold all the tweepy Tweets
        list_of_tweets = []

        # make initial request for most recent tweets (200 is the maximum allowed count)
        response = api.user_timeline(screen_name=screen_name, count=200)

        # save most recent tweets
        list_of_tweets.extend(response)

        print list_of_tweets

    if __name__ == '__main__':
        try:
            user_input = sys.argv[1]

            # Pass in the username of the account
            get_tweets(user_input)

        except IndexError:
            print "Please enter twitter username as an argument"
