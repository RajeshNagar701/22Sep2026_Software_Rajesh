"""
Python Constructors
Earlier we assigned a default value to a class attribute,

The __init__() method is called automatically every time 
the class is being used to create a new object.

The constructor above initializes the value of the name attribute.
We have used the self.name to refer to the name attribute of the bike1 object.
If we use a constructor to initialize values inside a class, 
we need to pass the corresponding value during the object creation of the class.


# constructor function    
    
    def __init__(self, name = ""):
        self.name = name

"""

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# p1 = Person("Emil", 36)
# print(p1.name)
# print(p1.age)

#===================================================
"""
The self Parameter
The self parameter is a reference to the current instance of the class.

It is used to access properties and methods that belong to the class.
"""

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def greet(self):
    print("Hello, my name is " , self.name , "my age is" , self.age)

p1 = Person("Nagar", 25)
p1.greet()



#===================================================

#Without the __init__() method, you would need to set properties 
# manually for each object:


# class Person:
#   pass

# p1 = Person()
# p1.name = "Tobias"
# p1.age = 25

# print(p1.name)
# print(p1.age)