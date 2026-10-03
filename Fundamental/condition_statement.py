"""

Python If Statement

1)
if condition:
    # This code runs only if condition is True

2)
if condition:
    # Run this code if condition is True
else:
    # Run this code if condition is False



3)

if condition1:
    # Run this code if condition1 is True
elif condition2:
    # Run this code if condition1 is False but condition2 is True
else: 
    # Run this code if both condition1 and condition2 are False

4) Nested if Statements

age = int(input("Enter your age: "))

# Condition to check if age is less than 18
if age < 18:
    if age < 0:
        print("Invalid age.")
    else:
        print("Deny access.")
else:
    print("Grant access.")


5)Short Hand if...else

    age = 22
    status = "Adult" if age >= 18 else "Minor"
    print(status)

6) Python Pass Statement
   if statements cannot be empty, but if you for some reason have an 
   if statement with no content, put in the pass statement to avoid getting an error.

    a = 33
    b = 200

    if b > a:
      pass
      
      
7) The Python Match Statement
    
   Instead of writing many if..else statements, you can use the match statement.
   The match statement selects one of many code blocks to be executed.
   
day = 4
match day:
    case 1:
    print("Monday")
    case 2:
    print("Tuesday")
    case 3:
    print("Wednesday")
    case 4:
    print("Thursday")
    
    
    
    Default Value
    
day = 4
match day:
  case 6:
    print("Today is Saturday")
  case 7:
    print("Today is Sunday")
  case _:
    print("Looking forward to the Weekend")

    Combine Values
    
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5:
    print("Today is a weekday")
  case 6 | 7:
    print("I love weekends!") 
    
"""


# age = int(input("Enter your age: "))

# if age >= 18:
#     print("Grant access to the website.")


# age = int(input("Enter your age: "))

# if age >= 18:
#     print("Grant access.")
# else:
#     print("Deny access.")


# pass
age=17
if age >= 18:
    pass
else:
    print("Deny access.")


# age = 22
# status = "Adult" if age >= 18 else "Minor"
# print(status)



# per = int(input("Enter your per % : "))

# if per >= 90:
#     print("A++")
# elif per >= 80:
#     print("A")
# elif per >= 70:
#     print("B++")
# elif per >= 60:
#     print("B")
# elif per >= 50:
#     print("C")
# else:
#     print("Fail")


# email="raj@gmail.com"
# password="1234"
# status="Block"

# if email=="raj@gmail.com":
#    if password=="1234":
#        if status=="Unblock":
#            print("Login success")
#        else:
#            print("Account is Block") 
#    else:
#        print("Login Failed due to Wrong Password")
# else:
#     print("Email dones not exist")




#match   

# day=input("Enter Today Day : ")
# match day:
#     case 'TUE':
#         print("Today is Tuesday")
#     case 'THU':
#         print("Today is Thursday")
#     case 'SAT':
#         print("Today is Saturday")
#     case _:
#         print("Wrong Day")
        
# day=int(input("Enter Today Day No : "))
# match day:
#   case 1 | 2 | 3 | 4 | 5:
#     print("Today is a weekday")
#   case 6 | 7:
#     print("I love weekends!") 