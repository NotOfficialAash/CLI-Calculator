from sys import exit
import os
import operations

#Defining a function to clear the screen based on the OS
def clear():
    if os.name == "nt": #Windows OS is also knonw as 'nt'
        os.system("cls")
    else: #In case of mac or Linux
        os.system("clear")


clear()
print("!!!Welcome!!!")
print("Press ENTER to continue or type 'exit' to close...")
status = input()

#While loop so that the program dosen't stop after one excecution
while True:

    if status == "exit":
     break
    
    clear()
    try:
        num1 = int(input("First number: "))
        operator = input("Operation: ")
        num2 = int(input("Second number: "))
    except Exception as error:
        print(f"{error = }")
        print("It was a vaue error!\nPlease restart the program\n")
        exit(0x1)
        

    match operator:
        case "+":
            operations.add(num1, num2)
        case "-":
            operations.subtract(num1, num2)
        case "*":
            operations.multiply(num1, num2)
        case "/":
            operations.divide(num1, num2)
        case "%":
            operations.modulus(num1, num2)
        case "^":
            operations.carat(num1, num2)
        case _:
            print("Invalid operator\n")

    print("Press any ENTER to continue or type 'exit' to close...")     
    status = input()
    clear()
