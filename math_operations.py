class MathOperations:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        if self.num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return self.num1 / self.num2


class CustomException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message
