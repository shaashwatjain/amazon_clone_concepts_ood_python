from user import *
from item import *
from cart import *

def initialize():
    # Import for accounts
    try:
        import_database()
    except:
        print('No database for users detected!')
    # Import for items
    try:
        import_items()
    except:
        print('No items in the database! Nothing to sell!')
    try:
        import_carts()
    except:
        pass

current_user = None

def switch_main():
    while(1):
        print("Menu")
        print("1. Login")
        print("2. Register")
        print("3. Show all items")
        print("4. Search for item")
        print("5. Add to cart by item id")
        print("6. See cart")
        print("7. Manage items (Seller)")
        print("8. Log Out")
        choice = int(input("Enter your choice (numeral) : "))
        inner_choice = None
        if choice == 1:
            user = login()
            while not user:
                print("Invalid login!")
                inner_choice = int(input("Login again(1) or exit to main menu(0) : "))
                if inner_choice:
                    user = login()
                else:
                    break
            if not exists_cart(user):
                new_cart(user)
            print("Login successful!")
            current_user = user
        elif choice == 2:
            try:
                new_user()
            except:
                print("Invalid registration!")
                inner_choice = int(input("Register again(1) or exit to main menu(0) : "))
                if inner_choice:
                    new_user()
                else:
                    break
            else:
                print("Successful registration! You can login now")
        elif choice == 3:
            try:
                display_all()
            except:
                print("Problem loading items!")
        elif choice == 4:
            keyword = input("Enter keyword to search on : ")
            search_item(keyword)
        elif choice == 5:
            if current_user:
                item_id = int(input("Enter id of item to add : "))
                display_item_at_index(item_id)
                qty = int(input("Enter quantity of item to add : "))
                return_cart(current_user).add_to_cart(items[item_id], qty)
            else:
                print("Please login first!")
        elif choice == 6:
            if current_user:
                cart = return_cart(current_user)
                cart.display_cart()
            else:
                print("Please login first!")
        elif choice == 7:
            # manage items
            # only by seller
            # check if other functionality needed
            # require login
            switch_seller(current_user)
        elif choice == 8:
            current_user = None
        else:
            print("Invalid option!")

def switch_seller(current_user):
    while(1):
        print("1. View products being sold")
        print("2. Add new product")
        print("3. Manage product")
        print("0. Back to main menu")
        inner_choice = int(input("Enter your choice:"))
        if inner_choice == 1:
            # show products being sold by seller
            pass
        elif inner_choice == 2:
            try: 
                new_item(str(current_user))
            except:
                print("Error above explains the problem in adding product")
        elif inner_choice == 3:
            # manage product : delete, update
            pass
        elif inner_choice == 0:
            break
        else:
            print("Wrong input!")


def finalise():
    # all export commands
    pass
    
if __name__ == "__main__":
    initialize()
    switch_main()
    finalise()