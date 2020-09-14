stores = []
grocery_items = []

class Store:
    
    def __init__(self, title, address):
        self.store_name = title
        self.store_address = address
        self.grocery_items = []

class Grocery_Item:
    def __init__(self, title, quantity, price):
        self.title = list_item
        self.quantity = quantity
        self.price = price

def Shopping_List_Menu():
    while True:
        print("""
        1 = Quit
        2 = Add Store
        3 = Add Store Address
        4 = Add Grocery Item
        5 = Add Item Quantity
        6 = Add Price of Item
        7 = Print Shopping List
        """)
        user_input = input("Enter Menu Number: ")

        if user_input == "1":
            quit
        elif user_input == "2":
            Add_Store()
        elif user_input == "3":
            Add_Adress()
        elif user_input == "4":
            Add_Grocery_Item()
        elif user_input == "5":
            Add_Item_Quant()
        elif user_input == "6":
            Add_Item_Price()
        elif user_input == "7":
            Print_List()

def Add_Store():
    store_name = input("Enter store name: ")
    stores.append(store_name)

def Add_Adress():
    store_address = input("Enter store address: ")
    stores.append(store_address)

def Add_Grocery_Item():
    list_item = input("Add an item to your shopping list: ")
    grocery_items.append(list_item)

def Add_Item_Quant():
    quantity = input("Add item quantity: ")
    grocery_items.append(quantity)

def Add_Item_Price():
    price = int(input("Add price of item: $"))
    grocery_items.append(price)

def Print_List():
    message = f"My store to shop at is: {stores} and I am buying {grocery_items}."
    print(message)

Shopping_List_Menu()