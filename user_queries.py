import cx_Oracle
import time
def print_followers(followers):
    for f in followers:
        print("ID: "+str(f['usr']))
        print("Username: "+f['name'])
        print("Email: "+f['email'])
        print('********************************************')
        
def print_follower_details(details):
    print("User Information")
    print("ID: "+str(details['usr']))
    print("Name: "+details['name'])
    print("Number of followers: "+str(details['follower_count']))
    print("Number of followees: "+str(details['following_count']))
    print('********************************************')
        
        
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
    
def save_follow(flwer,flwee,con):
    start_date = cx_Oracle.DateFromTicks(time.time())
    run_post_query('create_follow',{"flwer":flwer,"flwee":flwee,"start_date":start_date},con)

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