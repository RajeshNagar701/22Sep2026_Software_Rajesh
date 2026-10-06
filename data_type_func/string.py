#Python Strings
#A string is a sequence of characters enclosed inside quotes 
# (either double or single quotes).

# message=" Hi how are yoy "
# print(message)



# Multiline string
# message = """To avoid pain, they avoid pleasure.
# To avoid death, they avoid life."""
# print(message)

"""
String:     P  y  t  h  o  n 
Index:      0  1  2  3  4  5 
Negative:  -6 -5 -4 -3 -2 -1 
"""



# Access String Characters

# model = 'ChatGPT'
# print(model[0])    # Output: C # Access the first character
# print(model[-1])   # Output: T  # Access the last character
# print(model[0:4])   # Output: Chat

# Strings are Immutable  can't change

# model = 'ChatGPT'
# model[0] = 'W'
# print(model) #TypeError: 'str' object does not support item assignment


# model = 'Opus'
# version = '5'

# model = model + " " + version
# print(model)    # Opus 5






# Python String Methods

#String Slicing 

#string[ start:stop:step]  

# name = "Python" 
# print(name[0:2]) 
# print(name[2:5]) 
# print(name[1:4]) 
# print(name[:4]) 
# print(name[2:]) 


# Reverse a String 

# name = "Python" 
# reverse = name[::-1] 
# print(reverse) 


# Substring Extraction 

# text = "Hello Python" 
# print(text[0:5]) 



# len() – String Length 

# name = "Python" 
# print(len(name)) 

# Replace

# text = "ChatGPT is great."
# new_text = text.replace("ChatGPT", "Claude")
# print(new_text)  # Output: Claude is great.

# print('Chat' in 'ChatGPT')        # True
# print('Claude' not in 'ChatGPT')  # True


# Extra Function : 
# upper() , lower() , capitalize(),  title() , strip() , find() , count()



# Iterate Through a String

# model = 'Opus'

# for c in model:
#     print(c)


# Escape Sequences

# example = "He said, "What's there?""   
# print(example) # Error

# escape double quotes
# example = "He said, \"What's there?\""
# # escape single quotes
# example = 'He said, "What\'s there?"'

# print(example)  # Output: He said, "What's there?"




# String Formatting (f-Strings)

company = 'Google'
field = 'AI'
print(f"hello {company}  hello  {field}")