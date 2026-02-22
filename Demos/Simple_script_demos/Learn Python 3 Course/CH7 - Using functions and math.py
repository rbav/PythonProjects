# CH 7 - Using functions and math in Python
# Goal: Getting use to writing functions and calling with different variables later
# Getting ready for Physics class

# Uncomment this when you reach the "Use the Force" section
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1


# Write your code below: 

#This function will take an input in Fahrenheit and convert it into a temperature in Celcius
#This one uses the print command spliced by commas (type I)
#return variable in separate line for later use
#If you don't return the variable within the function it cant be used anywhere else in the code
def f_to_c(f_temp):
  c_temp = ((f_temp - 32) * 5/9)
  print("answer", round(c_temp, 2), "input", round(f_temp, 2))
  return c_temp
f100_in_celcius  = f_to_c(100)

#This function will take an input in Celcius and convert it into a temperature in Fahrenheit
#This one uses the print command spliced by + signs (type II)
def c_to_f(c_temp):
  f_temp = c_temp *9/5 + 32
  print("answer " + str(round(f_temp, 2)), "input " + str(round(c_temp,2)))
  return f_temp
c0_in_fahrenheit = c_to_f(0)

#this function gets the value for force by multiplying the mass and the acceleration
#uses type I print statement
#returns the value for force to be used later on
def get_force(mass, acceleration):
  train_force = mass * acceleration
  print("The GE train supplies " + str(train_force) + " Newtons of force")
  return train_force
get_force(train_mass, train_acceleration)

#This function gets the value of energy by multiplying the mass times the speed of light squared (C^2)
def get_energy(mass, c = 3*(10**8)):
  bomb_energy = mass * c**2
  print("A 1kg bomb supplies " + str(bomb_energy) + " Joules")
get_energy(bomb_mass)

#This function gets the value of work by multiplying the force by the distance
#This function calls an earlier function "get_force" and saves its value to the variable "force"
def get_work(mass, acceleration, distance):
  force = get_force(mass, acceleration)
  return force * distance

#This line creates a variable "train_work" and calls the function "get_work" using the three variables provided at top
train_work = get_work(train_mass, train_acceleration, train_distance)

#This line prints the following statement using type II print
print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters")
