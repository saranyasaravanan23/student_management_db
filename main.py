from student import (
    add_student,
    view_students,
    view_student_by_id,
    search_student,
    update_student,
    delete_student
)

from course import (
    add_course,
    view_courses,
    update_course,
    delete_course,
    search_course
)

from result import (
    add_result,
    view_results,
    view_results_by_student,
    view_results_by_course
)

from reports import (
    all_students_courses_marks,
    highest_mark,
    average_marks,
    students_above_80,
    students_per_course,
    failed_students
)


def student_menu():
    while True:
        print("\n===== STUDENT MANAGEMENT =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. View Student By ID")
        print("4. Search Student By Name")
        print("5. Update Student")
        print("6. Delete Student")
        print("7. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            view_student_by_id()
        elif choice == "4":
            search_student()
        elif choice == "5":
            update_student()
        elif choice == "6":
            delete_student()
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please try again.")


def course_menu():
    while True:
        print("\n===== COURSE MANAGEMENT =====")
        print("1. Add Course")
        print("2. View All Courses")
        print("3. Update Course")
        print("4. Delete Course")
        print("5. Search Course By Name")
        print("6. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_course()
        elif choice == "2":
            view_courses()
        elif choice == "3":
            update_course()
        elif choice == "4":
            delete_course()
        elif choice == "5":
            search_course()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")


def result_menu():
    while True:
        print("\n===== RESULT MANAGEMENT =====")
        print("1. Add Result")
        print("2. View All Results")
        print("3. View Results By Student")
        print("4. View Results By Course")
        print("5. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_result()
        elif choice == "2":
            view_results()
        elif choice == "3":
            view_results_by_student()
        elif choice == "4":
            view_results_by_course()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")


def reports_menu():
    while True:
        print("\n===== REPORTS =====")
        print("1. All Students + Course + Marks")
        print("2. Highest Mark")
        print("3. Average Marks")
        print("4. Students Above 80")
        print("5. Number of Students Per Course")
        print("6. Failed Students")
        print("7. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            all_students_courses_marks()
        elif choice == "2":
            highest_mark()
        elif choice == "3":
            average_marks()
        elif choice == "4":
            students_above_80()
        elif choice == "5":
            students_per_course()
        elif choice == "6":
            failed_students()
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please try again.")


def main():
    while True:
        print("\n======================================")
        print(" STUDENT COURSE & RESULT MANAGEMENT")
        print("======================================")
        print("1. Student Management")
        print("2. Course Management")
        print("3. Result Management")
        print("4. Reports")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            student_menu()
        elif choice == "2":
            course_menu()
        elif choice == "3":
            result_menu()
        elif choice == "4":
            reports_menu()
        elif choice == "5":
            print("Thank you! Goodbye.")
            break
        else:
            print("Invalid choice. Please enter 1-5.")


if __name__ == "__main__":
    main()