from utils import books, normalize_title


def add_book():
    print("\n--- Add Book ---")
    book_name = input("Enter book title: ").strip()
    if not book_name:
        print("Book title cannot be empty.")
        return

    book_key = normalize_title(book_name)
    if book_key in books:
        print(f"'{book_name}' already exists in records.")
        return

    books[book_key] = {
        "title": book_name.strip().title(),
        "available": True,
        "issued_to": None,
    }
    print(f"Book added successfully: {books[book_key]['title']}")