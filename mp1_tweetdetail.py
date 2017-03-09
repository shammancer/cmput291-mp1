import tweet_tools as tt
import printing as p
def tweet_details_mode(user, targetTweet, con):
    if len(targetTweet)<1:
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
            help_cmd(["home","help", "retweet", "reply"])
        elif cmd == "retweet":
            tt.retweet(user,targetTweet[0],con)
        elif cmd == "reply":
            tt.reply(user,args,con,targetTweet[0])