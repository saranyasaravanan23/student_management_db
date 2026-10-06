import mysql.connector


def get_connection():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="User12345",
        database="student_management_db",
        port=3306,
        use_pure=True,
        connection_timeout=5
    )


if __name__ == "__main__":
    try:
        connection = get_connection()
        print("MySQL Database Connected Successfully!")
        connection.close()
    except mysql.connector.Error as error:
        print("Database connection failed:", error)