#Defining functions for each operator

def add(x, y):
    result = x + y
    return result

def subtract(x, y):
    result = x - y
    return result

def multiply(x, y):
    result = x * y
    return result

def divide(x, y):
    if y == 0:
        print("Cannot Divide Number by Zero\n")
    else:
        result = x / y
        return result

def modulus(x, y):
    result = x % y
    return result

def carat(x, y):
    result = x ** y
    return result

def floordivision(x, y):
    if y == 0:
        print("Cannot Divide Number by Zero\n")
    else:
        result = x // y
        return result