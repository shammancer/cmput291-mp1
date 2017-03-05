import cx_Oracle

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

def save_user(u, con):
    curs = con.cursor()
    query = None
    with open('queries/create_user.sql', 'r') as myfile:
        query = myfile.read()
    curs.prepare(query)
    curs.execute(None, u)
    curs.close()
    con.commit()
