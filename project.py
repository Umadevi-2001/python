students = {}

def add_student():
    sid = input("Enter Student ID: ")
    name = input("Enter Name: ")
    marks = input("Enter Marks: ")
    students[sid] = {"Name": name, "Marks": marks}
    print("Student added successfully")

def view_students():
    if not students:
        print("No records found")
    for sid, details in students.items():
        print(sid, details)

def search_student():
    sid = input("Enter Student ID to search: ")
    if sid in students:
        print(students[sid])
    else:
        print("Student not found")

while True:
    print("\n1.Add 2.View 3.Search 4.Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        break
    else:
        print("Invalid choice")
