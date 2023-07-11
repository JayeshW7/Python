
# creating ds function
def ds(roll_no, name):
    print("Roll No:", roll_no)
    print("Name:", name)

roll_no = 125
name = "Jayesh"
ds(roll_no, name)

# adding values 
List = [roll_no, name]
Tuple = (roll_no, name)
Set = {roll_no, name}
Dict = {"roll_no": roll_no, "name": name}

new_roll_no = 47
new_name = "prateek"

List[0] = new_roll_no
List[1] = new_name

Tuple = list(Tuple)
Tuple[0] = new_roll_no
Tuple[1] = new_name
Tuple = tuple(Tuple)

Set.remove(roll_no)
Set.remove(name)
Set.add(new_roll_no)
Set.add(new_name)

Dict["roll_no"] = new_roll_no
Dict["name"] = new_name

print(List)
print(Tuple)
print(Set)
print(Dict)



del List
del Tuple
del Set
del Dict

