import tweet_tools as tt
import tweet_queries as tq
import printing as p
import numbers as n
def tweet_detail_mode(user, targetTweet, con):
    if len(targetTweet)<1 or not targetTweet[0].isdigit() :
        print("Usage: select <tweet id>")
        return
    p.print_tweet_details(tq.get_tweet_details(targetTweet[0],con))
    while True:
        prompt = user["name"].strip() + " (" + str(user["usr"]) + ")" + " Tweet Details: #> "
        s = input(prompt)
        args = s.split(' ')
        cmd = args[0]
        del args[0]
        if cmd == "home":
            return True
        elif cmd == "help":
            p.help_cmd(["home","help", "retweet", "reply"])
        elif cmd == "retweet":
            if not tq.has_retweeted(user["usr"], targetTweet[0], con):
                tt.retweet(user,targetTweet[0],con)
            else:
                print("Already Retweeted")
        elif cmd == "reply":
            tt.reply(user,args,con,targetTweet[0])
