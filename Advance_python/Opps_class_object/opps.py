"""

Python Object Oriented Programming

Python is a versatile programming language that supports various programming styles,
including object-oriented programming (OOP) through the use of objects and classes.

Class	    Objects
Fruit	    Apple, Banana, Mango
Car	        Volvo, Audi, Toyota


Advantages of OOP

Provides a clear structure to programs
Makes code easier to maintain, reuse, and debug
Helps keep your code DRY (Don't Repeat Yourself)
Allows you to build reusable applications with less code & time
opps provide securities

class           block of code by class keyword
object          instance of class
Encapsulation
Inheritance
polymorphism
abtraction

"""

# def sum():
#     a=20
#     b=20  
#     print(a+b)
# sum()

# def multi():
#     a=20
#     b=20
#     print(a*b)
# multi()


class abc:     # class declation by class keyword
    
    a=10       # class variable declation
    b=20
    
    def sum(self):         # class method
        print(self.a+self.b)
   
    def multi(self):
        print(self.a*self.b)

obj = abc() # create object of class
obj.sum()
obj.multi();

print(obj.a)