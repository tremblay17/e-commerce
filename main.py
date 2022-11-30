from user import *
from log_reg import *
import validate as v
from cart import *
from inventory import *
from product import *

def displayLogin():
    choice = input("\nChoose login or register or exit: ")
    if choice == 'login':
        print("Login ")
        username = input("Username: ")
        passwd = input("Password: ")
        fname, lname, uname, email, password, addr1, addr2, city, state, zip, payment = '','','','','','','','','','',''
        auth = login(username, passwd)
        if(auth):
            res = db.exeQuery(f"SELECT * FROM USERS WHERE uname='{username}' AND password='{passwd}';")
            for i in res:
                print(i)
                for j in i:
                    fname=i[0]
                    lname=i[1]
                    uname=i[2]
                    email=i[3]
                    password=i[4]
                    addr1=i[5]
                    addr2=i[6]
                    city=i[7]
                    state=i[8]
                    zip=i[9]
                    payment=i[10]
                    break
            return USER(fname, lname, uname, email, password, addr1, addr2, city, state, zip, payment)
        else:
            print('Login Error - username or password incorrect')
    elif choice == 'register':
        print("Register ")
        fname = input('First Name: ')
        lname = input('Last Name: ')
        username = input('Username: ')
        email = input('Email: ')
        password = input('Password: ')
        confirmPwd = input('Confirm Password: ')
        auth = register(fname, lname, username, email, password, confirmPwd)
        if(auth):
            return USER(fname, lname, username, email, password)
        else:
            match(auth):
                case 2:
                    print('Passwords Do Not Match', auth)
                case 3:
                    print('Invalid Password', auth)
                case 4:
                    print('Invalid Username', auth)
                case 5:
                    print('Invalid Email', auth)
                case _:
                    print('Registration Error', auth)
            return auth
    elif choice == 'exit':
        return 'exit'
    else:
        print('Input Error')

def displayAccountInfo(user):
    fname=user.getFName()
    lname=user.getLName()
    uname=user.getUName()
    email=user.getEmail()
    password=user.getPwd()
    addr=user.getAddr()
    payment=user.getPayment()
    print(f'Account Info of {uname}: ')
    print(f'1: {fname}')
    print(f'2: {lname}')
    print(f'3: {uname}')
    print(f'4: {email}')
    print(f'5: {password}')
    print(f'6: {addr}')
    print(f'7: {payment}')
    choice = input('You may select what you want to edit: ')
    match (choice):
        case '1':
            newInfo = input('Enter your first name: ')
            user.setInfo(choice, newInfo)
            user.editAccount(colVal=f'fname = "{newInfo}"', cond=f'uname = "{user.getUName()}" OR email = "{user.getEmail()}"')
        case '2':
            newInfo = input('Enter your last name: ')
            user.setInfo(choice, newInfo)
            user.editAccount(colVal=f'lname = "{newInfo}"', cond=f'uname = "{user.getUName()}" OR email = "{user.getEmail()}"')
        case '3':
            newInfo = input('Enter your username: ')
            if(v.validateUname(newInfo)):
                user.setInfo(choice, newInfo)
                user.editAccount(colVal=f'uname = "{newInfo}"', cond=f'uname = "{user.getUName()}" OR email = "{user.getEmail()}"')
            else:
                print('Invalid Username')
        case '4':
            newInfo = input('Enter your email: ')
            if(v.validateEmail(newInfo)):
                user.setInfo(choice, newInfo)
                user.editAccount(colVal=f'email = "{newInfo}"', cond=f'uname = "{user.getUName()}" OR email = "{user.getEmail()}"')
            else:
                print('Invalid Email')
        case '5':
            newInfo = input('Enter your new password: ')
            confPw = input('Confirm your password: ')
            if (v.confirmPasswd(newInfo, confPw)):
                user.setInfo(choice, newInfo)
                user.editAccount(colVal=f'password = "{newInfo}"', cond=f'uname = "{user.getUName()}" OR email = "{user.getEmail()}"')
            else: 
                print("Error Passwords Don't Match")
        case '6':
            newInfoLi = []
            newInfo = input('Enter your house number and street: ')
            newInfoLi.append(newInfo)
            newInfo = input("Enter your apt number if applicable or 'na': ")
            if newInfo == 'na':
                pass
            else:
                newInfoLi.append(newInfo)
            newInfo = input('Enter your city: ')
            newInfoLi.append(newInfo)
            newInfo = input('Enter your state: ')
            newInfoLi.append(newInfo)
            newInfo = input('Enter your zip code: ')
            newInfoLi.append(newInfo)
            newInfo = ', '.join(newInfoLi)
            user.setInfo(choice, newInfo)
            user.editAccount(colVal=f'addr1="{newInfoLi[0]}", addr2 ="{newInfoLi[1]}", city="{newInfoLi[2]}", state="{newInfoLi[3]}", zip="{newInfoLi[4]}"', cond=f'uname = "{user.getUName()}" OR email = "{user.getEmail()}"')
        case '7':
            newInfo = input('Enter your card number: ')
            if(v.validatePayment(newInfo)):
                user.setInfo(choice, newInfo)
                user.editAccount(colVal=f'payment = "{newInfo}"', cond=f'uname = "{user.getUName()}" OR email = "{user.getEmail()}"')
            else:
                print('Invalid Card Number')
        case _:
            print('Invalid Input')

