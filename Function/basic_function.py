"""
Python Functions : block of code 

    1) User Define   , sum()
    2) Python Library Functions exa: len(),upper()

A function is a block of code that performs a specific task.


def greet():
    print('Hello World!')
greet()

"""


# 1) create basic function

# def greet():
#     print('Hello World!')
# greet()


# 2) create Arguments function
# def greet(name):
#     print("Hello", name)

# greet("John")  # call function with pass argument

# # function with two arguments
# def add_numbers(num1, num2):
#     sum = num1 + num2
#     print("Sum: ", sum)

# add_numbers(5, 4)  # function call with two values






 # 3) create return Statement function

# def find_square(num):
#     result = num * num
#     return result

# square = find_square(3)   # function call
# print('Square:', square)


# 4) Default Arguments in Functions
# def add_numbers( a = 7,  b = 8):
#     sum = a + b
#     print('Sum:', sum)

# add_numbers(2, 3)     # Sum: 5
# add_numbers(a = 2)    # Sum: 10  
# add_numbers()         # Sum: 15  


# 5) The pass Statement
# The pass statement serves as a placeholder for future code,
# preventing errors from empty code blocks.

# def future_function():
#     pass

# # this will execute without any action or error
# future_function()  




# 6) *args:  Python Function With Arbitrary Arguments


# Sometimes, we do not know in advance the number of arguments that will 
# be passed into a function. 
# To handle this kind of situation, we can use arbitrary arguments in Python.

# def find_sum(*numbers):
#     result = 0    
#     for num in numbers:
#         result = result + num
    
#     print("Sum = ", result)

# # function call with 3 arguments
# find_sum(1, 2, 3)                 # Sum =  6


# **kwargs  :  **kwargs allows multiple keyword arguments.


"""
7) Python Recursive Function

In Python, we know that a function can call other functions. 
It is even possible for the function to call itself. 
These types of construct are termed as recursive functions.

"""
# 5*4*3*2*1   
def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))
num = 5 
print("The factorial of", num, "is", factorial(num))


"""
8) lambda 

lambda function is a small, anonymous (unnamed) function that can take 
any number of arguments but can only have one single expression. 
The result of that expression is automatically returned without using a return keyword.

lambda arguments: expression

Lambda functions are most powerful when used inline as arguments for 
higher-order functions like map(), filter(), or sorted()


"""

# A lambda function that adds 10 to an argument

def sum(x):
    print(x+5)
    print(x*15)
sum(5)    

sum=lambda : 5+5
print(sum())


# # A lambda function with multiple arguments
# multiply = lambda a, b: a * b
# print(multiply(5, 6))  # Output: 30


#=============================================================