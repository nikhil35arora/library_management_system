from utils import books


def show_book():
    print("\n--- Library Books ---")
    if not books:
        print("No books available in the library records.")
        return

    for index, record in enumerate(books.values(), start=1):
        status = "Available" if record["available"] else "Issued"
        print(f"{index}. {record['title']} | Status: {status}")
        if not record["available"] and record["issued_to"]:
            issue = record["issued_to"]
            print(
                f"   Issued To: {issue['student_name']} | "
                f"Issued On: {issue['issued_on']} | Due Date: {issue['due_date']}"
            )