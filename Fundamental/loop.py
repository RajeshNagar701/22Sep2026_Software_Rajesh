"""
Python for Loop
    Python has two primitive loop commands:

    1)while loops
    2)for in loops (Range)

i = 1
while i < 6:
  print(i)
  i += 1


range(stop) 
range(start, stop) 
range(start, stop, step) 


for item in sequence:
    # Run this block of code

For Loop with Python range(start,stop,step)  

# Generate numbers from 1 to 4
values = range(1, 5)

"""


#1) While

#i = 1
#while i < 6:
#  print(i)
#  i += 1
    


#2) For in

# models = ["Fable", "ChatGPT", "Gemini"]

# Access items of the list one by one
# for model in models:
#     print(model)
#     print("---")


# Iterate from i = 1 to i = 10
# for i in range(1, 11):
#     print(f"Displaying product {i}")    


# language = 'Python'

# for x in language:
#     print(x)


# if we want in reverse 100 to 1
#for i in range(100, 1,-1):
#    print(i) 




# Break & Continue

# for num in range(1, 11):
#     if num == 5:
#         break
#     print(num)


# The continue Statement

# for num in range(1, 6):
#     if num == 3:
#         continue
#     print(num)

# Python pass Statement
# In Python, pass is a null statement and it does nothing when executed. 
# Despite not doing anything, pass does have a purpose.

# is_valid = True
# if is_valid:
#     pass # in {} body we have add some code if not then gives error so we add PASS
# else:
#     print("Login invalid. Redirect to form.")


# we can also add step in range
# for i in range(1,10,2):
#     print(i)   # 1 3 5 7 9





"""
An iterator is an object that contains a countable number of values.
An iterator is an object that can be iterated upon, meaning that you can 
traverse through all the values.
Technically, in Python, an iterator is an object which implements the 
iterator protocol, which consist of the methods __iter__() and __next__().

Lists, tuples, dictionaries, and sets are all iterable objects. 
They are iterable containers which you can get an iterator from.


"""

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))