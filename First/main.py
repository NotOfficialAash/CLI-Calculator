from sys import exit
import os
import operations

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

print("!!!Welcome!!!")
print("Press ENTER to continue or type 'exit' to close...")
status = input()

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
        print("Oops!! You did not enter a number!\nPlease restart the program")
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
        case _:
            print("Invalid operator")

    print("Press any ENTER to continue or type 'exit' to close...")     
    status = input()
    clear()
