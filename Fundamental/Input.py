"""
In Python, you accept user input using the input() function. 

By default, the input() function always returns the data as a string (str)

Numeric Input (Typecasting) : int , float 
string : by default str

name=input("Enter your name : ")  // default string
age=int(input("Enter your name : "))  
per=float(input("Enter your name : "))


Multiple Inputs in One Line

first_name, last_name = input("Enter your first and last name: ").split()


"""


# a=10
# b=30
# print("sum of a & b are : ", a+b)

# a= int(input('Enter number of a : '))
# b= int(input('Enter number of b : '))
# print("sum of a & b are : ", a+b)


first_name, last_name= input("Enter your first and last name: ").split()
print("Your first name is : " , first_name , "and yoy Last name is : ", last_name)

#fstring
print(f"Your first name is : {first_name} and your Last name is : {last_name}")
