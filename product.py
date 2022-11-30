'''
Defines methods related to products
class used for storing products
'''
from log_reg import *
from db_conn import *
from dataclasses import dataclass

'''this code works assuming itemName is an alternate key.'''
class PRODUCT:

    def __init__(self, name=''):
        self.name = name
        self.db = DATABASE()

    '''adds or subtracts from quantity based on input of mod. positive for addition, negative for subtraction'''
    def modQuant(self, mod):

        res1 = self.db.exeQuery(f'SELECT itemQuantity FROM INVENTORY WHERE itemName={self.name};')
        for itemQuantity in res1:
            self.quantity = 0 + itemQuantity



        self.quantity += mod
        res2 = self.db.exeQuery(f'UPDATE INVENTORY SET {self.quantity} WHERE itemName={self.name};')
        

        
