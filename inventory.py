'''
Defines methods related to inventory
'''
from log_reg import *
from db_conn import *
from dataclasses import dataclass
from product import *

class INVENTORY:

    def __init__ (self):
        self.db = DATABASE()

    def addNewItem(self, itemName, itemQuantity, itemPrice):
        '''gets highest item id and increments by 1'''
        resSel = self.db.exeQuery('SELECT MAX(itemId) FROM INVENTORY')
        for (itemId) in resSel:
            self.itemIdNext = itemId + 1

        '''insertrs new item'''
        resIns = self.db.exeQuery('INSERT INTO INVENTORY (itemId, itemName, itemQuantity, itemPrice) ' 
                                            f'VALUES ("{self.itemIdNext}","{itemName}","{itemQuantity}","{itemPrice}");')

    def increaseInv(itemName, amount):
        item = PRODUCT(itemName)
        item.modQuant(amount)

    def decreaseInv(itemName, amount):
        item = PRODUCT(itemName)
        amount = amount * -1
        item.modQuant(amount)

    def GetInventory(self):
        res = self.db.exeQuery('SELECT * FROM INVENTORY;')
        return res

    def AddToCart(self, username, itemId, amount):
        resItem = self.db.exeQuery(f'SELECT itemName, itemPrice, itemQuantity FROM INVENTORY WHERE itemId="{itemId}";')
        for inm, ipr, iqt in resItem:
            itemName = inm
            itemPrice = ipr


        ##only inserts into cart if enough of the item is left
        if(iqt > amount):
            res = self.db.exeQuery('INSERT INTO CARTS (itemId, itemName, itemPrice, itemQuantity, uname) ' 
                f'VALUES ("{itemId}","{itemName}","{itemPrice}","{amount}","{username}");')
