"""
Create a Set in Python
In Python, we create sets by placing all the elements inside curly braces {}, 
separated by commas.

A set can have any number of items and they may be of different 
types (integer, float, tuple, string, etc.).

# create a set of integer type
student_id = {112, 114, 116, 118, 115}


# create a set of string type
vowel_letters = {'a', 'e', 'i', 'o', 'u'}


# create a set of mixed data types
mixed_set = {'Hello', 101, -2, 'Bye'}


Create an Empty Set in Python

# create an empty set
empty_set = set()

# create an empty dictionary
empty_dictionary = { }

"""


# create a set of integer type
# student_id = {112, 114, 116, 118, 115}
# print('Student ID:', student_id)
# print(f'Student ID: {student_id}')



# Iterate Over a Set in Python

# for fruit in fruits: 
#     print(fruit)


# Duplicate Items in a Set  // can not contain duplicates.

# numbers = {2, 4, 6, 6, 2, 8}
# print(numbers)   # {8, 2, 4, 6}



# Add and Update and discard Set Items in Python

# numbers = {21, 34, 54, 12}
# numbers.add(32)
# print('Updated Set:', numbers) # Updated Set: {32, 34, 12, 21, 54}


# using update() method

# companies = {'Lacoste', 'Ralph Lauren'}
# tech_companies = ['apple', 'google', 'apple']
# companies.update(tech_companies)
# print(companies)  # Output: {'google', 'apple', 'Lacoste', 'Ralph Lauren'}


# using discard() method

# languages = {'Swift', 'Java', 'Python'}
# removedValue = languages.discard('Java')  # remove 'Java' from a set
# print(languages)    # {'Python', 'Swift'} 





# Built-in Functions with Set

# Function	Description
# all()	    Returns True if all elements of the set are true (or if the set is empty).
# any()	    Returns True if any element of the set is true. If the set is empty, returns False.
# enumerate()	Returns an enumerate object. It contains the index and value for all the items of the set as a pair.
# len()	    Returns the length (the number of items) in the set.
# max()	    Returns the largest item in the set.
# min()	    Returns the smallest item in the set.
# sorted()	Returns a new sorted list from elements in the set(does not sort the set itself).
# sum()	    Returns the sum of all elements in the set.

# add()	    Adds an element to the set
# clear()	Removes all elements from the set
# copy()	Returns a copy of the set
# difference()	Returns the difference of two or more sets as a new set
# difference_update()	Removes all elements of another set from this set
# discard()	Removes an element from the set if it is a member. (Do nothing if the element is not in set)
# intersection()	Returns the intersection of two sets as a new set
# intersection_update()	Updates the set with the intersection of itself and another
# isdisjoint()	Returns True if two sets have a null intersection
# issubset()	Returns True if another set contains this set
# issuperset()	Returns True if this set contains another set
# pop()	Removes and returns an arbitrary set element. Raises KeyError if the set is empty
# remove()	Removes an element from the set. If the element is not a member, raises a KeyError
# symmetric_difference()	Returns the symmetric difference of two sets as a new set
# symmetric_difference_update()	Updates a set with the symmetric difference of itself and another
# union()	Returns the union of sets in a new set
# update()	Updates the set with the union of itself and others


# find number of elements

# even_numbers = {2,4,6,8}
# print('Total Elements:', len(even_numbers))  # Total Elements: 4



# Python Set Operations 
# union: |  , 
# Intersection : &  , 
# difference : - , 
# symmetric_difference : ^


print('Union using |:', A | B)
print('Union using union():', A.union(B))     