stud_dict = {'Alice' : 85, 'Bob' : 92, 'Charlie' : 78, 'David' : 90, 'Eva' : 88}
print("1. Adding a new student and grade")
print("2. Updating an existing student's grade")
print("3. Printing all students and their grades")

choice  = input("Enter Choice: ")
if choice == '1':
    name = input("Enter student name: ")
    grade = int(input("Enter student grade: "))
    stud_dict[name] = grade
    print(f"Added {name} with grade {grade}.")

elif choice == '2':
    name = input("Enter student name to update: ")
    if name in stud_dict:
        grade = int(input("Enter new grade: "))
        stud_dict[name] = grade
        print(f"Updated {name}'s grade to {grade}.")
    else:
        print(f"Student {name} not found.")

elif choice == '3':
    print("Student Grades:")
    for name, grade in stud_dict.items():
        print(f"{name}: {grade}")

else:
    print("Invalid choice.")