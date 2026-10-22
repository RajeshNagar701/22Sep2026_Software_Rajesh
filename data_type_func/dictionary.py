"""

create a dictionary by placing key: value pairs inside curly brackets {}

students={1,'RAJ NAGAR','raj@gmail.com','abc@123','123654789'}

students={id:1,name:'RAJ NAGAR',email:'raj@gmail.com',password:'abc@123',mobile:'123654789'},
print(students["name"])   => output : RAJ NAGAR

student1=[
          {id:1,name:'RAJ NAGAR',email:'raj@gmail.com',password:'abc@123',mobile:'123654789'},
          {id:2,name:'Akash NAGAR',email:'Akash@gmail.com',password:'abc@123',mobile:'123654789'},
          {id:3,name:'nirav NAGAR',email:'nirav@gmail.com',password:'abc@123',mobile:'123654789'}
        ]

student1[1][name]


country = {
  "Germany": "Berlin", 
  "Canada": "Ottawa", 
  "England": "London"
}

print(country["Germany"])    # Output: Berlin
print(country.get('Germany'))  # Output: Berlin   by get() method


{'Germany': 'Berlin', 'Canada': 'Ottawa', 'England': 'London'}


Valid and Invalid Dictionaries

# valid dictionary

my_dict = {1: "one", 2: "two", 3: "three"}                 # integer as a key 
my_dict = {(1, 2): "one two", 3: "three"}                  # tuple as a key
my_dict = {"USA": ["Chicago", "California", "New York"]}   # string as a key, list as a value

# invalid dictionary
my_dict = {1: "Hello", [1, 2]: "Hello Hi"}                 # Error: using a list as a key is not allowed


# Note : dictionary must be unique  
============================================================


hogwarts_houses = {
    "Harry Potter": "Gryffindor",
    "Hermione Granger": "Gryffindor",
    "Harry Potter": "Slytherin"         # duplicate key with a different house
}

# If there are duplicate keys, the later value of the key overwrites the previous value.
output : {'Harry Potter': 'Slytherin', 'Hermione Granger': 'Gryffindor'}

"""

# country = {
#   "Germany": "Berlin", 
#   "Canada": "Ottawa", 
#   "England": "London"
# }

# print(country["Germany"])    # Output: Berlin
# print(country.get('Germany'))  # Output: Berlin   by get() method



#Add Items to a Dictionary

# country_capitals = {
#   "Germany": "Berlin", 
#   "Canada": "Ottawa", 
# }

# # add an item with "Italy" as key and "Rome" as its value
# country_capitals["Italy"] = "Rome"  
# print(country_capitals)      #{'Germany': 'Berlin', 'Canada': 'Ottawa', 'Italy': 'Rome'}  

# # change the value of "Italy" key to "Rome"
# country_capitals["Italy"] = "Naples" 
# print(country_capitals)       #{'Germany': 'Berlin', 'Italy': 'Naples', 'England': 'London'}

# # delete item having "Germany" key
# del country_capitals["Germany"]   
# print(country_capitals)      # {'Canada': 'Ottawa', 'Italy': 'Naples'}

# # clear the dictionary
# country_capitals.clear()    
# print(country_capitals)      # {}



# country_capitals = {
#   "United States": "Washington D.C.", 
#   "Italy": "Rome" 
# }

# # print dictionary keys one by one
# for country in country_capitals:
#     print(country)

# # print dictionary values one by one
# for country in country_capitals:
#     capital = country_capitals[country]
#     print(capital)


# Find Dictionary Length 
# country_capitals = {"England": "London", "Italy": "Rome"}
# print(len(country_capitals))   # Output: 2



# Python Dictionary Methods

# Function	Description

# pop()	    Removes the item with the specified key.
# update()	Adds or changes dictionary items.
# clear()	  Remove all the items from the dictionary.
# keys()	  Returns all the dictionary's keys.
# values()	Returns all the dictionary's values.
# get()	    Returns the value of the specified key.
# popitem()	Returns the last inserted key and value as a tuple.
# copy()	  Returns a copy of the dictionary.



students={'id':1,'name':'Nagar','email':'raj@gmail.com','password':'abc@123','mobile':'123654789'}
print(students.keys())   # list format all keys
print(students.values())  # list format all value

for key in students:
  print(students[key])

users = [
    {"name": "Alice", "role": "Admin", "status": "Active"},
    {"name": "Bob", "role": "Developer", "status": "Inactive"},
    {"name": "Charlie", "role": "Designer", "status": "Active"}
]

for user in users:
  #print(user)
  #print(user['name'])
  print(f"{user['name']} is a {user['role']} and is currently {user['status']}.")
  
  
  
  
# Dictionary Membership Test : # use of in and not in operators

# file_types = {
#     ".txt": "Text File",
#     ".pdf": "PDF Document",
#     ".jpg": "JPEG Image",
# }

# print(".pdf" in file_types)       # Output: True
# print(".mp3" in file_types)       # Output: False
# print(".mp3" not in file_types)   # Output: True