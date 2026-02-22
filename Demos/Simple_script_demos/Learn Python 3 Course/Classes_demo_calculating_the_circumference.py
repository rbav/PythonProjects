#Introduction to object oriented programming
#This program is a demo for creating a class with two methods


class Circle:
  #Class variable
  pi = 3.14

  # method initiated for class
  # Saves an item as self each time its initiated
  # Uses the input diameter when called to calculate the radius
  def __init__(self, diameter):
    print("Creating circle with diameter {d}".format(d=diameter))
    self.radius = (diameter/2)

  # Method for calculating the circumference using the radius
  # Variables are passed from the method above to this method
  def circumference(self):
    return 2 * self.pi * self.radius
    
medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print("Medium Pizza Circumference is: ", medium_pizza.circumference())
print("Teaching table Circumference is: ", teaching_table.circumference())
print("Round room Circumference is: ", round_room.circumference())