from database import get_connection


def all_students_courses_marks():
    try:
        connection = get_connection()
        cursor = connection.cursor()

        query = """
        SELECT
            s.student_id,
            s.student_name,
            c.course_name,
            r.marks,
            r.grade
        FROM students s
        INNER JOIN results r ON s.student_id = r.student_id
        INNER JOIN courses c ON r.course_id = c.course_id
        ORDER BY s.student_id
        """

        cursor.execute(query)
        rows = cursor.fetchall()

        print("\n--- All Students, Courses and Marks ---")

        if not rows:
            print("No data found.")
            return

        for row in rows:
            print(row)

    except Exception as error:
        print("Error:", error)

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals():
            connection.close()


def highest_mark():
    try:
        connection = get_connection()
        cursor = connection.cursor()

        query = """
        SELECT
            s.student_name,
            c.course_name,
            r.marks
        FROM results r
        INNER JOIN students s ON r.student_id = s.student_id
        INNER JOIN courses c ON r.course_id = c.course_id
        WHERE r.marks = (SELECT MAX(marks) FROM results)
        """

        cursor.execute(query)
        rows = cursor.fetchall()

        print("\n--- Highest Mark ---")

        if rows:
            for row in rows:
                print(row)
        else:
            print("No results found.")

    except Exception as error:
        print("Error:", error)

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals():
            connection.close()


def average_marks():
    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT AVG(marks) FROM results")
        result = cursor.fetchone()

        print("\n--- Average Marks ---")

        if result[0] is not None:
            print("Average Marks:", round(float(result[0]), 2))
        else:
            print("No marks available.")

    except Exception as error:
        print("Error:", error)

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals():
            connection.close()


def students_above_80():
    try:
        connection = get_connection()
        cursor = connection.cursor()

        query = """
        SELECT
            s.student_name,
            c.course_name,
            r.marks
        FROM results r
        INNER JOIN students s ON r.student_id = s.student_id
        INNER JOIN courses c ON r.course_id = c.course_id
        WHERE r.marks > 80
        """

        cursor.execute(query)
        rows = cursor.fetchall()

        print("\n--- Students with Marks Above 80 ---")

        if rows:
            for row in rows:
                print(row)
        else:
            print("No students found.")

    except Exception as error:
        print("Error:", error)

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals():
            connection.close()


def students_per_course():
    try:
        connection = get_connection()
        cursor = connection.cursor()

        query = """
        SELECT
            c.course_name,
            COUNT(DISTINCT r.student_id) AS student_count
        FROM courses c
        LEFT JOIN results r ON c.course_id = r.course_id
        GROUP BY c.course_id, c.course_name
        """

        cursor.execute(query)
        rows = cursor.fetchall()

        print("\n--- Number of Students Per Course ---")

        for row in rows:
            print(row)

    except Exception as error:
        print("Error:", error)

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals():
            connection.close()


def failed_students():
    try:
        connection = get_connection()
        cursor = connection.cursor()

        query = """
        SELECT
            s.student_name,
            c.course_name,
            r.marks,
            r.grade
        FROM results r
        INNER JOIN students s ON r.student_id = s.student_id
        INNER JOIN courses c ON r.course_id = c.course_id
        WHERE r.marks < 50
        """

        cursor.execute(query)
        rows = cursor.fetchall()

        print("\n--- Failed Students ---")

        if rows:
            for row in rows:
                print(row)
        else:
            print("No failed students.")

    except Exception as error:
        print("Error:", error)

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals():
            connection.close()