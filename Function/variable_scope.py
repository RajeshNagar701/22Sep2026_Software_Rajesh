"""
Python Variable Scope

In Python, we can declare variables in three different scopes: 

Local Variables
Global Variables
Nonlocal Variables

"""

# declare global variable
# message = 'Hello'

# def greet():
#     # declare local variable
#     print('Local', message)

# greet()
# print('Global', message)


"""
Python Nonlocal Variables

In Python, the nonlocal keyword is used within nested functions to 
indicate that a variable is not local to the inner function, 
but rather belongs to an enclosing function’s scope.

"""

# outside function 


message = 'global'                      # declare global variable
def outer():
    message = 'local'                   # declare local variable

    def inner():  # nested function  
        nonlocal message                # declare nonlocal variable
        message = 'nonlocal'  
        print("inner:", message)
    inner()
    print("outer:", message)

outer()



# inner: nonlocal
# outer: nonlocal

# Note : We have used the nonlocal keyword to modify the message variable 
# from the outer function within the nested function.