'''
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    

a = Calculator()
print(a.add(5, 3))        # Output: 8
print(a.subtract(10, 4))  # Output: 6
print(a.multiply(2, 3))   # Output: 6
print(a.divide(8, 2))     # Output: 4.0

try:
    print(a.divide(5, 0))  # This will raise an exception
except ValueError as e:
    print(e)               # Output: Cannot divide by zero
print(a.divide(9, 3))     # Output: 3.0
print(a.add(1, 2))        # Output: 3
print(a.subtract(7, 5))   # Output: 2
print(a.multiply(4, 6))   # Output: 24
print(a.divide(10, 2))    # Output: 5.0
print(a.add(0, 0))        # Output: 0
print(a.subtract(3, 3))   # Output: 0
print(a.multiply(1, 1))   # Output: 1
print(a.divide(1, 1))     # Output: 1.0
print(a.add(-5, -3))      # Output: -8
print(a.subtract(-10, -4)) # Output: -6
print(a.multiply(-2, -3))  # Output: 6
print(a.divide(-8, -2))    # Output: 4.0
print(a.add(5.5, 3.2))
'''


class FourCal:
    def __init__(self):
        self.first = 0
        self.second = 0

    def setData(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        return self.first + self.second

    def sub(self):
        return self.first - self.second

    def mul(self):
        return self.first * self.second

    def div(self):
        if self.second == 0:
            raise ValueError("Cannot divide by zero")
        return self.first / self.second


a = FourCal()
a.setData(4, 2)
print(a.first)  # Output: 4
print(a.second)  # Output: 
print(a.add())

