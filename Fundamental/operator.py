"""
Python Operators

Types of Python Operators
    Arithmetic Operators    +  -  *  /  //  %  **
    Assignment Operators    = += -= *= /= %= **=
    Comparison Operators    == != > < >= <=
    Logical Operators       and or not
    Bitwise Operators   
    Special Operators
        Identity operators     is / is not
        Membership operators   in / not_in 
"""


#------------Arithmatic-----------------------------------------------
# a = 10
# b = 2

# # addition
# print ('Sum: ', a + b)  

# # subtraction
# print ('Subtraction: ', a - b)   

# # multiplication
# print ('Multiplication: ', a * b)  

# # division
# print ('Division: ', a / b) 

# # floor division
# print ('Floor Division: ', a // b)

# # modulo
# print ('Modulo: ', a % b)  

# # a to the power b
# print ('Power: ', a ** b)  # 10*10   10 ** 3  


#=================Asignment===============================================
# # assign 10 to a
# a = 10

# # # assign 5 to b
# b = 5 

# # # assign the sum of a and b to a
# a += b      # a = a + b    

# print(a)

# #===============Comparision============================
# a = 5
# b = 2

# print (a > b)    # True


# #===============Logical ===============================

a = 5
b = 6
c = 10
# print((a > 2) and (b >= 6))    # True

if a>b and a>c:
    print("a is greater then b & c")

# if not condition:
#     # This code runs if the condition is False (or "Falsy")



# #-------------Special operators---------------------------------------

# #Identity operators
# x1 = 5
# y1 = 5
# x2 = 'Hello'
# y2 = 'Hello'

# print(x1 is not y1)  # prints False
# print(x2 is y2)  # prints True



# #Membership operators
message = 'Hello world'
dict1 = {1:'a', 2:'b'}

# # check if 'H' is present in message string
print('H' not in message)  # prints True

# # check if '1' key is present in dict1
print(1 in dict1)  # prints True