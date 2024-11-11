# An empty dictionary to store student names and their marks
students_grade = {
    'asfand': {'Core Python': 100, 'Machine Learning': 90, 'Data Science': 90},
    'faisal': {'Core Python': 80, 'Machine Learning': 65, 'Data Science': 50},
    'asad': {'Core Python': 45, 'Machine Learning': 35, 'Data Science': 40},
}

# This loop will run until the user enters 9 to exit
while True:
    print("\nI Hope, you are in good health")
    print("\nPress any number to perform the corresponding task:")
    print("1. For Adding Student marks")
    print("2. For updating marks of any student")
    print("3. For Delete any Student From data")
    print("4. For View the marks of student")
    print("5. For Count Total Student Present in Data")
    print("6. For inquire about the marks for any subject of a student")
    print("7. For Checking grades (A+, A, B+, B, C, Fail) of all students")
    print("8. For Checking failed students (marks below 50)")
    print("9. For Exit the app")

    # Taking number from user to perform the desired task
    task = int(input("\nEnter the number of the task you want to perform: "))

    # Task 1: Adding a student to students_grade dictionary
    if task == 1:
        name = input("Enter the name you want to add: ").lower()  # Convert name to lowercase
        if name in students_grade:
            print(f"The name {name} already exists in Data")
        else:
            # Input marks for each subject
            core_python = int(input("Enter marks of Core Python: "))
            machine_learning = int(input("Enter marks of Machine Learning: "))
            data_science = int(input("Enter marks of Data Science: "))

            # Check if marks are within the valid range
            if 0 <= core_python <= 100 and 0 <= data_science <= 100 and 0 <= machine_learning <= 100:
                # Add student data to the dictionary
                students_grade[name] = {'Core Python': core_python, 'Machine Learning': machine_learning, 'Data Science': data_science}
                print(f"The name {name} is added successfully")
                print(students_grade)
            else:
                print("\nPlease Enter Marks between 0-100")

    # Task 2: Updating marks of a student
    elif task == 2:
        update_name = input("Enter the name which you want to update: ").lower()
        if update_name in students_grade:
            # Input new marks for each subject
            updated_core_python = int(input("Enter marks of Core Python: "))
            updated_machine_learning = int(input("Enter marks of Machine Learning: "))
            updated_data_science = int(input("Enter marks of Data Science: "))

            # Check if updated marks are within the valid range
            if 0 <= updated_core_python <= 100 and 0 <= updated_data_science <= 100 and 0 <= updated_machine_learning <= 100:
                # Update student data in the dictionary
                students_grade[update_name] = {'Core Python': updated_core_python, 'Machine Learning': updated_machine_learning, 'Data Science': updated_data_science}
                print(f"The name {update_name} is updated successfully")
                print(students_grade[update_name])
            else:
                print("\nPlease Enter Marks between 0-100")
        else:
            print(f"The name {update_name} is not in our Data")

    # Task 3: Deleting a student from the data
    elif task == 3:
        del_name = input("Enter the name which you want to delete: ").lower()
        if del_name in students_grade:
            del students_grade[del_name]  # Remove student from dictionary
            print(f"The name {del_name} is deleted successfully")
            print(students_grade)
        else:
            print(f"The Name {del_name} is not available in Data")

    # Task 4: Viewing a student's marks
    elif task == 4:
        view_name = input("Enter the name which you want to view: ").lower()
        if view_name in students_grade:
            print(f"The info of {view_name} is below\n")
            print(students_grade[view_name])
        else:
            print(f"The name {view_name} is not available in Data")
    
    # Task 5: Counting total students present in data
    elif task == 5:
        print(len(students_grade))

    # Task 6: Marks in any Subjects
    elif task == 6:
        mark_of_stdent = input("Enter the Name to know the Subjects marks of student: ").lower()
    
        if mark_of_stdent in students_grade:
            subject = input("Enter the Name of Subject: ")
            subject_marks = students_grade[mark_of_stdent][subject]
            print(f"The Student {mark_of_stdent} marks in {subject} is {subject_marks}")

    # Task 7: Checking grades of all students
    elif task == 7:
        print("\n--- Grades of all students ---")
        for student, subjects in students_grade.items():
            print(f"\nStudent: {student.capitalize()}")
            for subject, marks in subjects.items():
                if marks >= 90:
                    grade = 'A+'
                elif marks >= 80:
                    grade = 'A'
                elif marks >= 70:
                    grade = 'B+'
                elif marks >= 60:
                    grade = 'B'
                elif marks >= 50:
                    grade = 'C'
                else:
                    grade = 'Fail'
                print(f"{subject}: Marks = {marks}, Grade = {grade}")

    # Task 8: Checking failed students (marks below 50)
    elif task == 8:
        print("\n--- Failed Students (Marks below 50) ---")
        failed_students = False
        for student, subjects in students_grade.items():
            for subject, marks in subjects.items():
                if marks < 50:
                    print(f"Student: {student.capitalize()}, Subject: {subject}, Marks: {marks} (Fail)")
                    failed_students = True
        if not failed_students:
            print("No students have marks below 50")

    # Task 9: Exiting the app
    elif task == 9:
        print("You exited the app\nTHANK YOU")
        break

    else:
        print("Please Choose Number of Given Task")
