from utils import books, issue_details, normalize_title


def issue_book():
    print("\n--- Issue Book ---")
    book_name = input("Enter book title to issue: ").strip()
    book_key = normalize_title(book_name)

    if book_key not in books:
        print(f"'{book_name}' does not exist in library records.")
        return

    if not books[book_key]["available"]:
        current_student = books[book_key]["issued_to"]["student_name"]
        print(f"Book is already issued to {current_student}.")
        return

    student_name = input("Enter student name: ").strip()
    if not student_name:
        print("Student name cannot be empty.")
        return

    try:
        days_allowed = int(input("Issued for how many days? ").strip())
    except ValueError:
        print("Please enter a valid number of days.")
        return

    if days_allowed <= 0:
        print("Days must be greater than 0.")
        return

    books[book_key]["available"] = False
    books[book_key]["issued_to"] = issue_details(student_name, days_allowed)

    issue = books[book_key]["issued_to"]
    print(f"Book issued successfully: {books[book_key]['title']}")
    print(
        f"Issued To: {issue['student_name']} | "
        f"Issued On: {issue['issued_on']} | Due Date: {issue['due_date']}"
    )
    print("Fine Notice:")
    print("Week 1  -> Rs.10/day/book")
    print("Week 2  -> Rs.20/day/book")
    print("Week 3  -> Rs.60/day/book")
    print("Week N  -> Rs.10 x (1*2*...*N)/day/book")
