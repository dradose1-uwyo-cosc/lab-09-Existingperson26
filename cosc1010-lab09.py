# Peter Martinez
# UWYO COSC 1010
# 11/17/2024
# Lab 09
# Lab Section: 12
# Sources, people worked with, help given to: ChatGPT had to help me big time with accessing methods between classes and then fixing errors with the methods picking up things they weren't supposed to be
# Your
# Comments
# Here

# Classes
# For this assignment, you will be creating two classes:
# One for Pizza
# One for a Pizzeria


# You will be creating a Pizza class. It should have the following attributes:
# - Size
# - Sauce
# - Toppings, which should be a list
# You need to create one method that corresponds with each of the above attributes
# which returns the corresponding attribute, just the value.
# For the size and toppings attributes, you will need to have a method to set them.
# - For Size, ensure it is an int > 10 (inches)
#   - If it is not, default to a 10" pizza (you can store ten). These checks should occur in init as well.
# - For toppings, you will need to add the toppings.
#   - This method needs to be able to handle multiple values.
#   - Append all elements to the list.
# Create a method that returns the amount of toppings.
# In your __init__() method, you should take in size and sauce as parameters.
# - Sauce should have a default value of red.
# - Size will not have a default value; use the parameter with the same safety checks defined above (you can use the set method).
# Within __init__(), you will need to:
# - Assign the parameter for size to a size attribute.
# - Assign the parameter for sauce to the attribute.
# - Create the toppings attribute, starting off as a list only holding cheese.


# You will be creating a Pizzeria class with the following attributes:
# - orders, the number of orders placed. Should start at 0.
# - price_per_topping, a static value for the price per topping of 0.30.
# - price_per_inch, a static value of 0.60 to denote how much the pizza cost per inch of diameter.
# - pizzas, a list of all the pizzas with the last ordered being the last in the list.
# You will need the following methods:
# - __init__()
#   - This one does not need to take in any extra parameters.
#   - It should create and set the attributes defined above.
# - placeOrder():
#   - This method will allow a customer to order a pizza.
#     - Which will increment the number of orders.
#   - It will need to create a pizza object.
#   - You will need to prompt the user for:
#     - the size
#     - the sauce, tell the user if nothing is entered it will default to red sauce (check for an empty string).
#     - all the toppings the user wants, ending prompting on an empty string.
#     - Implementation of this is left to you; you can, for example:
#       - have a while loop and append new entries to a list
#       - have the user separate all toppings by a space and turn that into a list.
#   - Upon completion, create the pizza object and store it in the list.
# - getPrice()
#   - You will need to determine the price of the pizza.
#   - This will be (pizza.getSize() * price_per_inch) + pizza.getAmountOfToppings() * price_per_topping.
#   - You will have to retrieve the pizza from the pizza list.
# - getReceipt()
#   - Creates a receipt of the current pizza.
#   - Show the sauce, size, and toppings.
#   - Show the price for the size.
#   - The price for the toppings.
#   - The total price.
# - getNumberOfOrders()
#   - This will simply return the number of orders.


# - Declare your pizzeria object.
# - Enter a while loop to ask if the user wants to order a pizza.
# - Exit on the word `exit`.
# - Call the placeOrder() method with your class instance.
# - After the order is placed, call the getReceipt() method.
# - Repeat the loop as needed.
# - AFTER the loop, print how many orders were placed.

class Pizza:
    def __init__(self, size, sauce = 'Tomato'):
        self.size = size
        self.sauce = sauce
        self.toppings = ["Cheese"]
        
    def getSauce(self):
        return self.sauce

    def setSize(self, size):
        if self.size < 10:
            print("Your pizza is too small! Defaulting to 10 inches.")
            self.size = 10

    def getSize(self):
        return self.size

    def addToppings(self, toppings):
        for topping in toppings:
            self.toppings.append(topping)
    
    def getToppings(self):
        return self.toppings

    def amtToppings(self):
        return len(self.toppings)

class Pizzeria:
    def __init__(self, orders, topPrice, sizePrice, pizzas):
        self.orders = orders
        self.topPrice = topPrice
        self.sizePrice = sizePrice
        self.pizzas = pizzas
    def placeOrder(self):
        try:
            size = int(input("Please enter a size for your pizza that is greater than or equal to 10 inches: "))
            if size < 10:
                print("Your pizza is too small! Defaulting to 10 inches.")
                size = 10
        except ValueError:
            print("Invalid input! Defaulting to 10 inches.")
            size = 10 
        self.orders += 1
        newPizza = Pizza(size) 
        askSauce = input("Please input a sauce type for your pizza! Leave blank for Tomato sauce: ")
        if askSauce:
            newPizza.sauce = askSauce
        toppings = []
        active2 = True
        while active2:
            askTopping = input("Please input a topping for your pizza. Type 'Stop' to finish: ")
            if askTopping.lower() == "stop":
                active2 = False
                break
            else:
                toppings.append(askTopping)
        newPizza.addToppings(toppings)
        self.pizzas.append(newPizza)
    def getPrice(self, pizza):
        price = (pizza.getSize() * self.sizePrice) + (pizza.amtToppings() * self.topPrice)
        return price
    def getReceipt(self, pizza):
        print("Here is your pizza!")
        print(f"Size: {pizza.getSize()} inches\nSauce: {pizza.getSauce()}\n Toppings: {pizza.getToppings()}\n\nPrice for Size: ${(pizza.getSize() * self.sizePrice)}\nPrice for Toppings: ${pizza.amtToppings() * self.topPrice}\n\nTotal Price: ${self.getPrice(pizza)}")
    def getNumOrders(self):
        return self.orders



pizzaTime = Pizzeria(orders=0, topPrice=0.30, sizePrice=0.60, pizzas=[])
active = True
while active:
    askPizza = input("Would you like to order a pizza? Type 'Yes' to get started, and 'No' to stop the program.")
    if askPizza.lower() == "no":
        active = False
        break
    elif askPizza.lower() == "yes":
        pizzaTime.placeOrder()
        pizzaTime.getReceipt(pizzaTime.pizzas[-1])
    if askPizza.lower() != "yes" and askPizza.lower() != "no":
        print("Invalid input!")
        continue
print(f"Total pizzas ordered: {pizzaTime.getNumOrders()}. Thank you for ordering!")












# Example output:
"""
Would you like to place an order? exit to exit
yes
Please enter the size of pizza, as a whole number. The smallest size is 10
20
What kind of sauce would you like?
Leave blank for red sauce
garlic
Please enter the toppings you would like, leave blank when done
pepperoni
bacon

You ordered a 20" pizza with garlic sauce and the following toppings:
                                                                  cheese
                                                                  pepperoni
                                                                  bacon
You ordered a 20" pizza for 12.0
You had 3 topping(s) for $0.8999999999999999
Your total price is $12.9

Would you like to place an order? exit to exit
"""
