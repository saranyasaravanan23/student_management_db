from database import get_connection


def add_student():
    name = input("Enter student name: ").strip()
    email = input("Enter email: ").strip()
    phone = input("Enter phone: ").strip()
    dob = input("Enter date of birth (YYYY-MM-DD): ").strip()

    if not name:
        print("Student name cannot be empty.")
        return

    if "@" not in email or "." not in email:
        print("Invalid email.")
        return

    try:
        connection = get_connection()
        cursor = connection.cursor()

        query = """
        INSERT INTO students
        (student_name, email, phone, date_of_birth)
        VALUES (%s, %s, %s, %s)
        """

        cursor.execute(query, (name, email, phone, dob))
        connection.commit()

        print("Student added successfully!")

    except Exception as error:
        print("Error:", error)

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals():
            connection.close()


def view_students():
    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()

        if not students:
            print("No students found.")
            return

        print("\nID | Name | Email | Phone | DOB")
        print("-" * 70)

        for student in students:
            print(student)

    except Exception as error:
        print("Error:", error)

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals():
            connection.close()


def view_student_by_id():
    try:
        student_id = int(input("Enter student ID: "))

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "SELECT * FROM students WHERE student_id = %s",
            (student_id,)
        )

        student = cursor.fetchone()

        if student:
            print("Student:", student)
        else:
            print("Student not found.")

    except ValueError:
        print("Student ID must be a number.")

    except Exception as error:
        print("Error:", error)

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals():
            connection.close()


def search_student():
    name = input("Enter student name to search: ").strip()

    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "SELECT * FROM students WHERE student_name LIKE %s",
            (f"%{name}%",)
        )

        students = cursor.fetchall()

        if students:
            for student in students:
                print(student)
        else:
            print("No students found.")

    except Exception as error:
        print("Error:", error)

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals():
            connection.close()


def update_student():
    try:
        student_id = int(input("Enter student ID to update: "))

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "SELECT * FROM students WHERE student_id = %s",
            (student_id,)
        )

        if not cursor.fetchone():
            print("Student not found.")
            return

        name = input("Enter new name: ").strip()
        email = input("Enter new email: ").strip()
        phone = input("Enter new phone: ").strip()

        cursor.execute(
            """
            UPDATE students
            SET student_name = %s, email = %s, phone = %s
            WHERE student_id = %s
            """,
            (name, email, phone, student_id)
        )

        connection.commit()
        print("Student updated successfully!")

    except ValueError:
        print("Student ID must be a number.")

    except Exception as error:
        print("Error:", error)

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals():
            connection.close()


def delete_student():
    try:
        student_id = int(input("Enter student ID to delete: "))

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "SELECT * FROM students WHERE student_id = %s",
            (student_id,)
        )

        if not cursor.fetchone():
            print("Student not found.")
            return

        confirm = input("Are you sure? (yes/no): ").lower()

        if confirm == "yes":
            cursor.execute(
                "DELETE FROM students WHERE student_id = %s",
                (student_id,)
            )
            connection.commit()
            print("Student deleted successfully!")
        else:
            print("Delete cancelled.")

    except ValueError:
        print("Student ID must be a number.")

    except Exception as error:
        print("Error:", error)

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals():
            connection.close()