import getpass
import cx_Oracle
import json
import random

import tweet_queries as tq

def help_cmd(params):
    print("Available commands: logout, exit, help")

def home_mode(user, con):
    print("Getting the tweets from those you follow")
    ftlc = tq.get_follower_tweets_curs(user, con)
    tq.print_tweet_list(tq.get_next_tweets(ftlc, 5))

    while True:
        prompt = user["name"].strip() + " (" + str(user["usr"]) + ")" + " #> "
        s = input(prompt)
        params = s.split(' ')
        cmd = params[0]
        del params[0]
        if cmd == "logout":
            return True
        elif cmd == "exit":
            return False
        elif cmd == "help":
            help_cmd(params)
            return (True, True)
        elif cmd == "more":
            tq.print_tweet_list(tq.get_next_tweets(ftlc, 5))
