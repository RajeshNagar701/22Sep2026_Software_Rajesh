# Python Numbers, Type Conversion and Mathematics

# In numeric values.

# int - holds signed integers of non-limited length.
# float - holds floating decimal points and it's accurate up to 15 decimal places.
# complex - holds complex numbers.

num1 = 5
print(num1, 'is of type', type(num1))  # 5 is of type <class 'int'>

num2 = 5.42
print(num2, 'is of type', type(num2)) # 5.42 is of type <class 'float'>

num3 = 8+2j
print(num3, 'is of type', type(num3)) # (8+2j) is of type <class 'complex'>

#===============================================================================

#Type Conversion in Python   int() , float(), complex()

num1 = int(2.3)
print(num1)  # prints 2

num2 = int(-2.8)
print(num2)  # prints -2

num3 = float(5)
print(num3) # prints 5.0

num4 = complex('3+5j')
print(num4)  # prints (3 + 5j)



# Python Random Module


"""
Random / Math Module : 
	random.randrange(10,20)   # 15
	random.choice(['a', 'b', 'c', 'd', 'e'])   # a
	random.shuffle(['a', 'b', 'c', 'd', 'e'])   # ['d', 'b', 'c', 'e', 'a']
	random.random(['a', 'b', 'c', 'd', 'e'])

"""

import random
# print(random.randrange(10, 20))  #15

# list1 = ['a', 'b', 'c', 'd', 'e']
# # get random item from list1
# print(random.choice(list1))      #a

# # Shuffle list1
# random.shuffle(list1)           
# print(list1)                     #['d', 'b', 'c', 'e', 'a']

# # Print random element   0.0 to 1.0
# print(random.random())          # 0.6716121217631744


# # Python Mathematics

# import math

print(math.pi)             #3.141592653589793
print(math.cos(math.pi))   #-1.0
print(math.exp(10))        #22026.465794806718
print(math.log10(1000))    #3.0
print(math.sinh(1))        #1.1752011936438014
print(math.factorial(6))   #720




