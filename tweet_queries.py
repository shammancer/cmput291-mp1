import cx_Oracle

    
def get_user_tweets_curs(user,con):
    curs = con.cursor()
    query = None
    with open('queries/select_user_tweets.sql','r') as myfile:
        query = myfile.read()
    curs.prepare(query)
    curs.execute(None,{"usr":user})
    return curs


    
def get_next_tweets(curs, num):
    l = curs.fetchmany(numRows=num)
    tl = []
    if l == None:
        return None
    for e in l:
        tl.append(data2tweet(e))
    return tl

def get_follower_tweets_curs(u, con):
    curs = con.cursor()
    query = None
    with open('queries/select_follower_tweets.sql', 'r') as myfile:
        query = myfile.read() 
    curs.prepare(query)
    curs.execute(None, {"flwer": u["usr"]})
    return curs

def data2tweet(t):
    dataObject = {
        "tid": t[0],
        "writer": t[1],
        "tdate": t[2],
        "text": t[3]
    }
    if len(t) == 5:
        dataObject.update({"replyto":t[4]})
    return dataObject
        
def formatTweetDetails(t):
    return {
        "text" : t[0],
        "tid" : t[1],
        "replies": t[2],
        "retweets": t[3]
    }



    
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
    
def get_tweet_details(tid, con):
    curs = con.cursor()
    query = None
    with open('queries/get_tweet_details.sql', 'r') as myfile:
        query = myfile.read()
    curs.prepare(query)
    curs.execute(None, {"tid": tid})
    tdata = curs.fetchone()
    if tdata == None:
        return None
    return formatTweetDetails(tdata)
    
    
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

    
def save_tweet(t, con):
    run_post_query('create_tweet',t,con)
    
def save_hashtag(hashtag, con):
    run_post_query('create_hashtag',{"hashtag": hashtag},con)

def save_mention(tweet, hashtag, con):
    run_post_query('create_mention',{
        "tid": tweet["tid"],
        "hashtag": hashtag
    },con)
    
def save_retweet(t,con):
    run_post_query('create_retweet',{"tid":t["tid"], "rdate":t["rdate"],"usr":t["usr"]},con)

def run_post_query(queryName, bindings, con):
    curs = con.cursor()
    query = None
    with open('queries/'+queryName+'.sql', 'r') as myfile:
        query = myfile.read()
    curs.prepare(query)
    curs.execute(None,bindings)
    curs.close()
    con.commit()
       

