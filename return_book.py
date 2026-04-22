from datetime import date

from utils import books, calculate_fine, normalize_title


def return_book():
    print("\n--- Return Book ---")
    book_name = input("Enter book title to return: ").strip()
    book_key = normalize_title(book_name)

    if book_key not in books:
        print(f"'{book_name}' does not exist in library records.")
        return

    if books[book_key]["available"] or books[book_key]["issued_to"] is None:
        print(f"'{books[book_key]['title']}' is not currently issued.")
        return

    issue = books[book_key]["issued_to"]
    today = date.today()
    late_days = (today - issue["due_date"]).days
    fine = calculate_fine(late_days)

    books[book_key]["available"] = True
    books[book_key]["issued_to"] = None

    print(f"Book returned successfully: {books[book_key]['title']}")
    print(f"Issued To: {issue['student_name']}")
    print(f"Issued On: {issue['issued_on']} | Due Date: {issue['due_date']}")
    print(f"Returned On: {today}")

    if fine > 0:
        print(f"Late by {late_days} day(s). Fine to be paid: Rs.{fine}")
    else:
        print("Returned within the allotted period. No fine applied.")
