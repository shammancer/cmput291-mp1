import cx_Oracle
import time

def search_user(keyword,con):
    curs = con.cursor()
    query = None
    with open('queries/search_user.sql', 'r') as myfile:
        query = myfile.read()
    curs.prepare(query)
    curs.execute(None, {"keyword": "%"+keyword[0].strip()+"%"})
    return curs
    
def get_next_users(curs, num):
    l = curs.fetchmany(numRows=num)
    if l == None:
        return None
    return map(lambda t:{
        "usr": t[0],
        "pwd": t[1],
        "name": t[2],
        "email": t[3],
        "city": t[4],
        "timezone": t[5]
    },l)
    
def get_user(usr, con):
    curs = con.cursor()
    query = None
    with open('queries/select_user.sql', 'r') as myfile:
        query = myfile.read()
    curs.prepare(query)
    curs.execute(None, {"usr": usr})
    t = curs.fetchone()
    curs.close()
    if t == None:
        return None
    
    u = {
        "usr": t[0],
        "pwd": t[1],
        "name": t[2],
        "email": t[3],
        "city": t[4],
        "timezone": t[5]
    }

    return u
    
def get_follower_details(user,con):
    curs = con.cursor()
    query = None
    with open('queries/get_user_details.sql', 'r') as myfile:
        query = myfile.read()
    curs.prepare(query)
    curs.execute(None, {"usr": user})
    t = curs.fetchone()
    curs.close()
    if t == None:
        return None
    t = {
        "usr":t[0],
        "name" : t[1],
        "tweet_count":t[2],
        "follower_count":t[3],
        "following_count":t[4]
    }
    return t
    
def get_followers(user,con):
    curs = con.cursor()
    query = None
    with open('queries/select_followers.sql', 'r') as myfile:
        query = myfile.read()
    curs.prepare(query)
    curs.execute(None,{"usr":user})
    followers = curs.fetchall()
    curs.close()
    if followers == None:
        return None
    return map(lambda t:{
        "usr": t[0],
        "pwd": t[1],
        "name": t[2],
        "email": t[3],
        "city": t[4],
        "timezone": t[5]
    },followers)

def is_following(usr, flwer, con):
    curs = con.cursor()
    query = None
    with open('queries/select_follower.sql', 'r') as myfile:
        query = myfile.read()
    curs.prepare(query)
    curs.execute(None,{"usr":usr, "flwer": flwer})
    followers = curs.fetchall()
    curs.close()
    if followers == None:
        return False
    else:
        return True
           
def save_follow(flwer,flwee,con):
    start_date = cx_Oracle.DateFromTicks(time.time())
    run_post_query('create_follow',{"flwer":flwer,"flwee":flwee,"start_date":start_date},con)
    print("Follow successful!")

def save_user(u, con):
    run_post_query('create_user',u,con)
    
def run_post_query(queryName, bindings, con):
    curs = con.cursor()
    query = None
    with open('queries/'+queryName+'.sql', 'r') as myfile:
        query = myfile.read()
    curs.prepare(query)
    curs.execute(None,bindings)
    curs.close()
    con.commit()
