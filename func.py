import json

# To implement : 
#       login
#       type of account
#       UI
#       Cart
#

class Item:

    def __init__(self, item_name, item_des, item_price, item_qty, item_img):
        str_type = type("")
        if(type(item_name) == str_type and type(item_des) == str_type):
            self.name = item_name
            self.description = item_des
        else:
            raise ValueError('Wrong Name or Description')
        if(item_qty >= 0):
            self.qty = item_qty
        else:
            raise ValueError('Quantity of item incorrect')
        if(item_price >= 0.0):
            self.price = item_price
        else:
            raise ValueError('Price of item incorrect')
        if(len(item_img) > 0):
            self.images = item_img
        else:
            raise ValueError('No images for product provided')

    def change_quantity(self,change):
        final_qty = self.qty - change
        if(final_qty >= 0):
            self.qty = final_qty
        else:
            raise ValueError('Quantity of item incorrect')

    def change_price(self,change):
        final_price = self.price - change
        if(final_price >= 0):
            self.price = final_price
        else:
            raise ValueError('Price of item incorrect')

    def display_item(self):
        print()

items = []

def new_item():
    name = input('Enter product name : ')
    description = input('Enter description : ')
    price = float(input('Enter price for product : '))
    quantity = int(input('Enter quantity : '))
    no_images = int(input('How many photos are you going to add (mandatory) : '))
    images = []
    while(no_images):
        image = input('Enter link : ')
        images.append(image)
        no_images -= 1
    item = Item(name,description,price,quantity,images)
    items.append(item)
    return item

def export_items():
    data = open('database.txt','w')
    for item in items:
        data.write(item.name + "\n")
        data.write(item.description + "\n")
        data.write(str(item.price) + "\n")
        data.write(str(item.qty) + "\n")
        data.write(json.dumps(item.images) + "\n")

def import_items():
    data = open('database.txt','r').readlines()
    i = 0
    item_data = []
    for line in data:
        line = line.rstrip()
        i += 1
        item_data.append(line)
        if(i == 5):
            item = Item(item_data[0],item_data[1],float(item_data[2]),int(item_data[3]),json.loads(item_data[4]))
            items.append(item)
            i = 0
            item_data = []


import_items()
print(items)