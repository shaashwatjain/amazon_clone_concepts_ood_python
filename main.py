from user import *
from item import *

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



def switch_main():
    while(1):
        print("Menu")
        print("1. Login")
        print("2. Register")
        print("3. Show all items")
        print("4. Search for item")
        print("5. See cart")
        print("6. Manage items (Seller)")
        choice = int(input("Enter your choice (numeral) : "))
        if choice == 1:
            user = login()
            while not user:
                print("Invalid login !")
                inner_choice = int(input("Login again(1) or exit to main menu(0) : "))
                if inner_choice:
                    user = login()
                else:
                    break
        elif choice == 2:
            

    
if __name__ == "__main__":
    initialize()
