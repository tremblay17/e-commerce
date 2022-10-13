from errno import errorcode
from pickle import TRUE
import getpass, os
from signal import pause
from unicodedata import category
import mysql.connector as mysql
from mysql.connector import Error

try:
    sqlConn = mysql.connect(user='root', password='', host='localhost', database='egulf_prod')
    print("Connection Success")
except mysql.Error as err:
    print(err)

class USER:
    def __init__(self):
        self.cur = sqlConn.cursor()
        self.query = ("")
        self.choice = ''

    def login(self, uname, pword): #move input and print to main function
        self.cur = sqlConn.cursor()
        self.loginQuery = ("SELECT uname, adminInd FROM users WHERE (uname = %s AND pword = %s)")

        try:
            self.cur.execute(self.loginQuery,(uname, pword))
            self.res = self.cur.fetchall()
            self.cur.close()
            return self.res
        except mysql.Error as err:
            print(err)

    def register(self, fname, lname, uname, email, pword):
        self.regQuery = ('INSERT INTO users (fname, lname, uname, email, pword) ' 
                        'VALUES (%s, %s, %s, %s, %s)') #fname, lname, uname, email, password
        self.loginQuery = ("SELECT uname, adminInd FROM users WHERE (uname = %s AND pword = %s)")
        
        try:
            self.cur.execute(self.regQuery,(fname, lname, uname, email, pword))
            sqlConn.commit()
            self.cur.close()
        except mysql.Error as err:
            print(err)
    
    def viewInStock(self): #move the input and print statements into main function
        self.cur = sqlConn.cursor()
        self.choice = input("You may view 'all' items or a 'category'\n")
        if(self.choice == 'category'):
            self.query("SELECT DISTINCT(category) FROM inventory")
            self.cur.execute(self.query)
            self.res = self.cur.fetchall()
            for row in self.res:
                print(row)
            self.choice = input('Please select a category: ')
            self.query = ("SELECT itemName, price FROM inventory WHERE (quantity > 0 AND category = %s)")
            self.cur.execute(self.query,[self.choice])
            self.res = self.cur.fetchall()
            self.cur.close()
            return self.res
        elif(self.choice == 'all'):
            self.query = ("SELECT itemName, price FROM inventory WHERE (quantity > 0)")
            self.cur.execute(self.query,[self.choice])
            self.res = self.cur.fetchall()
            self.cur.close()
            return self.res
        else:
            print('Choice Error')
    def searchInStock(self): #move the input and print statements into main function
        self.cur = sqlConn.cursor()
        self.search = input("Search For... ")
        self.query = ("SELECT itemName, price FROM inventory WHERE (itemName LIKE '%{self.search}%' AND quantity > 0)")
        self.cur.execute(self.query)
        self.res = self.cur.fetchall()
        self.cur.close()
        return self.res
    def viewInventory(self, choice, category):
        self.cur = sqlConn.cursor()
        if(choice == 'category'):
            self.query = ("SELECT DISTINCT(category) FROM inventory category")
            self.cur.execute(self.query)
            self.res = self.cur.fetchall()
            
            print('Categories: ', end='')
            for row in self.res:
                print(row, end=' ')
            print('\n')
            self.cat = category
            self.query = ("SELECT * FROM inventory WHERE (category = %s)")
            self.cur.execute(self.query,[self.cat])
            self.res = self.cur.fetchall()
            headers = [i[0] for i in self.cur.description]
            print(headers)
            self.cur.close()
            return self.res
        elif(choice == 'all'):
            self.query = ("SELECT * FROM inventory WHERE (1=1)")
            self.cur.execute(self.query)
            self.res = self.cur.fetchall()
            headers = [i[0] for i in self.cur.description]
            print(headers)
            self.cur.close()
            return self.res
        else:
            print('Choice Error')
    def searchInventory(self, searchParam):
        self.cur = sqlConn.cursor()
        item = '%'+searchParam+'%'
        self.query = ("SELECT * FROM inventory WHERE (itemName LIKE %s OR category = %s)")
        self.cur.execute(self.query,(item,searchParam))
        self.res = self.cur.fetchall()
        headers = [i[0] for i in self.cur.description]
        print(headers)
        self.cur.close()
        return self.res
    
    def viewUsers(self):
        self.cur = sqlConn.cursor()
        self.query = ("SELECT uname, email, fname, lname FROM users")
        self.cur.execute(self.query)
        self.res = self.cur.fetchall()
        headers = [i[0] for i in self.cur.description]
        print(headers)
        self.cur.close()
        return self.res
    def searchUsers(self, user):
        self.cur = sqlConn.cursor()
        self.query = ("SELECT uname, email, fname, lname FROM users WHERE (uname = %s OR fname = %s OR lname = %s)")
        self.cur.execute(self.query,(user,user,user))
        self.res = self.cur.fetchall()
        headers = [i[0] for i in self.cur.description]
        print(headers)
        self.cur.close()
        return self.res
    def viewAccount(self, user):
        self.cur = sqlConn.cursor()
        self.query = ("SELECT fname, lname, uname, email, pword, addressLine1, "
                    "addressLine2, city, state, zip, cardNo, expDate, ccv FROM users WHERE uname LIKE %s")
        self.cur.execute(self.query,[user])
        self.res = self.cur.fetchall()
        return self.res

    def logout(self):
        return True

    def viewOrders(self, orderID):
        self.cur = sqlConn.cursor()
        self.query = ("SELECT * FROM orders WHERE orderID LIKE %s")
        self.cur.execute(self.query, [orderID])
        self.res = self.cur.fetchall()
        headers = [i[0] for i in self.cur.description]
        print(headers)
        self.cur.close()
        return self.res

