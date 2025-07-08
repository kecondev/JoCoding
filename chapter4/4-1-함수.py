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


def add_multi(choice, *args):
    if choice == "add":
        return sum(args)
    elif choice == "multi":
        result = 1
        for num in args:
            result *= num
        return result
    else:
        return "Invalid choice"
    
print(add_multi("add", 1, 2, 3, 4))
print(add_multi("multi", 1, 2, 3, 4))
print(add_multi("other", 1, 2, 3, 4))   


lambda_add = lambda x, y: x + y
print(lambda_add(5, 3))  # 8