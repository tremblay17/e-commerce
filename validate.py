'''
Defines the methods necessary to validate user info
'''
import re

def confirmPasswd(password, password2):
    if password2 == password:
        return True
    else: 
        return False

def validatePasswd(password):
    regex = r'^(?=.{6,15}$)(?:[0-9]+[A-Za-z]+[!@#$<>]|[0-9]+[!@#$<>]+[A-Za-z]|[A-Za-z]+[0-9]+[!@#$<>]|[A-Za-z]+[!@#$<>]+[0-9]|[!@#$<>]+[A-Za-z]+[0-9]|[!@#$<>]+[0-9]+[A-Za-z])([A-Za-z0-9!@#$<>]*)$'
    #Password must be between 6-15 charaters alphanumeric and symbols
    if(re.fullmatch(regex, password)):
        return True
    else:
        return False

def validateUname(username):
    regex = r'^(?=.{4,20}$)(?:[A-Za-z]+([A-Za-z0-9!@#$<>]+))$'
    #Username must be 4-20 characters that begin with a letter
    if(re.fullmatch(regex, username)):
        return True
    else:
        return False
            
def validateEmail(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if(re.fullmatch(regex, email)):
        return True
    else:
        return False

def validatePayment(cardNum):
    regex = r'^(?=.{16}$)(?:[0-9])([0-9]*)$'
    if(re.fullmatch(regex, cardNum)):
        return True
    else:
        return False