def menu(admin, uname, userObj):
    logout = False
    while(logout != True):
        os.system('clear')
        print("Welcome to eGulf {}!".format(uname))
        if(admin==1):
            print("Here are the menu options...\n"
                "0. Show Menu\n"
                "1. View Account\n"
                "2. Search Inventory\n"
                "3. View Inventory\n"
                "4. Search Users\n"
                "5. View Users\n"
                "6. View All Orders\n"
                "7. Logout")
            choice = int(input("Please make a selection..."))
            if(choice == 0):
                continue
            elif(choice == 1):
                os.system('clear')
                i = 0
                attr = ['First Name', 'Last Name', 'Username', 'Email', 
                        'Password', 'Addr1', 'Addr2', 'City', 'State', 
                        'Zip', 'Card No', 'Exp Date', 'CCV',]
                res = userObj.viewAccount(uname)
                print('Account Information: ')
                for row in res:
                    for col in row:
                        print(attr[i], col)
                        i+=1
                choice = int(input("Please make a selection..."))
            elif(choice == 2):
                os.system('clear')
                search = input("Search For... ")
                res = userObj.searchInventory(search)
                for row in res:
                    print(row)
                choice = int(input("Please make a selection..."))
            elif(choice == 3):
                os.system('clear')
                choice2 = input('Filter on category y/n? ')
                if choice2 == 'y':
                    category = input('Select a category... ')
                    res = userObj.viewInventory('category', category)
                else:
                    res = userObj.viewInventory('all', '')
                for row in res:
                    print(row)
                choice = int(input("Please make a selection..."))
            elif(choice == 4):
                os.system('clear')
                user = input("Search Users... ")
                res = userObj.searchUsers(user)
                for row in res:
                    print(row)
                choice = int(input("Please make a selection..."))
            elif(choice == 5):
                os.system('clear')
                res = userObj.viewUsers()
                print('Users: ')
                for row in res:
                    print(row)
                choice = int(input("Please make a selection..."))
            elif(choice == 6):
                os.system('clear')
                defaultVal = '%'
                print("List of Orders: ")
                orders = userObj.viewOrders(defaultVal)
                for row in orders:
                    print(row)
                choice = int(input("Please make a selection..."))
            elif(choice == 7):
                os.system('clear')
                logout = userObj.logout()
                break
            else:
                print('Choice Error')
        elif(admin==0):
            print("Here are the menu options...\n"
                "1. Search Items By Name\n"
                "2. Search Items By Category\n"
                "3. View Items In Stock\n"
                "4. View Account\n"
                "5. View Cart")

def main():
    exitProg = False
    userObj = USER()
    while(exitProg != True):
        loginReg = input("'exit'/'login'/'register' to access eGulf... ")
        if(loginReg == 'login'):
            os.system('clear')
            print('LOGIN:\n')
            uname = input('Username: ')
            pword = getpass.getpass('Password: ')
            info = userObj.login(uname, pword)
            for row in info:
                admin = row[1]
                uname = row[0]
            menu(admin, uname, userObj)
        elif(loginReg == 'register'):
            os.system('clear')
            print('Register:\n')
            fname = input('First Name: ')
            lname = input('Last Name: ')
            uname = input('Username: ')
            email = input('Email: ')
            pword = getpass.getpass('Password: ')
            userObj.register(fname, lname, uname, email, pword)
            info = userObj.login(uname, pword)
            for row in info:
                admin = row[1]
                uname = row[0]
            menu(admin, uname, userObj)
        else:
            return 0

if __name__ == '__main__':
    main()

'''
    
    def editAccount(user):
        cur = sqlConn.cursor()

        return 1
    
    def deleteAccount(user):
        cur = sqlConn.cursor()

        return TRUE        
    
    def viewInventoryDetails():
        cur = sqlConn.cursor()

        res = cur.fetchall()
        return res
    
    def viewAllOrders():
        cur = sqlConn.cursor()

        return 1
'''
'''    

    def addCart(user):
        cur = sqlConn.cursor()
        print('Added Item, %s, To Cart')

    def removeCart(user):
        cur = sqlConn.cursor()
        print('Removed Item, %s, From Cart')
    
    def emptyCart(user):
        cur = sqlConn.cursor()
        print('Cart Emptied')

    def viewCart(user):
        cur = sqlConn.cursor()
        print("Items in %s's Cart:\n".format(user))

    def checkout(user):
        cur = sqlConn.cursor()
'''