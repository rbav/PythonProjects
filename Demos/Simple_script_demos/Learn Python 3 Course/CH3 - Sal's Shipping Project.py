# CH3 - Sal's Shipping Project
# Another project to learn if statements to sort options
## Project Shipping
## Code by NOVA_TAGO
## Educational Purpose
## Weight of package and determine cheapest ship

weight = 41.5
method = 'premium'

if method == 'ground':
  print ("You have selected 'ground' shipping")
  print ("Flat charge = $20.00")
elif method == 'premium':
  print ("You have selected 'premium' shipping")
  print ("Premium = $125.00")
elif method == 'drone':
  print ("You have selected 'drone' shipping")
  print ("Flat charge = $0.00")
else:
  print ("please select proper method")

## Ground shipping
## Price per pound
a = 1.50
b = 3.00
c = 4.00
d = 4.75
e = 0.00
f = 4.50
g = 9.00
h = 12.00
i = 14.25

if method == 'ground' and weight <= 2:
  flat = 20.00
  package = a
elif method == 'ground' and weight > 2 and weight <= 6:
  flat = 20.00
  package = b
elif method == 'ground' and weight > 6 and weight <= 10:
  flat = 20.00
  package = c
elif method == 'ground' and weight > 10:
  flat = 20.00
  package = d
elif method == 'premium':
  flat = 125.00
  package = e
elif method == 'drone' and weight <= 2:
  flat = 0.00
  package = f
elif method == 'drone' and weight > 2 and weight <= 6:
  flat = 0.00
  package = g
elif method == 'drone' and weight > 6 and weight <= 10:
  flat = 0.00
  package = h
elif method == 'drone' and weight > 10:
  flat = 0.00
  package = i
else:
  print("Error")

if package == a:
  price = flat + (weight * a)
elif package == b:
  price = flat + (weight * b)
elif package == c:
  price = flat + (weight * c)
elif package == d:
  price = flat + (weight * d)
elif package == e:
  price = flat + (weight * e)
elif package == f:
  price = flat + (weight * f)
elif package == g:
  price = flat + (weight * g)
elif package == h:
  price = flat + (weight * h)
elif package == i:
  price = flat + (weight * i)
else:
  print ("Error 2")

print ("Your total is $", price)