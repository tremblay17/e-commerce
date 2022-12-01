from log_reg import *
from db_conn import *
from dataclasses import dataclass
from inventory import *
  
class CART:
  
    def __init__ (self):
        self.db = DATABASE()
    
    def get_CartContents(self,username):
        #returns all items (and their quantities) in given user's CARTS
        res = self.db.exeQuery(f'SELECT itemId, itemName, itemQuantity FROM CARTS WHERE uname = "{username}";')
        return res
        
    def Remove_Item(self,username, itemID):
        #deletes selected item from given user's CARTS
        res = self.db.exeQuery(f'DELETE FROM CARTS WHERE itemID = "{itemID}" AND uname = "{username}";') 
    
    def get_TotalCost(self,username):
        #returns the combined cost of all items in CARTS belonging to the user
        res = self.db.exeQuery(f'SELECT SUM(itemPrice * itemQuantity) FROM CARTS WHERE uname = "{username}";')
        for i in res:
            for j in i:
                return j

    def Checkout(self,username):
        res = self.db.exeQuery(f'SELECT itemId FROM CARTS WHERE uname = "{username}";')
        for i in res:
            for j in i:
                self.db.exeQuery(f'UPDATE INVENTORY SET itemQuantity=itemQuantity-1 WHERE itemId = "{j}"')

        cart = CART()
        totalCost = cart.get_TotalCost(username)
        numItems = 0
        contents = cart.get_CartContents(username)
        for itemId, itemName, quantity in contents:
            numItems += quantity
        #adds an order
        self.db.exeQuery(f'INSERT INTO ORDERS (uname, numItems, subtotal) VALUES ("{username}","{numItems}","{totalCost}");')
        #deletes all of given user's items from CARTS
        self.db.exeQuery(f'DELETE FROM CARTS WHERE uname = "{username}";')
