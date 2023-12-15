# Task 2 (CALCULATOR)
''' Design a simple calculator with basic arithmetic operations.
Prompt the user to input two numbers and an operation choice.
Perform the calculation and display the resul '''

num1 = int(input("\nEnter first number: "))
num2 = int(input("\nEnter second number: "))
while True:
    def take_input():
        n1 = int(input("\nEnter first number: "))
        n2 = int(input("\nEnter second number: "))
        return n1,n2

    print("\nEnter 1 to Addition.")
    print("Enter 2 to Substraction.")
    print("Enter 3 to Multiplication.")
    print("Enter 4 to Division.")
    print("Enter 5 to take another input.")
    print("Enter 6 to Exit Program.")
    choice = int(input("Enter your choice: "))
    if(choice == 1):
        print("\nAddition : "+str(num1)+ " + "+str(num2) +" = "+ str(num1+num2))
    elif(choice == 2):
        print("\nSubstraction : "+str(num1)+" - "+ str(num2) +" = "+  str(num1-num2))
    elif(choice == 3):
        print("\nMultiplication : "+str(num1)+" * "+ str(num2) + " = "+ str(num1*num2))
    elif(choice == 4):
        print("\nDivision : "+str(num1)+ " + "+ str(num2) +" = "+  str(round((num1/num2),4)))
    elif(choice == 5):
        num1,num2 = take_input()
    elif(choice == 6):
        print("\nExit Program......")
        exit()
    else:
        print("\nEnter valid chioce: ")

