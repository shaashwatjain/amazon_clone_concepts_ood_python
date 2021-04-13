from user import *
from item import *

carts = {}

# make functions private to avoid unauthorized access

class Cart:
    def __init__(self,user, items = None):
        self.user = user
        self.items = items
    
    def add_to_cart(self,item, qty=1):
        if item.qty >= qty:
            if self.items:
                self.items.append((item,qty))
            else:
                self.items = [(item,qty)]
        else:
            print("Quantity not available. Try reducing quantity !")

    def check_cart(self):
        # check for existing items if quantity available
        for item in self.items:
            if item[0].qty < item[1]:
                print('Item in cart is not available in quantity now!')
                item[0].display_item()
                print("Ordered quantity : "+ str(item[1]))
                print("Reduce quantity or delete product from cart!")
                return False
        return True

    def modify_cart(self):
        #modify quantity of item or delete item here
        pass
    
    def buy_cart(self):
        for item in self.items:
            item[0].qty -= item[1]
        self.items = None
    
    def display_cart(self):
        if self.items:
            for item in self.items:
                item[0].display_item()
                print("Quantity added in cart : " + str(item[1]))
        else:
            print("---Empty cart---")

def exists_cart(user):
    if user in carts.keys():
        return True
    else:
        return False

def buy(user):
    cart = return_cart(user)
    if cart.check_cart():
        cart.buy_cart()
        return True
    return False

def new_cart(user):
    cart = Cart(user)
    carts[user] = cart

def return_cart(user):
    if exists_cart(user):
        return carts[user]
    else:
        return None

def display_cart(user):
    cart = return_cart(user)
    cart.display_cart()

def is_empty_cart(user):
    if return_cart(user).items:
        return False
    else:
        return True

def export_carts():
    carts_database = open("carts_database.txt","w")
    for cart in carts:
        carts_database.write(cart + "\n")
        carts_database.write(json.dumps(carts[cart].items) + "\n")

def import_carts():
    carts_database = open("carts_database.txt","r")
    carts_data = carts_database.readlines()
    i = 0
    user = None
    for cart in carts_data:
        cart = cart.rstrip()
        if i == 1:
            carts[user] = Cart(user,json.loads(cart))
        else:
            user = cart
            i = 1