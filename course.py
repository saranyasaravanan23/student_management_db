from database import get_connection


def add_course():
    name = input("Enter course name: ").strip()
    duration = input("Enter course duration: ").strip()

    if not name or not duration:
        print("Course name and duration cannot be empty.")
        return

    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO courses (course_name, duration)
            VALUES (%s, %s)
            """,
            (name, duration)
        )

        connection.commit()
        print("Course added successfully!")

    except Exception as error:
        print("Error:", error)

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals():
            connection.close()


def view_courses():
    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM courses")
        courses = cursor.fetchall()

        if not courses:
            print("No courses found.")
            return

        print("\nID | Course Name | Duration")
        print("-" * 40)

        for course in courses:
            print(course)

    except Exception as error:
        print("Error:", error)

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals():
            connection.close()


def update_course():
    try:
        course_id = int(input("Enter course ID to update: "))

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "SELECT * FROM courses WHERE course_id = %s",
            (course_id,)
        )

        if not cursor.fetchone():
            print("Course not found.")
            return

        name = input("Enter new course name: ").strip()
        duration = input("Enter new duration: ").strip()

        cursor.execute(
            """
            UPDATE courses
            SET course_name = %s, duration = %s
            WHERE course_id = %s
            """,
            (name, duration, course_id)
        )

        connection.commit()
        print("Course updated successfully!")

    except ValueError:
        print("Course ID must be a number.")

    except Exception as error:
        print("Error:", error)

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals():
            connection.close()


def delete_course():
    try:
        course_id = int(input("Enter course ID to delete: "))

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "SELECT * FROM courses WHERE course_id = %s",
            (course_id,)
        )

        if not cursor.fetchone():
            print("Course not found.")
            return

        confirm = input("Are you sure? (yes/no): ").lower()

        if confirm == "yes":
            cursor.execute(
                "DELETE FROM courses WHERE course_id = %s",
                (course_id,)
            )

            connection.commit()
            print("Course deleted successfully!")
        else:
            print("Delete cancelled.")

    except ValueError:
        print("Course ID must be a number.")

    except Exception as error:
        print("Error:", error)

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals():
            connection.close()


def search_course():
    name = input("Enter course name to search: ").strip()

    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            "SELECT * FROM courses WHERE course_name LIKE %s",
            (f"%{name}%",)
        )

        courses = cursor.fetchall()

        if courses:
            for course in courses:
                print(course)
        else:
            print("No courses found.")

    except Exception as error:
        print("Error:", error)

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals():
            connection.close()