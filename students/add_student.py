def add_student(students):
    student_name = input("Enter student name: ")
    student_id = input("Enter student ID: ")
    # Add more fields as per your requirement

    student = {
        "name": student_name,
        "id": student_id
        # Add more fields as per your requirement
    }

    students.append(student)
    print("Student added successfully!")
