"""
Python Encapsulation

Encapsulation is about protecting data inside a class.
It means keeping data (properties) and methods together in a class, 
while controlling how the data can be accessed from outside the class.

This prevents accidental changes to your data and hides the internal details 
of how your class works.


Private Properties
In Python, you can make properties private by using a double underscore __ prefix:

"""


Create a private class property named __age:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age # Private property

p1 = Person("Emil", 25)
print(p1.name)
print(p1.__age) # This will cause an error

# Note: Private properties cannot be accessed directly from outside the class.


# Get Private Property Value
#Use a getter method to access a private property:

"""
class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age

  def get_age(self):
    return self.__age

p1 = Person("Tobias", 25)
print(p1.get_age())
"""