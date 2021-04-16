from userTests import *
from itemTests import *
from cartTests import *

def startTest(done):
    while(1):
        print("Testing Menu")
        print("1. Test Users module")
        print("2. Test Carts module")
        print("3. Test Items module")
        print("4. Test all modules")
        print("5. Back")
        choice = int(input("Enter your choice (numeral) : "))
        if choice == 1:
            testUserModule(done)
            break
        elif choice == 2:
            testCartModule(done)
            break
        elif choice == 3:
            testItemModule(done)
            break
        elif choice == 4:
            testUserModule(done)
            testCartModule(done)
            testItemModule(done)
            break
        elif choice == 5:
            break
        else:
            print("Invalid option! Exiting")
            break

def testUserModule(done):
    testUserObjectCreation(done)
    testAuthorizeUser(done)

def testItemModule(done):
    testItemObjectCreation(done)
    testExistsProduct(done)
    testGetQuantity(done)
    testReturnItem(done)
    return

def testCartModule(done):
    return