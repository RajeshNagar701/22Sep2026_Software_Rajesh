"""
Python Polymorphism

The word "polymorphism" means "many forms", and in programming it refers 
to methods/functions/operators with the same name that can be executed on 
many objects or classes.

Class Polymorphism
Polymorphism is often used in Class methods, where we can have multiple 
classes with the same method name.


"""
# Different classes with the same move() method:

class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object

for x in (car1, boat1):
  x.move()
  
  
 # Inheritance Class Polymorphism
 # What about classes with child classes with the same name? 
 #Can we use polymorphism there
 
class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object

for x in (car1, boat1):
  print(x.brand)
  print(x.model)
  x.move()
  
  
  
# You can use super() inside any overridden method to run the parent logic first 

# class Parent:
#     def greet(self):
#         return "Hello"

# class Child(Parent):
#     def greet(self):
#         # Call the parent's greet method and append more text
#         return super().greet() + ", welcome to the team!"

# c = Child()
# print(c.greet())  # Output: Hello, welcome to the team!
