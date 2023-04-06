#Defining functions for each operator

def add(x, y):
    print(f"{x + y}\n")

def subtract(x, y):
    print(f"{x - y}\n")

def multiply(x, y):
    print(f"{x * y}\n")

def divide(x, y):
    if y == 0:
        print("Cannot Divide Number by Zero\n")
    else:
        print(f"{x / y}\n")

def modulus(x, y):
    print(f"{x % y}\n")

def carat(x, y):
    print(f"{x ** y}\n")

def floordivision(x, y):
    if y == 0:
        print("Cannot Divide Number by Zero\n")
    else:
        print(f"{x // y}\n")