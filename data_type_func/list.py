'''
Python Lists
Python has several data types that let us group items together.

Here's why lists fit this use case:

Lists allow us to add, remove and change items. A shopping cart can change.
Items in a list are ordered. A shopping cart shows items in the order they are added.
Lists allow duplicate values (might not be relevant for a shopping cart, though).

cart = ["T-shirt", "Lamp", "Pen"]  #list
print(cart)

my_list = [1, "Python", 3.14] # A list of mixed data types
print(my_list)

my_list = []  # Empty list
print(my_list)


Python List Methods

append()	Adds an item to the end of the list
remove()	Removes the specified value from the list
pop()	    Returns and removes the last item or item at the given index
clear() 	Removes all items from the list
insert()	Inserts an item at the specified index

extend()	Adds all the items from another list (or any other iterable)
index()	    Returns the index of the first matched item
count() 	Returns the count of the specified item
sort()	    Sorts the list in ascending/descending order
reverse()	Reverses the list
copy()	    Returns the shallow copy of a list

Built-in functions such as enumerate(), len(), max(), min(), sorted() etc. 
'''


#Accessing List Items

# languages = ["Python", "Swift", "C++"]
# print(f"languages[0] = {languages[0]}") # Access the first item
# print(f"languages[-1] = {languages[-1]}") # Access the last item


#Adding and Updating Items

# cart = ["T-shirt", "Lamp", "Pen"]
# cart[1] = "Shoes" # Update second item to "Shoes"
# print(cart)    # ['T-shirt', 'Shoes', 'Pen']


# cart.append("Book") # Add "Book" to the end of the list
# print(cart)    # ['T-shirt', 'Lamp', 'Pen', 'Book']


# cart = ["T-shirt", "Lamp", "Pen"]
# fav_items = ["Headphones", "Phone"]
# cart.extend(fav_items) # Add all the items from fav_items to cart
# print(cart)    # ['T-shirt', 'Lamp', 'Pen', 'Headphones', 'Phone']


# cart = ["T-shirt", "Lamp", "Pen"]
# cart.insert(2, "Book")  # Add "Book" at index 2 (3rd position)
# print(cart)             # ['T-shirt', 'Lamp', 'Book', 'Pen']


#Remove Items From a List remove() , pop() , clear()  del

cart = ["T-shirt", "Lamp", "Pen", "Book"]

# Remove "Pen" from the list
cart.remove("Pen")              # ['T-shirt', 'Lamp', 'Book']

last_item = cart.pop()          # Remove the last item
print(cart)                     # ['T-shirt', 'Lamp']
print(last_item)                # Book

cart.clear()                    # Clear the list
print(cart)                     # []

del cart[2]                     # Delete the third item (index 2)
print(cart)                     # ['T-shirt', 'Lamp', 'Book']

del cart                        # Delete the list itself
print(cart)                     # NameError: name 'cart' is not defined


#Copying a List
'''

favorite_items = ["T-shirt", "Lamp", "Pen"]
cart = favorite_items.copy()        # Copying a list
favorite_items.append("Book")       # Add an item to favorite_items list
print(f"favorite_items = {favorite_items}")   #favorite_items = ['T-shirt', 'Lamp', 'Pen', 'Book']
print(f"cart = {cart}")                       #cart = ['T-shirt', 'Lamp', 'Pen']

'''



# vowels = "aeiou"
# vowels_list = list(vowels)  # Convert a string to a list
# print(vowels_list)          # ['a', 'e', 'i', 'o', 'u']



#loop list
# cart_items = ["T-shirt", "Lamp", "Pen"]
# for item in cart_items:
#     print(item)

