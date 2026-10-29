"""
Python Classes/Objects

Python is an object oriented programming language.
Almost everything in Python is an object, with its properties and methods.

Create a Class
To create a class, use the keyword class:

1) Create a Class : To create a class, use the keyword class:

class MyClass:   # this class
  x = 5

p1 = MyClass()   # this object & we can access class properties by object
print(p1.x) 

2) del p1

3) create multiple object of 1 class

p1 = MyClass()
p2 = MyClass()
p3 = MyClass()


4) The pass Statement

class Person:
  pass
  
"""

class Parrot:           # create class

    name = ""           # class attribute
    age = 18

parrot1 = Parrot()      # create parrot1 object
parrot1.name = "Blu"

print(f"{parrot1.name} is {parrot1.age} years old")  # access attributes



