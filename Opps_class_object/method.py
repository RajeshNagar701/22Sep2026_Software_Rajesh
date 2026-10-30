"""
Python Methods
We can also define a function inside a Python class. 
A Python function defined inside a class is called a method.

"""

# create a class
class Room:
    length = 0.0    # attribute
    breadth = 0.0
    
    # method to calculate area
    def calculate_area(self):
        print("Area of Room =", self.length * self.breadth)

study_room = Room()       # create object of Room class

study_room.length = 42.5  # assign values to all the properties 

study_room.calculate_area() # access method inside class





"""

All methods must have self as the first parameter. 

class Calculator:
  def add(self, a, b):
    return a + b

  def multiply(self, a, b):
    return a * b

calc = Calculator()
print(calc.add(5, 3))
print(calc.multiply(4, 7)) 


"""