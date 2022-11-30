from errno import errorcode
import getpass, os
from signal import pause
from unicodedata import category
import mysql.connector as mysql
from mysql.connector import Error

class DATABASE:
    def __init__(self, user='root', pw='1234', host='localhost', db='egulf'):
        self.user = user
        self.password = pw
        self.host = host
        self.database = db
        self.sqlConn = mysql.connect(user=self.user, password=self.password, host=self.host, database=self.database)
        print("Connection Success")
    def exeQuery(self, q=''):
        dbConn=self.sqlConn
        #Executes given query
        try:
            self.cur = dbConn.cursor()
            self.query = q
            self.cur.execute(self.query)
            if ((self.cur != None) and (self.cur.fetchall() != None)): 
                self.res = self.cur.fetchall()
                self.cur.close()
                dbConn.commit()
                return self.res
            else:
                self.cur.close()
                dbConn.commit()
                return True
        except mysql.Error as err:
            print("Sorry there seems to be an error: {}".format(err))
    def closeConn(self):
        self.sqlConn.close()
