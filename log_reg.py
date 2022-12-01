'''
Defines methods for logging in and registering
'''
import mysql.connector as mysql
from db_conn import *
import validate as v

db = DATABASE()

def login(username, password):
    res = db.exeQuery(f'SELECT uname, password FROM USERS WHERE uname = "{username}" AND password = "{password}";')
    if len(res) != 0:
        return 1
    return 2


    #if res:
    #    return 1
    #else:
    #   for i in res:
    #       for j in i:
    #           if username in j:
    #                if password in j:
    #                    print("user found")
    #                    return True
    #                else:
    #                    return 1
    #            else:
     #               return 1
            

def register(fname, lname, username, email, password, password2, addr1 = '', addr2 ='', city='', state='', zip='', payment=''):
    if(v.confirmPasswd(password, password2)):
        if(v.validatePasswd(password)):
            if(v.validateUname(username)):
                if(v.validateEmail(email)):
                    db.exeQuery(f'INSERT INTO USERS (fname, lname, uname, email, password, addr1, addr2, city, state, zip, cardNum) VALUES ("{fname}","{lname}","{username}","{email}","{password}", "{addr1}", "{addr2}", "{city}", "{state}", "{zip}", "{payment}");')
                    return 1
                else:
                    #Invalid email format
                    return 5
            else:
                #Invalid username format
                return 4 
        else:
            #Invalid password format
            return 3
    else: 
        return 2 #Passwords don't match
