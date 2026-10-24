"""
Python Global Keyword
In Python, the global keyword allows us to modify the variable outside of the current scope.

It is used to create a global variable and make changes to the variable in a local context.

Rules of global Keyword
The basic rules for global keyword in Python are:

When we create a variable inside a function, it is local by default.
When we define a variable outside of a function, it is global by default. You don't have to use the global keyword.
We use the global keyword to modify (write to) a global variable inside a function.
Use of the global keyword outside a function has no effect.

"""

#Changing Global Variable From Inside a Function using global


c = 1         # global variable
def add():
    global c  # use of global keyword
    c = c + 2 
    print(c)
add()         # Output: 3 
