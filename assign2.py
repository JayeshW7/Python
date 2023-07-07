# ****** Arithmetic operators *******

a = 15 
b = 5

ans = a + b
print(f"Addition of {a} and {b} is {ans}")

ans = a - b
print(f"Subtraction of {a} and {b} is {ans}")

ans = a * b
print(f"multiplication of {a} and {b} is {ans}")

ans = a % b
print(f"Modulus of {a} and {b} is {ans}")   

ans = a / b
print(f"Division of {a} and {b} is {ans}")

ans = a**b
print(f"Exponent of {a} and {b} is {ans}")

ans = a // b
print(f"Floor division of {a} and {b} is {ans}")


# ****** Logical Operators ******

num = 20

ans2 = num > 10 and num <10 
print(f"AND operation result: {ans2}")

ans2 = num > 10 or  num < 10
print(f"OR operation result: {ans2}")

ans2 = not num 
print(f"NOT operation result: {ans2}")

# ****** Assignment operators ******

a = 8
print(f"initial value of a: {a}")

a += 2
print(f"+= operation result: {a}")

a-=2
print(f"-= operation result: {a}")

a*=2
print(f"*= operation result: {a}")

a/=2
print(f"/= operation result: {a}")

a//=2
print(f"//= operation result: {a}")

a**=2
print(f"**= operation result: {a}")


# ****** Comparison operators ******

a = 30
b = 20

ans3 = a < b
print(f"{30} < {20}: {ans3}")

ans3 = a > b
print(f"{30} > {20}: {ans3}")

ans3 = a <= b
print(f"{30} <= {20}: {ans3}")

ans3 = a >= b
print(f"{30} >= {20}: {ans3}")

ans3 = a != b
print(f"{30} != {20}: {ans3}")

ans3 = a == b
print(f"{30} == {20}: {ans3}")


# ****** Bitwise Operator ******

a = 20
b = 10

ans4 = a & b
print(f"bitwise & of {a} and {b} is {ans4}")

ans4 = a | b
print(f"bitwise | of {a} and {b} is {ans4}")

ans4 = a ^ b
print(f"bitwise ^ of {a} and {b} is {ans4}")

ans4 = a >> 2
print(f"bitwise >> of {a} and {b} is {ans4}")

ans4 = a << 2
print(f"bitwise << of {a} and {b} is {ans4}")

# ****** Identity Operators

a = 20
b = 20.0

ans5 = a is b
print(f"is a and b {ans5}")

ans5 = a is not b
print(f" is not a and b {ans5}")

# ****** special operators *******

strg = "Jayesh"
ans6 = "J" in strg
print(f"is J in string {ans6}")

ans6 = "W" not in strg
print(f"is W not in string {ans6}")