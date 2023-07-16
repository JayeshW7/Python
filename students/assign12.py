from students.add_student import add_student
from students.display_student import display_students
from students.update_student import update_student
from students.delete_student import delete_student

def menu():
    students = []  # List to store student information
    while True:
        print("Welcome to the Student Management System!")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_student(students)
        elif choice == '2':
            display_students(students)
        elif choice == '3':
            update_student(students)
        elif choice == '4':
            delete_student(students)
        elif choice == '5':
            print("Thank you for using the Student Management System!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    menu()
