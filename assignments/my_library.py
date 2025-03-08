import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# Create the books table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        book_id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        year_published INTEGER,
        genre TEXT
    )
''')
conn.commit()

# Function to add a book
def add_book(title, author, year_published, genre):
    cursor.execute("INSERT INTO books (title, author, year_published, genre) VALUES (?, ?, ?, ?)",
                   (title, author, year_published, genre))
    conn.commit()
    print("✅ Book added successfully!")

# Function to view all books
def view_books():
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    if books:
        print("\n📚 Library Collection:")
        for book in books:
            print(book)
    else:
        print("\n⚠️ No books found.")

# Function to search for a book by title
def search_books(title):
    cursor.execute("SELECT * FROM books WHERE title LIKE ?", ('%' + title + '%',))
    books = cursor.fetchall()
    if books:
        print("\n🔍 Search Results:")
        for book in books:
            print(book)
    else:
        print("\n⚠️ No matching books found.")

# Function to update book details
def update_book(book_id, title, author, year_published, genre):
    cursor.execute("UPDATE books SET title = ?, author = ?, year_published = ?, genre = ? WHERE book_id = ?",
                   (title, author, year_published, genre, book_id))
    conn.commit()
    print("✅ Book updated successfully!")

# Function to delete a book
def delete_book(book_id):
    cursor.execute("DELETE FROM books WHERE book_id = ?", (book_id,))
    conn.commit()
    print("✅ Book deleted successfully!")

# Interactive Menu
def menu():
    while True:
        print("\n📚 Library Management System")
        print("1️⃣ Add Book")
        print("2️⃣ View Books")
        print("3️⃣ Search Book")
        print("4️⃣ Update Book")
        print("5️⃣ Delete Book")
        print("6️⃣ Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            year_published = input("Enter year published: ")
            genre = input("Enter book genre: ")
            add_book(title, author, year_published, genre)

        elif choice == "2":
            view_books()

        elif choice == "3":
            title = input("Enter book title to search: ")
            search_books(title)

        elif choice == "4":
            book_id = input("Enter book ID to update: ")
            title = input("Enter new title: ")
            author = input("Enter new author: ")
            year_published = input("Enter new year published: ")
            genre = input("Enter new genre: ")
            update_book(book_id, title, author, year_published, genre)

        elif choice == "5":
            book_id = input("Enter book ID to delete: ")
            delete_book(book_id)

        elif choice == "6":
            print("👋 Exiting... Goodbye!")
            conn.close()
            break
        else:
            print("⚠️ Invalid choice, please try again!")

menu()
