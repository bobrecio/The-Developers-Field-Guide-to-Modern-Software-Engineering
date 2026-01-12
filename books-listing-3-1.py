import mysql.connector

db_config = {
    'host': 'mysql',            # This is the service name from docker-compose
    'user': 'exampleuser',
    'password': 'examplepass',
    'database': 'exampledb'
}
# Connect to the database
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# Define some books as dictionaries (title, author, year)
book1 = {"title": "1984", "author": "Orwell", "year": 1949}
book2 = {"title": "Brave New World", "author": "Huxley", "year": 1932}

# A list to store books
library = [book1, book2]

# A tuple representing a new book (title, author, year)
new_book_data = ("Fahrenheit 451", "Bradbury", 1953)

# Convert the tuple to a dictionary and add to the list
new_book = {"title": new_book_data[0], "author": new_book_data[1], "year": new_book_data[2]}
library.append(new_book)

def add_slug(books):
    for book in books:
        # Use replace to create a slug from the title
        slug = book["title"].lower().replace(" ", "-")
        book['slug'] = slug
    return books

# Function to print book info
def print_books(books):
    for book in books:
        # Use upper to emphasize title
        title_upper = book["title"].upper()
        status = "classic" if book["year"] < 1970 else "modern"
        print(f"{title_upper} by {book['author']} ({book['year']}) - {status} [slug: {book['slug']}]")

# Built-in functions: len(), sorted()
print(f"\nYou have {len(library)} books in your library.\n")

# Sort books by year and print them
print("Your books (sorted by year):")
sorted_books = sorted(library, key=lambda b: b["year"])
sorted_books = add_slug(sorted_books)
print_books(sorted_books)


for entry in sorted_books:
    print(entry)
    cursor.execute("""
        INSERT INTO books (title, author, year, slug)
        VALUES (%s, %s, %s, %s)
    """, (entry["title"], entry["author"], entry["year"], entry['slug']))
    conn.commit()



