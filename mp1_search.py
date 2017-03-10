import user_queries as uq
import tweet_queries as tq
import printing as p
import mp1_followers as user_details
import mp1_tweetdetail as tweet_details

TWEET_MODE = 0
USER_MODE = 1

def tweet_search_mode(user,params,con):
    if len(params)<1:
        print("Usage: search-tweet <keyword(s)>")
        return
    tweets = tq.search_tweet(params,con)
    p.print_tweet_list(tq.get_next_tweets(tweets, 5))
    search_mode(user,con,TWEET_MODE,tweets)
    
def user_search_mode(user,params,con):
    if len(params)<1:
        print("Usage: search-tweet <keywords>")
        return
    users = uq.search_user(params,con)
    p.print_users(uq.get_next_users(users,5))
    search_mode(user,con,USER_MODE,users)
            
def search_mode(user,con,type, curs):
    while True:
            prompt = user["name"].strip() + " (" + str(user["usr"]) + ")" + " Search Results: #> "
            s = input(prompt)
            params = s.split(' ')
            cmd = params[0]
            del params[0]
            if cmd == "home":
                return True
            elif cmd == "help":
                p.help_cmd(["home", "select","help","more"])
            elif cmd == "select":
                if type == USER_MODE:
                    user_details.user_detail_mode(user,params,con)
                else:
                    tweet_details.tweet_detail_mode(user,params,con)
            elif cmd == "more":
                if type == USER_MODE:
                    p.print_users(uq.get_next_users(curs,5))
                else:
                    p.print_tweet_list(tq.get_next_tweets(curs, 5))