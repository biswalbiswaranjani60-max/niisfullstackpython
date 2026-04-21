students = []

def add_student():
    roll = int(input("Enter Roll Number: "))
    name = input("Enter Name: ")
    marks = float(input("Enter Marks: "))
    
    student = {
        "roll": roll,
        "name": name,
        "marks": marks
    }
    
    students.append(student)
    print("Student added successfully!\n")

def display_students():
    if not students:
        print("No records found!\n")
        return
    
    for s in students:
        print(f"Roll: {s['roll']}, Name: {s['name']}, Marks: {s['marks']}")
    print()

def search_student():
    roll = int(input("Enter Roll Number to search: "))
    
    for s in students:
        if s["roll"] == roll:
            print("Student Found!")
            print(f"Name: {s['name']}, Marks: {s['marks']}\n")
            return
    
    print("Student not found!\n")

def delete_student():
    roll = int(input("Enter Roll Number to delete: "))
    
    for s in students:
        if s["roll"] == roll:
            students.remove(s)
            print("Student deleted successfully!\n")
            return
    
    print("Student not found!\n")

# Main Program
while True:
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Exiting program...")
        break
    else:
        print("Invalid choice!\n")