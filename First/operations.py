#Defining functions for each operator

def add(x, y):
    print(f"{x + y}\n")

def subtract(x, y):
    print(f"{x - y}\n")

def multiply(x, y):
    print(f"{x * y}\n")

def divide(x, y):
    if y == 0:
        print("Cannot divide number by Zero")
    else:
        print(f"{x / y}\n")

def modulus(x, y):
    print(f"{x % y}\n")

def carat(x, y):
    print(f"{x ** y}\n")