import os
import operations


def clear():
    #Clears the terminal screen.
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def get_input():
    #Prompts the user for input and returns the numbers and operator.
    try:
        num1 = int(input("First number: "))
        operator = input("Operation: ")
        num2 = int(input("Second number: "))
        return num1, operator, num2

    except ValueError as error:
        print(f"{error = }")
        print("It was a value error!\nPlease restart the program.\n")
        exit(1)


def perform_operation(num1, operator, num2):
    #Performs the operation based on the operator symbol.
    dictofoperations = {
        "+": operations.add,
        "-": operations.subtract,
        "*": operations.multiply,
        "/": operations.divide,
        "%": operations.modulus,
        "^": operations.carat,
        "//": operations.floordivision,
    }
    finaloperation = dictofoperations.get(operator)
    if finaloperation != None:
        finaloperation(num1, num2)
    else:
        print("Invalid operator.")


def main():
    #Main function to run the calculator.
    clear()
    print("!!!Welcome!!!")
    print("Press ENTER to continue or type 'exit' to close...")
    status = input()

    while status != "exit":
        clear()
        num1, operator, num2 = get_input()
        perform_operation(num1, operator, num2)
        print("Press ENTER to continue or type 'exit' to close...")
        status = input()
    clear()


if __name__ == "__main__":
    main()