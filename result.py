from database import get_connection


def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"


def add_result():
    try:
        student_id = int(input("Enter student ID: "))
        course_id = int(input("Enter course ID: "))
        marks = float(input("Enter marks (0-100): "))

        if marks < 0 or marks > 100:
            print("Marks must be between 0 and 100.")
            return

        connection = get_connection()
        cursor = connection.cursor()

        # Check student exists
        cursor.execute(
            "SELECT student_id FROM students WHERE student_id = %s",
            (student_id,)
        )

        if not cursor.fetchone():
            print("Student not found.")
            return

        # Check course exists
        cursor.execute(
            "SELECT course_id FROM courses WHERE course_id = %s",
            (course_id,)
        )

        if not cursor.fetchone():
            print("Course not found.")
            return

        grade = calculate_grade(marks)

        cursor.execute(
            """
            INSERT INTO results (student_id, course_id, marks, grade)
            VALUES (%s, %s, %s, %s)
            """,
            (student_id, course_id, marks, grade)
        )

        connection.commit()

        print("Result added successfully!")
        print("Grade:", grade)

    except ValueError:
        print("Student ID, Course ID and marks must be valid numbers.")

    except Exception as error:
        print("Error:", error)

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals():
            connection.close()


def view_results():
    try:
        connection = get_connection()
        cursor = connection.cursor()

        query = """
        SELECT
            r.result_id,
            s.student_name,
            c.course_name,
            r.marks,
            r.grade
        FROM results r
        INNER JOIN students s ON r.student_id = s.student_id
        INNER JOIN courses c ON r.course_id = c.course_id
        """

        cursor.execute(query)
        results = cursor.fetchall()

        if not results:
            print("No results found.")
            return

        print("\nID | Student | Course | Marks | Grade")
        print("-" * 60)

        for result in results:
            print(result)

    except Exception as error:
        print("Error:", error)

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals():
            connection.close()


def view_results_by_student():
    try:
        student_id = int(input("Enter student ID: "))

        connection = get_connection()
        cursor = connection.cursor()

        query = """
        SELECT
            r.result_id,
            s.student_name,
            c.course_name,
            r.marks,
            r.grade
        FROM results r
        INNER JOIN students s ON r.student_id = s.student_id
        INNER JOIN courses c ON r.course_id = c.course_id
        WHERE r.student_id = %s
        """

        cursor.execute(query, (student_id,))
        results = cursor.fetchall()

        if results:
            for result in results:
                print(result)
        else:
            print("No results found for this student.")

    except ValueError:
        print("Student ID must be a number.")

    except Exception as error:
        print("Error:", error)

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals():
            connection.close()


def view_results_by_course():
    try:
        course_id = int(input("Enter course ID: "))

        connection = get_connection()
        cursor = connection.cursor()

        query = """
        SELECT
            r.result_id,
            s.student_name,
            c.course_name,
            r.marks,
            r.grade
        FROM results r
        INNER JOIN students s ON r.student_id = s.student_id
        INNER JOIN courses c ON r.course_id = c.course_id
        WHERE r.course_id = %s
        """

        cursor.execute(query, (course_id,))
        results = cursor.fetchall()

        if results:
            for result in results:
                print(result)
        else:
            print("No results found for this course.")

    except ValueError:
        print("Course ID must be a number.")

    except Exception as error:
        print("Error:", error)

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals():
            connection.close()