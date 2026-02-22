#Project Carly's Clippers
#Code by NOVA_TAGO
#Goal: To demonstrate for loops in Python 3 and how they can be used to perform actions on lists.

hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
#Creates a list of hairstyles

prices = [30, 25, 40, 20, 20, 35, 50, 35]
#creates a list of prices

last_week = [2, 3, 5, 8, 4, 4, 6, 2]
#creates a list of occurances of haircuts from the last week

total_price = 0
#creates a variable and sets it intial value to 0

for price in prices:
 total_price += price
 #For loop that goes through each price ammount in the list prices and adds it to the variable "total_price"

length = len(prices)
average_prices = total_price / length
#creates a variable "length" and measures how many entries are in the list "prices"
#gets the average price by dividing total_price by length
#saves it to the variable average_prices

print("Average Haircut Price:", "<", average_prices, ">")
#prints average prices from above code

new_prices = [price -5 for price in prices]
#prices in list "prices" were too expensive
#this code cuts costs of each by 5 and saves to list "new_prices"

print(new_prices)
#printes the list "new prices" to check if code above worked

total_revenue = 0
#creates a variable "total_revenue" and sets its intial value to 0

length_hairstyles = len(hairstyles)
#creates a variable and counts number of entries in hairstyles list from above

for i in range(length_hairstyles):
  num =  last_week[i] * prices[i]
  total_revenue += num
#for loop to go through the list for purchases last week and their corresponding prices and create the total revenue by multiplying each haircut by the number of times it was performed and adding it to the variable "total_revenue" 

print("Total Revenue:", "<", total_revenue, ">")
#prints the value saved under total revenue generated last week.

average_daily_revenue = total_revenue/7
print(average_daily_revenue)
#finds the average daily revenue by dividing the total_revenue variable by 7.

cuts_under_30 = []
for i in range(length_hairstyles):
  if prices[i] < 30:
    cuts_under_30.append(hairstyles[i])
print(cuts_under_30) 
#first creates an empty list named "cuts under 30"
#for loop that goes from 0 to the length of the list "hairstyles" using the varaible created "length_hairstyles" (0>7, traversing 8 spaces total)
#if statement looking only at the values of "i" that are below 30 from the list called "prices"
#adds the new value from the list "hairstyles" at value "i" to the list "cuts_under_30" using the append command at next entry
#prints the new list "cuts_under_30"
