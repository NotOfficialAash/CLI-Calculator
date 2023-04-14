import os
import operations
import time

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
        result = finaloperation(num1, num2)
        return result
    else:
        print("Invalid operator.")


######################################### History Section ############################################
def write_history(his_num1, his_operator, his_num2, his_result):
    #Stores calculation history in a file
    with open("history.txt", "a") as his_file:
        his_time = time.strftime("%Y-%m-%d %H:%M:%S")
        his_file.write(f"{his_time} || {his_num1} {his_operator} {his_num2} = {his_result}\n")


def read_history():
    with open("history.txt", "r") as his_file:
        clear()
        if os.stat("history.txt").st_size == 0:
            print("Your History is empty")
        else:
            for i in his_file:
                print(i, end = "")


def clear_history():
    with open("history.txt", "w") as his_file:
        his_file.truncate(0)
    print("History Cleared successfully")
######################################################################################################


def main():
    #Main function to run the calculator.
    clear()
    print("!!!Welcome!!!")

    while True:
        print("\nPress ENTER to continue or type 'exit' to close...\nUse 'history' to manage your calculation history")
        status = input()
        clear()

        if status == "history -r":
            read_history()
        elif status == "history -c":
            clear_history()
        elif status == "history":
            print("Type 'history -r' to display your history")
            print("Type 'history -c' to clear your history")
        elif status == "exit":
            exit()
        elif status == "":
            num1, operator, num2 = get_input()
            main_result = perform_operation(num1, operator, num2)
            print(main_result)
            write_history(num1, operator, num2, main_result)
            input()
        


if __name__ == "__main__":
    main()