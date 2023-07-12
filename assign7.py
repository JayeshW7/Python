def FileFunc(file="Jay.txt"):
    try:
        with open(file, "a") as f:
            roll_number = "125"
            name = "Jayesh Wagh"
            class_name = "TY"
            entries = [roll_number, name, class_name]
            f.writelines("\n".join(entries))  # join to access the elements in file

        with open(file, "r") as f:
            display = f.readlines()
            print("Entered File Content:")
            for line in display:
                print(line.strip()) 

    except FileNotFoundError:
        print(f"File '{file}' not found!")


FileFunc()  

