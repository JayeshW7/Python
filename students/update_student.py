def update_student(students):
    student_id = input("Enter student ID to update: ")
    for student in students:
        if student['id'] == student_id:
            # Prompt the user for updated information and update the respective fields
            student['name'] = input("Enter updated student name: ")
            # Update more fields as per your requirement
            print("Student information updated successfully!")
            break
    else:
        print("Student not found!")
