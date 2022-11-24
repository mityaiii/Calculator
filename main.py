def check_for_type(value):
    if(type(value) not in [int, float]):
        raise TypeError("Value must be number")

def addition(a, b):
    check_for_type(a)
    check_for_type(b)
    return a + b

def subtraction(a, b):
    check_for_type(a)
    check_for_type(b)
    return a - b

def multiplication(a, b):
    check_for_type(a)
    check_for_type(b)
    return a * b

def division(a, b):
    check_for_type(a)
    check_for_type(b)
    if(b == 0):
        raise ValueError("Divided by zero")
    return a / b
