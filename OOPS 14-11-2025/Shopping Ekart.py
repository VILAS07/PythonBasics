class ShoppingCart:
    def __init__(self,CName):
        self.name=CName
        self.cart={}

    def add_item(self, item_name, price, quantity):
        if item_name in self.cart:
            self.cart[item_name]["quantity"] += quantity
        else:
            self.cart[item_name] = {"price": price, "quantity": quantity}
        print(f'{item_name} added successfully , Quantity : {quantity}')

    def remove_item(self,item_name):
        if item_name in self.cart:
            self.cart.pop(item_name)
            print(f'Removed {item_name} from cart')
        else:
            print('Item not found')

    def update_item(self, item_name, quantity):
        if item_name in self.cart:
            if quantity == 0:
                self.cart.pop(item_name)
                print(f"'{item_name}' removed because quantity was set to 0.")
            else:
                self.cart[item_name]["quantity"] = quantity
                print(f"Updated '{item_name}' quantity to {quantity}.")
        else:
            print(f"Item '{item_name}' not found in cart.")

    def calculate_total(self):
        for item, details in self.cart.items():
            price = details["price"]
            quantity = details["quantity"]
            total_price = price * quantity
            print(f"{item}: Total = {total_price}")


    def display_cart(self):
        print(self.cart)

    def empty_cart(self):
        self.cart.clear()

cart = ShoppingCart("Alice")

cart.add_item("Laptop", 60000, 1)
cart.add_item("Mouse", 500, 2)
cart.add_item("Keyboard", 1500, 1)

cart.display_cart()
print()
cart.update_item("Mouse", 1)
cart.remove_item("Keyboard")
cart.display_cart()
print()
cart.calculate_total()
# cart.empty_cart()
# cart.display_cart()












