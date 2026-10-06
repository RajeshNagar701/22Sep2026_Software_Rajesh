'''
Python Tuples

A tuple is a sequence similar to a Python list. 
The key difference between the two is that we cannot change the items of a 
tuple once it is created.

Use it for data that shouldn't change Tuples are Immutable but list can

not Deleting a Tuple   but  list can 


numbers = ()                # Empty tuple
print(numbers)

odd_nums = (1, 3, 5, 7)         # Tuple having data of the same type
print(odd_nums)

details = (111, "2026-08-09", "California") # Tuple having mixed data types
print(details)


# nested tuple
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))


# tuple can be created without parentheses ()
# also called tuple packing
my_tuple = 3, 4.6, "dog"   #withaout ()

a, b, c = my_tuple  # tuple unpacking is also possible

Diference between list vs Tuple

Key points to remember:
The literal syntax of tuples: parentheses () whereas the lists: square brackets [] .
Lists has variable length, tuple has fixed length.
List has mutable nature, tuple has immutable nature.
List has more functionality than the tuple.

'''

# my_tuple = ['p','e','r','m','i','t']  # i
# print(my_tuple[4])

# n_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
# print(n_tuple[1][1])  # nested index 's'




# Slicing
# We can access a range of items in a tuple by using the slicing operator (colon).

# my_tuple = ('p','r','o','g','r','a','m','i','z')
# print(my_tuple[1:4])  # elements 2nd to 4th ('r', 'o', 'g')
# print(my_tuple[:-7])  # elements beginning to 2nd  ('p', 'r')
# print(my_tuple[7:])   # elements 8th to end ('i', 'z')
# print(my_tuple[:])    # elements beginning to end ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')


#Changing or Deleting a Tuple
#Unlike lists, tuples are immutable : we can not change 
# tuples can be reassigned


#We can use + operator to combine two tuples
# print((1, 2, 3) + (4, 5, 6)) #(1, 2, 3, 4, 5, 6)
# print(("Repeat",) * 3) #('Repeat', 'Repeat', 'Repeat')

#We cannot delete or remove items from a tuple. But deleting the tuple entirely is possible using the keyword del

# my_tuple = ('p','r','o','g','r','a','m','i','z')
# del my_tuple
# print(my_tuple);  #NameError: name 'my_tuple' is not defined




#Python Tuple Methods
# count(x)	Return the number of items that is equal to x
# index(x)	Return index of first item that is equal to x

# my_tuple = ('a','p','p','l','e',)
# print(my_tuple.count('p'))   #2
# print(my_tuple.index('e'))   #4




#Other Tuple Operations : Tuple Membership Test
my_tuple = ('a','p','p','l','e',)
# print('a' in my_tuple)     #True
# print('b' in my_tuple)     #False
# print('g' not in my_tuple) #True


#Iterating Through a Tuple

# for name in ('John','Kate'):
#     print("Hello",name)




#Built-in Functions with Tuple

# Function	Description

# all()	    Return True if all elements of the tuple are true (or if the tuple is empty).
# any()	    Return True if any element of the tuple is true. If the tuple is empty, return False.
# enumerate()	Return an enumerate object. It contains the index and value of all the items of tuple as pairs.
# len()	    Return the length (the number of items) in the tuple.
# max()	    Return the largest item in the tuple.
# min()	    Return the smallest item in the tuple
# sorted()	Take elements in the tuple and return a new sorted list (does not sort the tuple itself).
# sum()	    Retrun the sum of all elements in the tuple.
# tuple()	    Convert an iterable (list, string, set, dictionary) to a tuple.



#Advantage of Tuple over List

# 1)tuple are immutable, iterating through tuple is faster than with list.
# 2)So there is a slight performance boost.
# 3)Tuples that contain immutable elements can be used as key for a dictionary.
# 4)tuple will guarantee that it remains write-protected.  doesn’t change


# we can also use tuple like this (23,23,56)

t1=23,23,56
print(type(t1))  # output : <class 'tuple'>
