# creating list by taking user input
list = []

print("Enter 5 numbers:")
for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    list.append(num)

print("Numbers entered by the user:", list)

# sum of numbers in the list
result = sum(list)
print(f'sum of {list} is {result}')

# smallest number from list
smallest = min(list)
print(f'smallest number in {list} is {smallest}')

# largest number from list
largest = max(list)
print(f'largest number in {list} is {largest}')

# Ascending list 
list.sort()
print(f'{list} in ascending order : {list}')

# Descending list
list.sort(reverse=True)
print(f'{list} in descending order : {list}')

# converting list to tuple
Tuple = tuple(list)
print(f'after converting list to tuple: {Tuple}')

# Deleting List
del list
print(list)
