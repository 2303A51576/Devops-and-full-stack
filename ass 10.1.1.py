
# College Student Management System

# Sample student data
students = [
    {
        "id": 1,
        "name": "Rahul",
        "rollNo": "CSE101",
        "branch": "CSE"
    },
    {
        "id": 2,
        "name": "Priya",
        "rollNo": "CSE102",
        "branch": "CSE"
    }
]


# Display all students
def display_students():
    print("\n========== STUDENT LIST ==========")
    print("{:<10} {:<15} {:<12}".format(
        "Roll No", "Name", "Branch"
    ))
    print("-" * 37)

    for student in students:
        print("{:<10} {:<15} {:<12}".format(
            student["rollNo"],
            student["name"],
            student["branch"]
        ))

    print("-" * 37)
    print("Total Students:", len(students))


# Add a new student
def add_student():
    name = input("Enter student name: ").strip()
    roll_no = input("Enter roll number: ").strip()
    branch = input("Enter branch: ").strip()

    if not name or not roll_no or not branch:
        print("Error: All fields are required.")
        return

    if any(s["rollNo"].lower() == roll_no.lower()
           for s in students):
        print("Error: Roll number already exists.")
        return

    new_id = max(
        (s["id"] for s in students), default=0
    ) + 1

    student = {
        "id": new_id,
        "name": name,
        "rollNo": roll_no,
        "branch": branch
    }

    students.append(student)
    print("Student added successfully!")


# Search for a student
def search_student():
    roll_no = input("Enter roll number to search: ").strip()

    for student in students:
        if student["rollNo"].lower() == roll_no.lower():
            print("\nStudent Details")
            print("ID:", student["id"])
            print("Name:", student["name"])
            print("Roll No:", student["rollNo"])
            print("Branch:", student["branch"])
            return

    print("Student not found.")


# Update student information
def update_student():
    roll_no = input("Enter roll number to update: ").strip()

    for student in students:
        if student["rollNo"].lower() == roll_no.lower():
            name = input("Enter new name: ").strip()
            branch = input("Enter new branch: ").strip()

            if name:
                student["name"] = name
            if branch:
                student["branch"] = branch

            print("Student updated successfully!")
            return

    print("Student not found.")


# Delete a student
def delete_student():
    roll_no = input("Enter roll number to delete: ").strip()

    for student in students:
        if student["rollNo"].lower() == roll_no.lower():
            confirm = input(
                "Are you sure you want to delete? (yes/no): "
            ).strip().lower()

            if confirm == "yes":
                students.remove(student)
                print("Student deleted successfully!")
            else:
                print("Deletion cancelled.")
            return

    print("Student not found.")


# Main menu
while True:
    print("\n===== COLLEGE STUDENT MANAGEMENT =====")
    print("1. Display Students")
    print("2. Add Student")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        display_students()
    elif choice == "2":
        add_student()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        print("Thank you for using Student Management System!")
        break
    else:
        print("Invalid choice. Please try again.")
