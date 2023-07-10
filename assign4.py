numbers = [1, 2, 3, 4, 5,6.7]

for i in numbers:
    if i == 3:
        print("Encountered 3, breaking loop")
        break  #
    elif i == 2:
        print("Encountered 2, continue")
        continue  
    elif i == 4:
        print("Encountered 4, passing")
        pass 
    print(i)
else:
    print("All numbers were iterated successfully!")

count = 0

while count < 5:
    if count == 2:
        print("Count is 2, breaking the loop")
        break
    elif count == 3:
        print("Count is 3, skipping this iteration")
        count += 1
        continue
    print(count)
    count += 1
else:
    print("Count reached 5!")
