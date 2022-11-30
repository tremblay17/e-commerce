from log_reg import *
from db_conn import *
from dataclasses import dataclass
from inventory import *
  
class CART:
  
    def __init__ (self):
        self.db = DATABASE()
    
    def get_CartContents(self,username):
        #returns all items (and their quantities) in given user's cart
        res = self.db.exeQuery(f'SELECT itemID, quantity_in_cart FROM CARTS WHERE uname = "{username}";')
        return res
        
    def Remove_Item(self,username, itemID):
        #deletes selected item from given user's cart
        res = self.db.exeQuery(f'DELETE FROM CARTS WHERE itemID = "{itemID}" AND uname = "{username}";') 
    
    def get_TotalCost(self,username):
        #returns the combined cost of all items in CART belonging to the user
        res = self.db.exeQuery(f'SELECT SUM(item_price * quantity_in_cart) FROM CARTS WHERE uname = "{username}";')
        return res

    def Checkout(self,username):
        #decreases inventory stock by amount of given items in user's cart  
        res1 = self.db.exeQuery(f'UPDATE INVENTORY JOIN CARTS ON INVENTORY.itemID = CARTS.itemID SET INVENTORY.quantity = INVENTORY.quantity - CARTS.quantity_in_cart WHERE CARTS.uname = "{username}";')

        cart = CART()
        totalCost = cart.get_TotalCost(username)
        numItems = 0
        contents = cart.get_CartContents(username)
        for itemId, quantity in contents:
            numItems += quantity
        #adds an order
        res3 = self.db.exeQuery(f'INSERT INTO ORDERS (uname, numItems, subtotal) VALUES ("{username}","{numItems}","{totalCost}");')
        #deletes all of given user's items from CART
        res2 = self.db.exeQuery(f'DELETE FROM CARTS WHERE uname = "{username}";')
