import json

class Item:

    def __init__(self, item_name, item_des, item_price, item_qty, item_img, item_seller):
        str_type = type("")
        if(type(item_name) == str_type and type(item_des) == str_type):
            self.name = item_name
            self.description = item_des
            self.seller = item_seller
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
        final_qty = self.qty + change
        if(final_qty >= 0):
            self.qty = final_qty
        else:
            print('Quantity of item incorrect')

    def change_price(self,change):
        final_price = self.price - change
        if(final_price >= 0):
            self.price = final_price
        else:
            print('Price of item incorrect')

    def display_item(self):
        if self.qty != 0:
            print("#"*10)
            print("Item name : " + self.name)
            print("Item description : " + self.description)
            print("Item images can be viewed on the links : ")
            for image in self.images:
                print(image)
            print("Item price (in INR): " + str(self.price))
            print("Available quantity : " + str(self.qty))
            print("Seller : " + self.seller)
            print("#"*10)

items = []

def new_item(user):
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
    item = Item(name,description,price,quantity,images,user)
    items.append(item)

def export_items():
    data = open('database.txt','w')
    if items:
        for item in items:
            if item.qty != 0:
                data.write(item.name + "\n")
                data.write(item.description + "\n")
                data.write(str(item.price) + "\n")
                data.write(str(item.qty) + "\n")
                data.write(json.dumps(item.images) + "\n")
                data.write(item.seller + "\n")

def import_items():
    data = open('database.txt','r').readlines()
    i = 0
    item_data = []
    for line in data:
        line = line.rstrip()
        i += 1
        item_data.append(line)
        if(i == 6):
            item = Item(item_data[0],item_data[1],float(item_data[2]),int(item_data[3]),json.loads(item_data[4]), item_data[5])
            items.append(item)
            i = 0
            item_data = []

def display_all():
    i = 0
    if not items:
        print("No items to display!")
    for item in items:
        print("Item id : " + str(i))
        item.display_item()
        i += 1

def display_item_at_index(index):
    try:
        items[index].display_item()
    except:
        print("Invalid index.")
        return False
    return True

def search_item(keyword):
    i = 0
    found = 0
    for item in items:
        if keyword in item.name or keyword in item.description:
            print("Item id : " + str(i))
            item.display_item()
            found += 1
        i += 1
    print("Found " + str(found) + " products to display")

def products_by_seller(user):
    i = 0
    found = False
    for item in items:
        if item.seller == user and item.qty != 0:
            print("Item id : " + str(i))
            item.display_item()
            found = True
        i += 1
    if found == False:
        print("No items sold by user!")

def exists_prod(prod_id):
    if prod_id >= len(items):
        return False
    return True

def is_product_sold_by_user(prod_id, user):
    return items[prod_id].seller == user

def get_quantity(prod_id):
    return items[prod_id].qty

def get_price(prod_id):
    return items[prod_id].price

def change_quantity(prod_id, change):
    items[prod_id].change_quantity(change)

def change_price(prod_id, change):
    items[prod_id].change_price(change)

def delete_item(prod_id):
    items[prod_id].qty = 0

def return_item(prod_id):
    return items[prod_id]