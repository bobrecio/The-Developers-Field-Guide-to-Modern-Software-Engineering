import mysql.connector

db_config = {
    'host': 'mysql',            # This is the service name from docker-compose
    'user': 'exampleuser',
    'password': 'examplepass',
    'database': 'exampledb'
}

conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# Drop tables in dependency-safe order
cursor.execute("DROP TABLE IF EXISTS student_subjects")
cursor.execute("DROP TABLE IF EXISTS student_queries")
cursor.execute("DROP TABLE IF EXISTS student_year")
cursor.execute("DROP TABLE IF EXISTS subjects")
cursor.execute("DROP TABLE IF EXISTS students")

# Create students table
cursor.execute("""
    CREATE TABLE students (
        student_id INT PRIMARY KEY,
        name VARCHAR(50)
    )
""")

# Create student_year table (1:1 with students)
cursor.execute("""
    CREATE TABLE student_year (
        student_id INT PRIMARY KEY,
        academic_year VARCHAR(20),
        FOREIGN KEY (student_id) REFERENCES students(student_id)
    )
""")

# Create subjects table
cursor.execute("""
    CREATE TABLE subjects (
        subject_id INT PRIMARY KEY,
        name VARCHAR(50)
    )
""")

# Create student_subjects junction table (M:N)
cursor.execute("""
    CREATE TABLE student_subjects (
        student_id INT,
        subject_id INT,
        PRIMARY KEY (student_id, subject_id),
        FOREIGN KEY (student_id) REFERENCES students(student_id),
        FOREIGN KEY (subject_id) REFERENCES subjects(subject_id)
    )
""")

# Create student_queries table (1:M with students)
cursor.execute("""
    CREATE TABLE student_queries (
        query_id INT PRIMARY KEY,
        student_id INT,
        query_text VARCHAR(255),
        FOREIGN KEY (student_id) REFERENCES students(student_id)
    )
""")

# Insert sample students
cursor.execute("INSERT INTO students (student_id, name) VALUES (1, 'Alice')")
cursor.execute("INSERT INTO students (student_id, name) VALUES (2, 'Bob')")

# Insert student_year
cursor.execute("INSERT INTO student_year (student_id, academic_year) VALUES (1, '2025')")
cursor.execute("INSERT INTO student_year (student_id, academic_year) VALUES (2, '2025')")

# Insert subjects
cursor.execute("INSERT INTO subjects (subject_id, name) VALUES (101, 'Math')")
cursor.execute("INSERT INTO subjects (subject_id, name) VALUES (102, 'Science')")

# Insert student_subjects links (M:N)
cursor.execute("INSERT INTO student_subjects (student_id, subject_id) VALUES (1, 101)")
cursor.execute("INSERT INTO student_subjects (student_id, subject_id) VALUES (1, 102)")
cursor.execute("INSERT INTO student_subjects (student_id, subject_id) VALUES (2, 101)")

# Insert student_queries (1:M)
cursor.execute("INSERT INTO student_queries (query_id, student_id, query_text) VALUES (1, 1, 'How do I register for Math?')")
cursor.execute("INSERT INTO student_queries (query_id, student_id, query_text) VALUES (2, 1, 'Can I switch subjects?')")
cursor.execute("INSERT INTO student_queries (query_id, student_id, query_text) VALUES (3, 2, 'When is the Science exam?')")

# Commit changes and close
conn.commit()
cursor.close()
conn.close()

print("Tables created and populated successfully.")
