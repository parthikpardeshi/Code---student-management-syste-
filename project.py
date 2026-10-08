# ============================================================
#              STUDENT MANAGEMENT SYSTEM
#                 PYTHON PROJECT
# ============================================================

students = []


# ============================================================
# 1. CALCULATE GRADE
# ============================================================

def calculate_grade(percentage):

    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B+"
    elif percentage >= 60:
        return "B"
    elif percentage >= 50:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "F"


# ============================================================
# 2. CALCULATE RESULT
# ============================================================

def calculate_result(marks):

    for mark in marks:
        if mark < 33:
            return "FAIL"

    return "PASS"


# ============================================================
# 3. CALCULATE TOTAL AND PERCENTAGE
# ============================================================

def calculate_percentage(marks):

    total = sum(marks)

    percentage = total / len(marks)

    return total, percentage


# ============================================================
# 4. ADD STUDENT
# ============================================================

def add_student():

    print("\n")
    print("=" * 60)
    print("                    ADD STUDENT")
    print("=" * 60)

    name = input("Enter Student Name: ")

    roll_no = input("Enter Roll Number: ")

    branch = input("Enter Branch: ")

    semester = input("Enter Semester: ")

    # Check duplicate roll number

    for student in students:

        if student["roll_no"] == roll_no:

            print("\nStudent with this Roll Number already exists!")

            return

    # Subjects

    subjects = [
        "Python",
        "Mathematics",
        "Physics",
        "English",
        "Environmental Studies"
    ]

    marks = []

    print("\nEnter marks out of 100:")

    for subject in subjects:

        while True:

            try:

                mark = float(input("Enter marks in " + subject + ": "))

                if mark >= 0 and mark <= 100:

                    marks.append(mark)

                    break

                else:

                    print("Marks must be between 0 and 100.")

            except ValueError:

                print("Please enter a valid number.")

    # Calculate result

    total, percentage = calculate_percentage(marks)

    grade = calculate_grade(percentage)

    result = calculate_result(marks)

    # Create student record

    student = {

        "name": name,

        "roll_no": roll_no,

        "branch": branch,

        "semester": semester,

        "subjects": subjects,

        "marks": marks,

        "total": total,

        "percentage": percentage,

        "grade": grade,

        "result": result
    }

    # Add record to list

    students.append(student)

    print("\n" + "=" * 60)

    print("Student record added successfully!")

    print("=" * 60)


# ============================================================
# 5. DISPLAY ONE STUDENT
# ============================================================

def display_student(student):

    print("\n")
    print("=" * 60)
    print("                  STUDENT REPORT")
    print("=" * 60)

    print("Student Name :", student["name"])

    print("Roll Number  :", student["roll_no"])

    print("Branch       :", student["branch"])

    print("Semester     :", student["semester"])

    print("-" * 60)

    print("Subject                  Marks")

    print("-" * 60)

    for i in range(len(student["subjects"])):

        print(
            f"{student['subjects'][i]:25} {student['marks'][i]}"
        )

    print("-" * 60)

    print("Total Marks  :", student["total"], "/ 500")

    print(
        "Percentage   :",
        round(student["percentage"], 2),
        "%"
    )

    print("Grade        :", student["grade"])

    print("Result       :", student["result"])

    print("=" * 60)


# ============================================================
# 6. VIEW ALL STUDENTS
# ============================================================

def view_all_students():

    print("\n")
    print("=" * 75)
    print("                       ALL STUDENTS")
    print("=" * 75)

    if len(students) == 0:

        print("No student records available.")

        return

    print(
        f"{'Roll No.':<12}"
        f"{'Name':<20}"
        f"{'Percentage':<15}"
        f"{'Grade':<10}"
        f"{'Result':<10}"
    )

    print("-" * 75)

    for student in students:

        print(
            f"{student['roll_no']:<12}"
            f"{student['name']:<20}"
            f"{student['percentage']:<15.2f}"
            f"{student['grade']:<10}"
            f"{student['result']:<10}"
        )

    print("=" * 75)


# ============================================================
# 7. SEARCH STUDENT
# ============================================================

