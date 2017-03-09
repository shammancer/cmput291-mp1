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