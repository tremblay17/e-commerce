'''
Defines methods for logging in and registering
'''
import mysql.connector as mysql
from db_conn import *
import validate as v

db = DATABASE()

def login(username, password):
    res = db.exeQuery(f'SELECT uname, password FROM USERS WHERE uname = "{username}" AND password = "{password}";')
    for i in res:
        for j in i:
            if username in j:
                if password in j:
                    return True
                else:
                    return 1
            else:
                return 1
            

def register(fname, lname, username, email, password, password2, addr1 = '', addr2 ='', city='', state='', zip='', payment=''):
    if(v.confirmPasswd(password, password2)):
        if(v.validatePasswd(password)):
            if(v.validateUname(username)):
                if(v.validateEmail(email)):
                    res = db.exeQuery(f'INSERT INTO USERS (fname, lname, uname, email, password, addr1, addr2, city, state, zip, cardNum) VALUES ("{fname}","{lname}","{username}","{email}","{password}", "{addr1}", "{addr2}", "{city}", "{state}", "{zip}", "{payment}");')
                    return True
                else:
                    error = 5 #Invalid email format
                    return error
            else:
                error = 4 #Invalid username format
                return error 
        else:
            error = 3 #Invalid password format
            return error
    else: 
        error = 2
        return error #Passwords don't match