def search_student():

    print("\n")
    print("=" * 60)
    print("                    SEARCH STUDENT")
    print("=" * 60)

    if len(students) == 0:

        print("No student records available.")

        return

    roll_no = input("Enter Roll Number to search: ")

    for student in students:

        if student["roll_no"] == roll_no:

            display_student(student)

            return

    print("\nStudent not found.")


# ============================================================
# 8. UPDATE STUDENT
# ============================================================

def update_student():

    print("\n")
    print("=" * 60)
    print("                    UPDATE STUDENT")
    print("=" * 60)

    if len(students) == 0:

        print("No student records available.")

        return

    roll_no = input("Enter Roll Number to update: ")

    for student in students:

        if student["roll_no"] == roll_no:

            print("\nStudent found!")

            print("\nEnter new details.")

            name = input(
                "Enter new name (press Enter to keep old): "
            )

            branch = input(
                "Enter new branch (press Enter to keep old): "
            )

            semester = input(
                "Enter new semester (press Enter to keep old): "
            )

            if name != "":

                student["name"] = name

            if branch != "":

                student["branch"] = branch

            if semester != "":

                student["semester"] = semester

            print("\nStudent information updated successfully!")

            return

    print("\nStudent not found.")


# ============================================================
# 9. UPDATE MARKS
# ============================================================

def update_marks():

    print("\n")
    print("=" * 60)
    print("                    UPDATE MARKS")
    print("=" * 60)

    if len(students) == 0:

        print("No student records available.")

        return

    roll_no = input("Enter Roll Number: ")

    for student in students:

        if student["roll_no"] == roll_no:

            print("\nStudent found!")

            print("\nEnter new marks:")

            for i in range(len(student["subjects"])):

                while True:

                    try:

                        mark = float(
                            input(
                                "Enter marks in "
                                + student["subjects"][i]
                                + ": "
                            )
                        )

                        if 0 <= mark <= 100:

                            student["marks"][i] = mark

                            break

                        else:

                            print(
                                "Marks must be between 0 and 100."
                            )

                    except ValueError:

                        print("Please enter a valid number.")

            # Recalculate everything

            total, percentage = calculate_percentage(
                student["marks"]
            )

            student["total"] = total

            student["percentage"] = percentage

            student["grade"] = calculate_grade(
                percentage
            )

            student["result"] = calculate_result(
                student["marks"]
            )

            print("\nMarks updated successfully!")

            return

    print("\nStudent not found.")


# ============================================================
# 10. DELETE STUDENT
# ============================================================

def delete_student():

    print("\n")
    print("=" * 60)
    print("                    DELETE STUDENT")
    print("=" * 60)

    if len(students) == 0:

        print("No student records available.")

        return

    roll_no = input("Enter Roll Number to delete: ")

    for student in students:

        if student["roll_no"] == roll_no:

            print("\nStudent Found!")

            print("Name:", student["name"])

            confirmation = input(
                "Are you sure you want to delete? (yes/no): "
            )

            if confirmation.lower() == "yes":

                students.remove(student)

                print("\nStudent deleted successfully!")

            else:

                print("\nDeletion cancelled.")

            return

    print("\nStudent not found.")


# ============================================================
# 11. SHOW TOPPER
# ============================================================

def show_topper():

    print("\n")
    print("=" * 60)
    print("                      CLASS TOPPER")
    print("=" * 60)

    if len(students) == 0:

        print("No student records available.")

        return

    topper = students[0]

    for student in students:

        if student["percentage"] > topper["percentage"]:

            topper = student

    display_student(topper)


# ============================================================
# 12. SORT STUDENTS
# ============================================================

def sort_students():

    print("\n")
    print("=" * 60)
    print("              STUDENTS BY PERCENTAGE")
    print("=" * 60)

    if len(students) == 0:

        print("No student records available.")

        return

    sorted_students = sorted(
        students,
        key=lambda student: student["percentage"],
        reverse=True
    )

    position = 1

    for student in sorted_students:

        print(
            position,
            ".",
            student["name"],
            "-",
            round(student["percentage"], 2),
            "%",
            "- Grade:",
            student["grade"]
        )

        position += 1


