def display_students(students):
    print("Student List:")
    if not students:
        print("No students found.")
    else:
        for student in students:
            print(f"Name: {student['name']}, ID: {student['id']}")
            # Display more fields as per your requirement
