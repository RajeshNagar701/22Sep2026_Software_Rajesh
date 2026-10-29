"""
Python Exceptions :
An exception is an unexpected event that occurs during program execution.

Python Logical Errors (Exceptions)
Errors that occur at runtime (after passing the syntax test) re called exceptions or logical errors.

Example : 3 types of event occured

1)try to open a file(for reading) that does not exist (FileNotFoundError)
2)try to divide a number by zero (ZeroDivisionError)
3)try to import a module that does not exist (ImportError) and so on.


We can handle these built-in and user-defined exceptions in Python using 

try,  => code all 
except,  => if any error ocured then 
finally statements.  => run all time  


Python Error and Exception

1) Errors represent conditions such as compilation error, syntax error, 
error in the logical part of the code, library incompatibility, 
infinite recursion, etc.

Errors are usually beyond the control of the programmer and 
we should not try to handle errors.

2) Exceptions can be caught and handled by the program.
We know that exceptions abnormally terminate the execution of a program.

The try...except block is used to handle exceptions in Python. 
Here's the syntax of try...except block:

"""

# view all the built-in exceptions using the built-in local() function as follows:
#print(dir(locals()['__builtins__']))



"""

Python try...except Block

try:
    # code that may cause exception
except:
    # code to run when exception occurs

"""


# try:
#     numerator = 10
#     denominator = 0

#     result = numerator/denominator
#     print(result)
# except:
#     print("Error: Denominator cannot be 0.")

# Output: Error: Denominator cannot be 0.     

#===========================================================

#Catching Specific Exceptions in Python

# try:
#     even_numbers = [2,4,6,8]
#     print(even_numbers[5])
# except ZeroDivisionError:
#     print("Denominator cannot be 0.")
# except IndexError:
#     print("Index Out of Bound.") 

# Output: Index Out of Bound    

#===========================================================

# Python try with else clause

# program to print the reciprocal of even numbers

# try:
#     num = int(input("Enter a number: "))
#     assert num % 2 == 0 # the assert statement in the code checks that num is an even number
# except:
#     print("Not an even number!")
# else:
#     reciprocal = 1/num
#     print(reciprocal)

#========================================================================
"""

Python try...finally
In Python, the finally block is always executed no matter 
whether there is an exception or not.

"""
try:
    numerator = 10
    denominator = 5

    result = numerator/denominator

    print(result)
except:
    print("Error: Denominator cannot be 0.")
    
finally:
    print("This is finally block.")