# ============================================================
# 13. CLASS STATISTICS
# ============================================================

def class_statistics():

    print("\n")
    print("=" * 60)
    print("                  CLASS STATISTICS")
    print("=" * 60)

    if len(students) == 0:

        print("No student records available.")

        return

    total_students = len(students)

    passed = 0

    failed = 0

    total_percentage = 0

    highest = students[0]

    lowest = students[0]

    for student in students:

        total_percentage += student["percentage"]

        if student["result"] == "PASS":

            passed += 1

        else:

            failed += 1

        if student["percentage"] > highest["percentage"]:

            highest = student

        if student["percentage"] < lowest["percentage"]:

            lowest = student

    average = total_percentage / total_students

    pass_percentage = (
        passed / total_students
    ) * 100

    print("Total Students :", total_students)

    print("Passed         :", passed)

    print("Failed         :", failed)

    print(
        "Class Average  :",
        round(average, 2),
        "%"
    )

    print(
        "Pass Percentage:",
        round(pass_percentage, 2),
        "%"
    )

    print(
        "Highest        :",
        highest["name"],
        "-",
        round(highest["percentage"], 2),
        "%"
    )

    print(
        "Lowest         :",
        lowest["name"],
        "-",
        round(lowest["percentage"], 2),
        "%"
    )


# ============================================================
# 14. SUBJECT PERFORMANCE
# ============================================================

def subject_performance():

    print("\n")
    print("=" * 60)
    print("                 SUBJECT PERFORMANCE")
    print("=" * 60)

    if len(students) == 0:

        print("No student records available.")

        return

    subjects = students[0]["subjects"]

    for i in range(len(subjects)):

        total = 0

        highest = 0

        lowest = 100

        for student in students:

            mark = student["marks"][i]

            total += mark

            if mark > highest:

                highest = mark

            if mark < lowest:

                lowest = mark

        average = total / len(students)

        print("\nSubject :", subjects[i])

        print(
            "Average :",
            round(average, 2)
        )

        print("Highest :", highest)

        print("Lowest  :", lowest)


# ============================================================
# 15. STUDENT COUNT
# ============================================================

def student_count():

    print("\n")
    print("=" * 60)
    print("                   STUDENT COUNT")
    print("=" * 60)

    print(
        "Total students registered:",
        len(students)
    )


# ============================================================
# 16. MAIN MENU
# ============================================================

def main_menu():

    while True:

        print("\n")

        print("*" * 65)

        print(
            "          STUDENT MANAGEMENT SYSTEM"
        )

        print("*" * 65)

        print("1.  Add Student")

        print("2.  View All Students")

        print("3.  Search Student")

        print("4.  Update Student Details")

        print("5.  Update Student Marks")

        print("6.  Delete Student")

        print("7.  Show Class Topper")

        print("8.  Sort Students by Percentage")

        print("9.  Class Statistics")

        print("10. Subject Performance")

        print("11. Student Count")

        print("12. Exit")

        print("*" * 65)

        choice = input("Enter your choice: ")

        if choice == "1":

            add_student()

        elif choice == "2":

            view_all_students()

        elif choice == "3":

            search_student()

        elif choice == "4":

            update_student()

        elif choice == "5":

            update_marks()

        elif choice == "6":

            delete_student()

        elif choice == "7":

            show_topper()

        elif choice == "8":

            sort_students()

        elif choice == "9":

            class_statistics()

        elif choice == "10":

            subject_performance()

        elif choice == "11":

            student_count()

        elif choice == "12":

            print("\n")
            print("=" * 65)
            print("Thank you for using Student Management System!")
            print("=" * 65)

            break

        else:

            print("\nInvalid choice!")

            print("Please enter a number between 1 and 12.")


# ============================================================
# PROGRAM START
# ============================================================

print("\n")

print("*" * 65)

print("              WELCOME TO STUDENT")
print("                MANAGEMENT SYSTEM")

print("*" * 65)

print("\nAll student records will be entered by the user.")

main_menu()