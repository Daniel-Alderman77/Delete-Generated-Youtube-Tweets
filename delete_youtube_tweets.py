# Based upon https://gist.github.com/yanofsky/5436496

import sys


# Twitter API credentials
consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""


def get_tweets(screen_name):
    print "Now attempting to retrieve tweets for " + screen_name


if __name__ == '__main__':
    try:
        user_input = sys.argv[1]

        # Pass in the username of the account
        get_tweets(user_input)

    except IndexError:
        print "Please enter twitter username as an argument"
