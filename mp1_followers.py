import printing as p
import user_queries as uq
import tweet_queries as tq
def followers_mode(user,con):
    print("Getting your followers")
    p.print_followers(uq.get_followers(user['usr'],con))
    while True:
        prompt = user["name"].strip() + " (" + str(user["usr"]) + ")" + " Followers: #> "
        s = input(prompt)
        params = s.split(' ')
        cmd = params[0]
        del params[0]
        if cmd == "home":
            return True
        elif cmd == "help":
            help_cmd(["home", "select","help"])
        elif cmd == "select":
            follower_detail_mode(user,params,con)
            
def follower_detail_mode(user, targetUser, con):
    if len(targetUser)<1:
        print("Usage: select <User id>")
        return

    p.print_follower_details(uq.get_follower_details(targetUser[0],con))
    curs = tq.get_user_tweets_curs(targetUser[0],con)
    p.print_tweet_list(tq.get_next_tweets(curs,3))
    while True:
        prompt = user["name"].strip() + " (" + str(user["usr"]) + ")" + " Follower Details: #> "
        s = input(prompt)
        params = s.split(' ')
        cmd = params[0]
        del params[0]
        if cmd == "exit":
            return True
        elif cmd == "help":
            help_cmd(["exit", "more","help","follow"])
        elif cmd == "more":
            p.print_tweet_list(tq.get_next_tweets(curs,3))
        elif cmd == "follow":
            uq.save_follow(user['usr'],targetUser[0],con)