"""
    Python Type Conversion

    There are two types of type conversion in Python.

    Implicit Conversion - automatic type conversion
    Explicit Conversion - manual type conversion

"""

#Implicit Type Conversion

integer_number = 123
float_number = 1.23

new_number = integer_number + float_number

# display new value and resulting data type
print("Value:",new_number)
print("Data Type:",type(new_number))


#=====================================================
#Explicit Conversion


num_string = '12'
num_integer = 23

print("Data type of num_string before Type Casting:",type(num_string))

# explicit type conversion
num_string = int(num_string)
print("Data type of num_sum:",type(num_string))