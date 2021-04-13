import getpass
import json

details = {}

class User:

    def __init__(self,username,password,name=None,address=None,phone=None,email=None):
        self.username = username
        self.password = password
        self.address = address
        self.name = name
        self.phone = phone
        self.email = email
    
    def change_details(self,name = None,address=None,phone=None,email=None):
        if address and address != "":
            self.address = address
        if name and name != "":
            self.name = name
        if phone and phone != "":
            self.phone = phone
        if email and email != "":
            self.email = email


def new_user():
    username = input("Enter your username : ")
    while username in details:
        print("Username already exists!")
        username = input("Enter your username : ")
    try:
        password = getpass.getpass()
    except Exception as error:
        print('ERROR', error)
    else:
        details[username] = User(username,password)

def export_database():
    user_database = open("user_database.txt","w")
    for user in details.keys():
        user_database.write(user + "\n")
        temp_user = details[user]
        user_details = [temp_user.password, temp_user.name, temp_user.address,temp_user.phone, temp_user.email]
        user_database.write(json.dumps(user_details) + "\n")
        

def import_database():
    user_database = open('user_database.txt','r').readlines()
    i = 0
    user_name = None
    for user in user_database:
        user = user.rstrip()
        if i == 1:
            print(user)
            user_details = json.loads(user)
            details[user_name] = User(user_name,user_details[0],user_details[1],user_details[2],user_details[3],user_details[4])
            user_name = None
            i = 0
        else:
            user_name = user
            i = 1
        


