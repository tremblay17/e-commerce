'''
Defines methods related to users and admins
'''
from log_reg import *
from db_conn import *
from dataclasses import dataclass

class USER:
    def __init__(self, fname, lname, username, email, password, addr1='', addr2='', city='', state='', zip='', payment=''):
        self.fname = fname
        self.lname = lname
        self.username = username
        self.password = password
        self.email = email
        self.addr1 = addr1
        self.addr2 = addr2
        self.city = city
        self.state = state
        self.zip = zip
        self.payment = payment
        self.db = DATABASE()
            
    def logout(self):
        return True

    def getFName(self):
        return self.fname
    def getLName(self):
        return self.lname
    def getUName(self):
        return self.username
    def getEmail(self):
        return self.email
    def getPwd(self):
        return self.password
    def getAddr(self):
        return (self.addr1+' '+self.addr2+', '+self.city+', '+self.state+' '+self.zip)
    def getPayment(self):
        return self.payment
    def setInfo(self, info, newVal):
        match(info):
            case '1':
                self.fname = newVal
            case '2':
                self.lname = newVal
            case '3':
                self.username = newVal
            case '4':
                self.email = newVal
            case '5':
                self.password = newVal
            case '6':
                addr = newVal.split(', ')
                if len(addr) == 5:
                    self.addr1 = addr[0]
                    self.addr2 = addr[1]
                    self.city = addr[2]
                    self.state = addr[3]
                    self.zip = addr[4]
                else: 
                    self.addr1 = addr[0]
                    self.addr2 = ''
                    self.city = addr[1]
                    self.state = addr[2]
                    self.zip = addr[3]
            case '7':
                self.payment = newVal

    def editAccount(self, colVal='0=1', cond='0=1'): #Set Info
        colVal = colVal
        cond = cond
        res = self.db.exeQuery(f'UPDATE USERS SET {colVal} WHERE {cond};')
        return res

    def viewAccount(self, cols='*', cond='0=1'): #Get Info
        cols = cols
        cond = cond
        res = self.db.exeQuery(f'SELECT {cols} FROM USERS WHERE {cond};')
        return res
        

    def viewOrders(self, cols='*', cond='0=1'): #Get Orders
        cols = cols
        cond = cond
        res = self.db.exeQuery(f'SELECT {cols} FROM ORDERS WHERE {cond};')
        return res
                            
    def deleteAcct(self): #Deletes Acct
        self.db.exeQuery(f'DELETE FROM USERS WHERE uname = "{self.username}"; ')
        self.db.exeQuery(f'DELETE FROM CARTS WHERE uname = "{self.username}"; ')
        self.db.exeQuery(f'DELETE FROM ORDERS WHERE uname = "{self.username}"; ')
        return True
