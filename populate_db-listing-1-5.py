import mysql.connector

try:
    # Database connection details
    db_config = {
        'host': 'mysql',            # This is the service name from docker-compose
        'user': 'exampleuser',
        'password': 'examplepass',
        'database': 'exampledb'
    }
    # Connect to the database
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Check if the table already exists
    cursor.execute("SHOW TABLES LIKE 'books'")
    result = cursor.fetchone()

    if result:
        print("Table 'books' already exists.")
    else:
        # Create table if it doesn't exist
        create_table_query = """
        CREATE TABLE books (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(100),
            author VARCHAR(100),
	    year char(4),
            slug VARCHAR(100)
        )
        """
        cursor.execute(create_table_query)
        conn.commit()
        print("Table 'books' created successfully.")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
