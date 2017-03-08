import cx_Oracle
import random
import getpass

import user_queries

def login(params, con):
    if len(params) != 1:
        print("Usage: login <usr(int)>")
        return (False, None)

    usr = None
    try:
        usr = int(params[0])
    except ValueError:
        print("The usr should be an Integer")
        return (False, None)

    
    pwd = getpass.getpass("password: ")
    u = user_queries.get_user(usr, con)
    if u is None:
        print("Invalid password or usr")
        return (False, None)
    elif u["pwd"].strip() != pwd.strip():
        print("Invalid password or usr")
        return (False, None)
    return (True, u)

def signup(con):
    user = {}
    print("You are now signing up")
    user["name"] = input("name: ")
    user["pwd"] = getpass.getpass("password: ")
    user["email"] = input("email: ")
    user["city"] = input("city: ")
    try:
        user["timezone"] = float(input("timezone: "))
    except ValueError:
        print("The timezone must be a float")
        return (False, None)
        
    got_usr = False
    while not got_usr:
        user["usr"] = random.randint(0, 2 ** 16)
        if user_queries.get_user(user["usr"], con) is None:
            got_usr = True

    user_queries.save_user(user, con)
            
    return (True, user)

def login_mode(con):
    s = input("Login: #> ")
    params = s.split(' ')
    cmd = params[0]
    del params[0]

    if cmd == "login":
        
        return login(params, con);    
    elif cmd == "signup":
        return signup(con)
    elif cmd == "help":
        print("Available commands: login, signup, exit, help")
        return (False, None)
    elif cmd == "exit":
        return (True, None)
    else:
        return (False, None)
