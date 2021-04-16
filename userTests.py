from user import authorize_user

def testUserObjectCreation(done):
    # Test Username
    try:
        newUser = User(None, "password")
        done(False, "User object is accepting None value as username")
    except:
        done(True, "User object is able to sanity check username field")

    # Test Password
    try:
        newUser = User("test", None)
        done(False, "User object is accepting None value as password")
    except:
        done(True, "User object is able to sanity check password field")

def testAuthorizeUser(done):
    # Test return value
    if (authorize_user("test", "test")):
        done(True, "authorize_user is working as expected")
    else:
        done(False, "authorize_user is not accepting correct credentials")
