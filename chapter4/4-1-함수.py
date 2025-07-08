def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Division by zero error"

print(add(5, 3))        # 8
print(subtract(5, 3))   # 2
print(multiply(5, 3))   # 15
print(divide(5, 3))     # 1.6666666666666667
print(divide(5, 0))     # Division by zero error