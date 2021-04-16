from item import exists_prod, get_quantity, return_item

def testItemObjectCreation(done):
    # Test required fields of Item object
    try:
        newUser = Item("soap", "Body soap")
        done(False, "Item object is being created regardless of not providing required values")
    except:
        done(True, "Item object is only created if all the required parameters are passed")
    
    # Test if qty field doesn't accept values other than those of type integer
    try:
        newUser = Item("soap", "Body soap", 100, "ten", "https://www.google.com/imgres?imgurl=https%3A%2F%2F5.imimg.com%2Fdata5%2FLW%2FGN%2FMY-4990337%2Fbath-soap-500x500.jpg&imgrefurl=https%3A%2F%2Fwww.indiamart.com%2Fproddetail%2Fsky-blue-bath-soap-13275191933.html&tbnid=Eq3_rxZQXd-njM&vet=12ahUKEwjDme2_5YLwAhV-wAIHHZ0dBMYQMygAegUIARDmAQ..i&docid=_U7R6efWbgmkeM&w=500&h=500&q=soap&ved=2ahUKEwjDme2_5YLwAhV-wAIHHZ0dBMYQMygAegUIARDmAQ", "test")
        done(False, "Item object is being created with sting value for quantity values")
    except:
        done(True, "Item object doesn't accept string values as input as expected")
    
def testExistsProduct(done):
    if (exists_prod(9)):
        done(False, "exists_prod return true for a product that doesn't exist")
    else:
        done(True, "exists_prod returns true for a product that doesn't exist")

def testGetQuantity(done):
    if (isinstance(get_quantity(0), int)):
        done(True, "get_quantity returns integer value")
    else:
        done(False, "get_quantity is returning non integer values")

def testReturnItem(done):
    if (isinstance(return_item(0), object)):
        done(True, "return_item returns item object")
    else:
        done(False, "return item is returning invalid values")