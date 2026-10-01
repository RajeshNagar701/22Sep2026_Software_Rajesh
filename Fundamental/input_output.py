"""
Python Output

    print('Python is powerful')

    Syntax of print()

    print(object= separator= end= file= flush=)

    object - value(s) to be printed
    sep (optional) - allows us to separate multiple objects inside print().
    end (optional) - allows us to add add specific values like new line "\n", tab "\t"
    file (optional) - where the values are printed. It's default value is sys.stdout (screen)
    flush (optional) - boolean specifying if the output is flushed or buffered. Default: False

1)
    print('Good Morning!')
    print('It is rainy today')

    output
    Good Morning!
    It is rainy today

2)  # print with end whitespace

    print('Good Morning!', end= ' ')
    print('It is rainy today')

    Output : Good Morning! It is rainy today

3) print('New Year', 2023, 'See you soon!', sep= '. ')

    New Year. 2023. See you soon!

4)  Concatenated Strings

    print('Programiz is ' + 'awesome.')

5) Output formatting

    x = 5
    y = 10
    print('The value of x is {} and y is {}'.format(x,y))

    output : The value of x is 5 and y is 10

"""

#print output  
print('Python is powerful')

# using input() to take user input
num = input('Enter a number: ')
print('You Entered:', num)
print('Data type of num:', type(num)) # type of var


age=18
height=5.1
print(f"my age is {age} my height is {height}")
print("my age is", age ,"my height is", height)

