def check_for_type(value):
    if(isinstance(value, str)):
        if(not(value.isdigit())):
            raise TypeError("Value must be number")
        return float(value)
    else:
        if(type(value) not in [int, float]):
            raise TypeError("Value must be number")
        return value

def addition(a, b):
    a = check_for_type(a)
    b = check_for_type(b)
    return a + b

def subtraction(a, b):
    a = check_for_type(a)
    b = check_for_type(b)
    return a - b

def multiplication(a, b):
    a = check_for_type(a)
    b = check_for_type(b)
    return a * b

def division(a, b):
    a = check_for_type(a)
    b = check_for_type(b)
    if(b == 0):
        raise ValueError("Divided by zero")
    return a / b

if __name__ == '__main__':
    while (True):
        action, a, b = input().split()
        if (action == '+'):
            print(addition(a, b))
        elif (action == '-'):
            print(subtraction(a, b))
        elif (action == '*'):
            print(multiplication(a, b))
        elif (action == '/'):
            print(division(a, b))
        else:
            break
