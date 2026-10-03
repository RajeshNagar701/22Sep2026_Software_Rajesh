"""

Python match Statement

The Python Match Statement
    
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
    
    
    
    => Default Value
    
day = 4
match day:
  case 6:
    print("Today is Saturday")
  case 7:
    print("Today is Sunday")
  case _:
    print("Looking forward to the Weekend")


    => Combine Values
    
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5:
    print("Today is a weekday")
  case 6 | 7:
    print("I love weekends!") 
    
    
    => If Statements as Guards
       You can add if statements in the case evaluation as an extra condition-check:
       
month = 5
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case _:
    print("No match")

    
"""

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