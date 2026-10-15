
# 1) 


while True:

    menu = """
        Press 1 for Insert Data list
        Press 2 for Fetch All Data list
        Press 3 for Fetch Single Data by index list
        Press 4 for Update Data
        Press 5 for Delete Data
        Press 6 for Exit
        """

    print(menu)


    students=["Raj","nagar"]
    print(students)

    number =int(input("Enter any Number : "))
    if number==1:
        name=str(input("Enter any Name : "))
        students.append(name)
    elif number==2:
        students.pop()
    elif number==3:
        index=int(input("Enter any index of list : "))
        updated_list=str(input("Enter any Name : "))
        students[index]=updated_list
    else:
        print("Invalid Number")
    print(f'Updated list : {students}')            


