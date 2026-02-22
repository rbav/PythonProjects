# Your code below:
# Len's Slice project
#Goal: Learn about how to build and manipulate lists
# Code by Nova Tago

#list with topping ingredients
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

#list with prices for toppings
prices = [2, 6, 1, 3, 2, 7, 2]

#counts the number of times "2" shows up in the list prices and saves it to a variable
num_two_dollar_slices = prices.count(2)

#counts the length of the list "toppings"
num_pizzas = len(toppings)

#simple print command with string and variable from len
print("We sell ", num_pizzas, " different kinds of pizza!")

#creates a new 2D list manually from the data above
pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]
#prints the new 2D list
print(pizza_and_prices)

#sorts the 2D list with ascending prices
pizza_and_prices.sort()
print(pizza_and_prices)

#stores the first element in the sorted pizza_and_prices lists as a variable "cheapest_pizza"
cheapest_pizza = pizza_and_prices[0]

#stores the last element in the sorted pizza_and_prices list using the negative index methods
priciest_pizza = pizza_and_prices[-1]

#someone bought the last anchovie pizza and this command removes the last entry from the list
pizza_and_prices.pop(-1)

#adds a new 2D entry to the 2D list at a specific location
pizza_and_prices.insert(4, [2.5, "peppers"])
#print(pizza_and_prices) -> checks to see if done correctly

#slices the pizza_and_prices list to contain only the cheapest three options
three_cheapest = pizza_and_prices[0:3]
print(three_cheapest)
