def delete_student(students):
    student_id = input("Enter student ID to delete: ")
    for student in students:
        if student['id'] == student_id:
            students.remove(student)
            print("Student deleted successfully!")
            break
    else:
        print("Student not found!")
