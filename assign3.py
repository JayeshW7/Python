
#functions
def add(num1,num2):
    return num1 + num2

def sub(num1,num2):
    return num1 - num2

def mul(num1,num2):
    return num1 * num2

def div(num1,num2):
    return num1 / num2

def floor_div(num1,num2):
    return num1 // num2

def exponent(num1,num2):
    return num1** num2


# choice selection
print("Please select a number:" \
    "1. Add\n" \
    "2. Sub\n" \
    "3. Multiply\n" \
    "4. Divide\n"
    "5. floor division\n" 
    "6. exponent\n")

#User input
choice = int(input("Select a choice from 1,2,3,4,5,6:"))

num_1 = int(input("Enter first number:"))
num_2 = int(input("Enter second number:"))

if choice == 1:
    print(f"{num_1} + {num_2} = ",add(num_1,num_2))

elif choice == 2:
    print(f"{num_1} - {num_2} = ",sub(num_1,num_2))

elif choice == 3:
    print(f"{num_1} * {num_2} = ",mul(num_1,num_2))

elif choice == 4:
    print(f"{num_1} / {num_2} = ",div(num_1,num_2))

elif choice == 5:
    print(f"{num_1} // {num_2} = ",floor_div(num_1,num_2))

elif choice == 6:
    print(f"{num_1} ** {num_2} = ",exponent(num_1,num_2))
else:
    print("invalid input")