def displayOrderInfo(user):
    print(f'Orders of {user.getUName()}: ')
    #Call View Orders Method
    ords = user.viewOrders(cols='orderId, numItems', cond=f'uname = "{user.getUName()}"')
    for i in range(len(ords)):
        for j in i:
            print(j, sep=' ')
    choice = input('You may select Order ID you want to view(n to skip): ')
    if choice != 'n':
        ords = user.viewOrders(cond=f'uname = "{user.getUName()}" AND orderID = "{choice}"')
        for i in ords:
            for j in i:
                print(j, sep=' ')

def displayInventory(user):
    inv = INVENTORY()
    itemList = inv.GetInventory()
    for item in itemList:
        for val in item:
            print(val, sep=' ')
    choice = input('You may select an ID to add it to your cart(n to skip): ')
    while(choice != 'n'):
        try:
            inv.AddToCart(user.getUName(), choice, 1)
        except:
            print("Id not found, please try again.")
        choice = input('Item added to cart. You may select another ID to add it to your cart(n to skip): ')
    
def displayCart(user):
    cart = CART()
    itemList = cart.get_CartContents(user.getUName())
    for item in itemList:
        for val in item:
            print(val, sep=' ')
    choice = input('You may select c to checkout, or select an ID to remove it from your cart(n to skip): ')
    while(choice != 'n'):
        if choice == 'c':
            cart.CheckOut(user.getUName())
            print("Checkout complete. Check your orders for more info. Returning to main menu.")
            choice = 'n'
        else:
            try:
                cart.Remove_Item(user.getUName(), choice,)
                itemList = cart.get_CartContents(user.getUName())
                for item in itemList:
                    for val in item:
                        print(val, sep=' ')
            except:
                print("ID not found, please try again.")
            choice = input('You may select c to checkout, or you may select another ID to remove from your cart(n to skip): ')



def displayUserMenu():
    exitInd = False
    while exitInd == False:
        user = displayLogin()
        if user == False:
            print('Authentication Error')
        elif isinstance(user, USER):
            os.system('clear')
            logoutInd = False
            while logoutInd == False:
                #os.system('clear')
                print('\n')
                print(f"Welcome to eGulf! {user.getUName()}\n")
                choice = (input('Please Choose One: \n'
                        '1: View Inventory\n'
                        '2: View My Cart\n' 
                        '3: View Account Info\n' #Calls Display Method
                        '4: View Orders\n' #Calls Display Method
                        '5: Logout\n' #Call Logout Method
                        '6: Delete Account\n' #Call Delete Acct Method
                        'Choice: '))
                match (choice):
                    case '1':
                        os.system('clear')
                        try:
                            displayInventory(user)
                        except:
                            continue
                    case '2':
                        os.system('clear')
                        try:
                            displayCart(user)
                        except:
                            continue
                    case '3':
                        os.system('clear')
                        try:
                            displayAccountInfo(user)
                        except:
                            continue
                    case '4':
                        os.system('clear')
                        try: 
                            displayOrderInfo(user)
                        except:
                            continue
                    case '5':
                        os.system('clear')
                        print('Logging Out...')
                        logoutInd = user.logout()
                    case '6':
                        os.system('clear')
                        try:
                            user.deleteAcct()
                            logoutInd = user.logout()
                        except:
                            continue
                    case _:
                        os.system('clear')
                        print('Choice is Invalid')
        elif user == 'exit':
            exitInd = True
        else:
            print('Unkown Error')
            continue
    os.system('clear')
    print('Exiting...')

def main():
    displayUserMenu()

if __name__ == '__main__':
    main()