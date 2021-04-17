from user import *
from item import *
from cart import *
from test import *
from os import system

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

def switch_main(current_user):
    while(1):
        print("Menu")
        if (not current_user): print("1. Login")
        if (not current_user): print("2. Register")
        print("3. Show all items")
        print("4. Search for item")
        print("5. Add to cart by item id")
        print("6. Manage cart")
        print("7. Manage user")
        print("8. Manage items (Seller)")
        if (current_user): print("9. Log Out")
        print("10. Run tests")
        print("0. Exit")
        try:
            choice = int(input("Enter your choice (numeral) : "))
        except:
            print("Invalid choice. Try again.")
            continue
        inner_choice = None
        if choice == 1:
            if not current_user:
                user = login()
                while not user:
                    print("Invalid login!")
                    try:
                        inner_choice = int(input("Login again(1) or exit to main menu(0) : "))
                    except:
                        print("Invalid choice. Try again.")
                        continue
                    if inner_choice:
                        user = login()
                    else:
                        user = None
                        break
                if not user:
                    continue
                if not exists_cart(user):
                    new_cart(user)
                print("Login successful!")
                current_user = user
            else:
                print("Please log out first!")
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
                if not display_item_at_index(item_id):
                    continue
                qty = int(input("Enter quantity of item to add : "))
                if exists_cart(user):
                    cart = carts[user]
                    cart.add_to_cart(items[item_id], qty)
            else:
                print("Please login first!")
        elif choice == 6:
            # delete items from cart
            # Look for merging as : manage cart
            # Implement buy now as well 
            if current_user:
                display_cart(current_user)
                switch_cart(current_user)
            else:
                print("Please login first!")
        elif choice == 7:
            # edit details of user
            if current_user:
                print("1. Show details")
                print("2. Edit details")
                inner_choice = int(input("Enter choice : "))
                if inner_choice == 1:
                    show_details(current_user)
                elif inner_choice == 2:
                    print("Leave field blank if no update needed!")
                    inp_name = input("Enter full name :")
                    inp_address = input("Enter full address : ")
                    inp_phone = input("Enter phone number : ")
                    inp_email = input("Enter email address : ")
                    change_details(current_user, inp_name,inp_address,inp_phone, inp_email)
                else:
                    print("Invalid Option!")
            else:
                print("Login first!")
        elif choice == 8:
            # manage items
            # only by seller
            # check if other functionality needed
            # require login
            if current_user:
                switch_seller(current_user)
            else:
                print("Please login first !")
        elif choice == 9:
            current_user = None
            print("Logged out!")
        elif choice == 10:
            startTest(done)

            passedTestCases = 0
            for test in results:
                if test["status"]: passedTestCases += 1
                
            print()
            print("\x1b[32m" + str(passedTestCases) + " test cases passed out of " + str(len(results)) + "\x1b[0m.")
            print()

            if (passedTestCases != len(results)):
                print("\x1b[1m\x1b[35mReport of failed test cases:\x1b[0m")
                print()
                print("-"*25)
                print()

                print("Test status" + " "*10 + "Test")
                print()

                for test in results:
                    if not test["status"]:
                        print("\x1b[31mFailed\x1b[0m" + " \x1b[34m"*15 + test["message"] + "\x1b[0m")
                
                print()
                print("-"*25)
                print()
        elif choice == 0:
            print("Exiting!")
            break
        else:
            print("Invalid option!")
            continue

results = []

def done(passed, message):
    results.append({
        "status": passed,
        "message": message
    })

def switch_seller(current_user):
    while(1):
        print("1. View products being sold")
        print("2. Add new product")
        print("3. Manage product")
        print("0. Back to main menu")
        inner_choice = int(input("Enter your choice : "))
        if inner_choice == 1:
            try:
                products_by_seller(current_user)
            except:
                print("Internal Error!")
        elif inner_choice == 2:
            try: 
                new_item(current_user)
            except ValueError as err:
                print("Value Error: {0}".format(err))
                print("Error above explains the problem in adding product")
        elif inner_choice == 3:
            switch_manage_product(current_user)
        elif inner_choice == 0:
            break
        else:
            print("Wrong input!")

def switch_manage_product(user):
    # Add user auth
    prod_id = int(input("Enter product id : "))
    if exists_prod(prod_id):
        print("#"*10)
        print("1. Update quantity")
        print("2. Delete item")
        in_choice = int(input("Enter choice : "))
        if in_choice == 1:
            old_quantity = get_quantity(prod_id)
            print("Current Quantity : " + str(old_quantity))
            new_quantity = int(input("Enter new quantity : "))
            update_quantity = new_quantity - old_quantity
            change_quantity(prod_id, update_quantity)
        elif in_choice == 2:
            delete_item(prod_id)
    else:
        print("Product id does not exist")

def switch_cart(user):
    print("1. Update item in cart by id")
    print("2. Delete item in cart by id")
    print("3. Buy Cart")
    in_choice = int(input("Enter choice : "))
    if in_choice == 1:
        prod_id = int(input("Enter cart id to update : "))
        update_qty = int(input("Enter update quantity : "))
        update_cart_item(user, prod_id, update_qty)
    elif in_choice == 2:
        prod_id = int(input("Enter item id to delete : "))
        delete_cart_item(user, prod_id)
    elif in_choice == 3:
        if not is_empty_cart(user):
            buy(user)
        else:
            print("Cart is empty!")
    else:
        print("Invalid input!")

def finalise():
    export_database()
    export_items()
    export_carts()
    
if __name__ == "__main__":
    current_user = None
    initialize()
    switch_main(current_user)
    finalise()