import getpass
import cx_Oracle
import json
import random
import time

import tweet_queries as tq
import user_queries as uq
import printing as p
import mp1_followers as followermode
import mp1_tweetdetail as tweetdetailmode
import mp1_search as searchmode
import tweet_tools as tt



def home_mode(user, con):
    print("Getting the tweets from those you follow")
    ftlc = tq.get_follower_tweets_curs(user, con)
    p.print_tweet_list(tq.get_next_tweets(ftlc, 5))

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
            p.help_cmd(["logout", "exit","help","more","compose","select","followers","search-user","search-tweet"])
        elif cmd == "more":
            p.print_tweet_list(tq.get_next_tweets(ftlc, 5))
        elif cmd == "compose":
            tt.compose_tweet(user, params, con, None)
        elif cmd == "select" :
            tweetdetailmode.user_detail_mode(user, params, con)
        elif cmd == "followers" :
            followermode.followers_mode(user,con)
        elif cmd == "search-user":
            searchmode.user_search_mode(user,params,con)
        elif cmd == "search-tweet": 
            searchmode.tweet_search_mode(user,params,con)
		




    
    
    
    
    
    
    
