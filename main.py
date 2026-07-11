students = []
while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")
    

    choice = input("Enter your choice: ")
 
    if choice == "1":
        student = {"roll_num": "", "name": "", "dept": "", "cgpa": ""}
        input_roll_num = input("Enter Roll Number: ")
        exists = False
        for s in students:
            if s["roll_num"] == input_roll_num:
                print("Student with this roll number already exists.")
                exists = True
                break
        if exists:
            continue
        student["roll_num"] = input_roll_num
        student["name"] = input("Enter Name: ")
        student["dept"] = input("Enter Department: ")
        student["cgpa"] = input("Enter CGPA: ")
        students.append(student)
        print("Student added successfully!")
    if choice == "2":
        if not students:
            print("No students found.")
        else:
            print("\nList of Students:")
            for student in students:
                print(f"Roll Number: {student['roll_num']}, Name: {student['name']}, Department: {student['dept']}, CGPA: {student['cgpa']}")
        
    if choice == "6":

        print("Thank you!")
        break