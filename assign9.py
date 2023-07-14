from math_operations import MathOperations, CustomException

try:
    math_obj = MathOperations(10, 5)
    print("Addition:", math_obj.add())
    print("Subtraction:", math_obj.subtract())
    print("Multiplication:", math_obj.multiply())
    print("Division:", math_obj.divide())

    # Uncomment the next line to test the custom exception
    # raise CustomException("This is a custom exception")

except ZeroDivisionError as e:
    print("Error:", e)

except CustomException as e:
    print("Custom Exception:", e)
