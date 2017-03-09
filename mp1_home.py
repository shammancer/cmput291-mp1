import getpass
import cx_Oracle
import json
import random
import time

import tweet_queries as tq

def help_cmd(params):
    print("Available commands: "+' '.join(params))

def compose_tweet(user, params, con, replyto):
    if len(params) < 1:
        print("Usage: compose <text>")
        return

    text = " ".join(params)
    if len(text) > 80:
        print("Tweet too long.")
        return

    tdate = cx_Oracle.DateFromTicks(time.time())
    t = {
        'writer': user['usr'],
        'tdate': tdate,
        'text' : text,
        'tid' : None,
        'replyto' : replyto
    }

    # Generate ID
    got_tid = False
    while not got_tid:
        t["tid"] = random.randint(0, 2 ** 16) 
        if tq.get_tweet(t["tid"], con) is None:
            got_tid = True

    tq.save_tweet(t, con)

    for word in params:
        if word.startswith('#'):
            hashtag = word[1:]
            if tq.get_hashtag(hashtag, con) is None:
                tq.save_hashtag(hashtag, con)
            tq.save_mention(t, hashtag, con)
    print("Tweet Created")


def home_mode(user, con):
    print("Getting the tweets from those you follow")
    ftlc = tq.get_follower_tweets_curs(user, con)
    tq.print_tweet_list(tq.get_next_tweets(ftlc, 5))

    while True:
        prompt = user["name"].strip() + " (" + str(user["usr"]) + ")" + " Home: #> "
        s = input(prompt)
        params = s.split(' ')
        cmd = params[0]
        del params[0]
        if cmd == "logout":
            return True
        elif cmd == "exit":
            return False
        elif cmd == "help":
            help_cmd(["logout", "exit","help","more","compose","select"])
            return (True, True)
        elif cmd == "more":
            tq.print_tweet_list(tq.get_next_tweets(ftlc, 5))
        elif cmd == "compose":
            compose_tweet(user, params, con, None)
        elif cmd == "select" :
            tweet_details_mode(user, params, con)

def tweet_details_mode(user, targetTweet, con):
    if len(targetTweet)<1:
        print("Usage: select <tweet id>")
        return
    tq.print_tweet_details(tq.get_tweet_details(targetTweet[0],con))
    while True:
        prompt = user["name"].strip() + " (" + str(user["usr"]) + ")" + " Tweet Details: #> "
        s = input(prompt)
        args = s.split(' ')
        cmd = args[0]
        del args[0]
        if cmd == "home":
            return True
        if cmd == "help":
            help_cmd(["home","help", "retweet", "reply"])
        if cmd == "retweet":
            retweet(user,targetTweet[0],con)
        if cmd == "reply":
            reply(user,args,con,targetTweet[0])
def retweet(user,replyto,con):
    rdate = cx_Oracle.DateFromTicks(time.time())
    t = {
        'usr': user['usr'],
        'rdate': rdate,
        'tid' : replyto
    }
    tq.save_retweet(t,con)
    print("Retweeted!")
            
def reply(user, text, con, replyto):
    compose_tweet(user,text,con,replyto)
    print("Replied to tweet!")

    
    
    
    
    
    
    
