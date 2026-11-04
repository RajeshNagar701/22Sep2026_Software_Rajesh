"""
Python Inheritance

Inheritance allows us to define a class that inherits 
all the methods and properties from another class.

Parent class is the class being inherited from, also called base class.

Child class is the class that inherits from another class, 
also called derived class.

There are 5 types of Inheritance

  1) Single Level,
  2) Multilevel Level
  3) Multiple 
  4) Hierarchical 
  5) Hybride


"""

# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)

# class Student(Person):
#   pass

# x = Student("Mike", "Olsen")
# x.printname()


"""
Add the __init__() function to the Student class:
When you add the __init__() function, the child class will 
no longer inherit the parent's __init__() function.

"""



class Person:
  def __init__(self, a, b):
    self.a = a
    self.b = b

  def sum(self):
    print(self.a + self.b)
    

class Student(Person):
  
  def __init__(self,a,b,c):
  
    super().__init__(a,b)
    self.c = c  # New child attribute
  
  def multi(self):
    print(self.a * self.b * self.c)
    

x = Student(10,5,3)
x.sum()
x.multi()