import json
try:
    students=[]
    with open("student.json", "r") as f:
        students = json.load(f)
except:
    students=[]

def check_roll_num_exists(roll_num):
    exists = False
    for s in students:
      if s["roll_num"] == input_roll_num:
        print("Student with this roll number already exists.")
        exists = True
        break
    return exists
def view_students():
    if not students:
        print("No students found.")
    else:
        print("\nList of Students:")
        for student in students:
            print(f"Roll Number: {student['roll_num']}, Name: {student['name']}, Department: {student['dept']}, CGPA: {student['cgpa']}")
    
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
        exists = check_roll_num_exists(input_roll_num)
        if exists:
            continue
        student["roll_num"] = input_roll_num
        student["name"] = input("Enter Name: ")
        student["dept"] = input("Enter Department: ")
        student["cgpa"] = input("Enter CGPA: ")
        students.append(student)
        with open("student.json", "w") as f:
           json.dump(students,f, indent=4)
    
        print("Student added successfully!")
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_roll_num = input("Enter Roll Number to search: ")
        found=  check_roll_num_exists(search_roll_num)
        if found:
            for student in students:
                if student["roll_num"] == search_roll_num:
                    print(f"Roll Number: {student['roll_num']}, Name: {student['name']}, Department: {student['dept']}, CGPA: {student['cgpa']}")
                    break
    elif choice == "4":
        

    if choice == "6":

        print("Thank you!")
        break



