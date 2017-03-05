import getpass
import cx_Oracle
import json
import random

import mp1_login
import mp1_home

def help_cmd(params):
    print("Available commands: logout, exit, help")

def mp1(con):
    running = True

    
    print("Welcome to Harley's and Dannick's Miniproject")
    while running:
        logged_in = False
        while not logged_in:
            (logged_in, user) = mp1_login.login_mode(con)
            if logged_in is True and user is None:
                # exit sent from login_mode
                running = False
                break

        if running:
            running = mp1_home.home_mode(user, con)        

if __name__ == "__main__": 
    u = None
    s = None
    random.seed()
    with open('config.json') as data_file:    
        data = json.load(data_file)
        u = data["duser"]
        s = data["dpass"]

    try:
        con = cx_Oracle.connect(u, s, 'gwynne.cs.ualberta.ca:1521/CRS')
        mp1(con)
        con.commit();
        con.close();
    except cx_Oracle.DatabaseError as err:
        print(err)

