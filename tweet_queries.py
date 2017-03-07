import cx_Oracle

def get_next_tweets(curs, num):
    l = curs.fetchmany(numRows=num)
    tl = []
    if l == None:
        return None
    for e in l:
        tl.append = data2tweet(e)
    return tl;

def get_follower_tweets_curs(u, con):
    curs = con.cursor()
    query = None
    with open('queries/select_follower_tweets.sql', 'r') as myfile:
        query = myfile.read() 
    curs.prepare(query)
    curs.execute(None, {"flwee": u["usr"]})
    return curs

def data2tweet(t):
    return {
        "tid": t[0],
        "writer": t[1],
        "tdate": t[2],
        "text": t[3],
        "replyto": t[4]
    }

def print_tweet_list(tl):
    if tl is None:
        print("No more tweets left");
    else:
        for t in tl:
            print(t)
    
def print_tweet(t):
    print("TID" + str(t["tid"]))
    print("Writer: " + t["writer"])
    print("Date Posted: " + str(t["date"]))
    print(t["text"])

def save_tweet(t, con):
    curs = con.cursor()
    query = None
    with open('queries/create_tweet.sql', 'r') as myfile:
        query = myfile.read()
    curs.prepare(query)
    curs.execute(None, t)
    curs.close()
    con.commit()

def get_tweet(tid, con):
    curs = con.cursor()
    query = None
    with open('queries/get_tweet.sql', 'r') as myfile:
        query = myfile.read()
    curs.prepare(query)
    curs.execute(None, {"tid": tid})
    tdata = curs.fetchone()
    curs.close()
    if tdata == None:
        return None
    return data2tweet(tdata)

def get_hashtag(hashtag, con):
    curs = con.cursor()
    query = None
    with open('queries/get_hashtag.sql', 'r') as myfile:
        query = myfile.read()
    curs.prepare(query)
    curs.execute(None, {"hashtag": hashtag})
    tdata = curs.fetchone()
    curs.close()
    if tdata == None:
        return None
    return data2tweet(tdata)

def save_hashtag(hashtag, con):
    curs = con.cursor()
    query = None
    with open('queries/create_hashtag.sql', 'r') as myfile:
        query = myfile.read()
    curs.prepare(query)
    curs.execute(None, {"hashtag": hashtag})
    curs.close()
    con.commit()

def save_mention(tweet, hashtag, con):
    curs = con.cursor()
    query = None
    with open('queries/create_mention.sql', 'r') as myfile:
        query = myfile.read()
    curs.prepare(query)
    curs.execute(None, {
        "tid": tweet["tid"],
        "hashtag": hashtag
    })
    curs.close()
    con.commit()
