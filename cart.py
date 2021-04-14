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
                for tmp_item in self.items:
                    if tmp_item[0] == item:
                        tmp_qty = tmp_item[1] + qty
                        if item.qty >= tmp_qty:
                            tmp_item[1] = tmp_qty
                            return
                self.items.append([item,qty])
            else:
                self.items = [[item,qty]]
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

    def update_cart_item(self, cart_id, qty):
        try:
            self.items[cart_id][1] = qty
        except:
            print("Could not update! Cart ID doesn't exist")

    def delete_cart_item(self, cart_id):
        try:
            self.items[cart_id][1] = 0
        except:
            print("Could not update! Cart ID doesn't exist")
    
    def buy_cart(self):
        for item in self.items:
            item[0].qty -= item[1]
        self.items = None
    
    def display_cart(self):
        i = 0 
        if self.items:
            for item in self.items:
                if item[1] != 0:
                    print("Cart index : " + str(i))
                    item[0].display_item()
                    print("Quantity added in cart : " + str(item[1]))
                i += 1
        else:
            print("---Empty cart---")
        print(str(i) + " items in cart!")

def exists_cart(user):
    if user in carts.keys():
        return True
    else:
        return False

def buy(user):
    if exists_cart(user) and check_address(user):
        cart = carts[user]
        if cart.check_cart():
            cart.buy_cart()
            return True
    return False

def new_cart(user):
    cart = Cart(user)
    carts[user] = cart

def display_cart(user):
    if exists_cart(user):
        cart = carts[user]
        cart.display_cart()

def is_empty_cart(user):
    if exists_cart(user):
        cart = carts[user]
        if cart.items:
            return False
        else:
            return True

def export_carts():
    carts_database = open("carts_database.txt","w")
    if carts:
        for cart in carts:
            temp_items = carts[cart].items
            if temp_items:
                for item in temp_items:
                    if item[1] == 0:
                        temp_items.remove(item)
                carts[cart].items = temp_items
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

def update_cart_item(user,cart_id,qty):
    carts[user].update_cart_item(cart_id,qty)

def delete_cart_item(user, cart_id):
    carts[user].delete_cart_item(cart_id)