# Student Course & Result Management System

## Project Objective

This is a console-based Student Course & Result Management System developed using Python and MySQL.

The system is used to manage students, courses, marks, grades, and generate useful reports through a menu-driven console application.

## Technologies Used

- Python
- MySQL
- SQL
- MySQL Connector

## Features

### Student Management

- Add Student
- View All Students
- View Student By ID
- Search Student By Name
- Update Student
- Delete Student

### Course Management

- Add Course
- View All Courses
- Update Course
- Delete Course
- Search Course By Name

### Result Management

- Add Result
- View All Results
- View Results By Student
- View Results By Course
- Automatic Grade Calculation

### Reports

The system provides the following reports:

1. All Students with Course and Marks
2. Highest Mark
3. Average Marks
4. Students who scored above 80
5. Number of Students in each Course
6. Failed Students

## Grade Calculation

| Marks | Grade |
|---|---|
| 90 - 100 | A+ |
| 80 - 89 | A |
| 70 - 79 | B |
| 60 - 69 | C |
| 50 - 59 | D |
| Below 50 | F |

## Database

Database Name:

`student_management_db`

### Students Table

| Column | Description |
|---|---|
| student_id | Primary Key |
| student_name | Student Name |
| email | Unique Email |
| phone | Phone Number |
| date_of_birth | Date of Birth |

### Courses Table

| Column | Description |
|---|---|
| course_id | Primary Key |
| course_name | Unique Course Name |
| duration | Course Duration |

### Results Table

| Column | Description |
|---|---|
| result_id | Primary Key |
| student_id | Foreign Key |
| course_id | Foreign Key |
| marks | Student Marks |
| grade | Automatically Calculated Grade |

### Table Relationship

Students → Results ← Courses

The `results` table connects students and courses using foreign keys.

## SQL Concepts Used

- CREATE DATABASE
- CREATE TABLE
- INSERT
- SELECT
- UPDATE
- DELETE
- WHERE
- LIKE
- BETWEEN
- ORDER BY
- COUNT()
- AVG()
- MAX()
- GROUP BY
- INNER JOIN

## Input Validation

The application validates:

- Student name cannot be empty
- Email format
- Student ID must be an integer
- Course ID must be an integer
- Marks must be between 0 and 100
- Student existence
- Course existence
- Invalid menu choices
- Invalid numeric input

## Exception Handling

The application uses exception handling to manage invalid user input and database errors without crashing the program.

## Project Structure

```text
student_management_system/
│
├── main.py
├── database.py
├── student.py
├── course.py
├── result.py
├── reports.py
├── schema.sql
└── README.md