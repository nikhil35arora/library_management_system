from datetime import date


# Book records are stored in a dictionary.
# Key: normalized book title (UPPERCASE)
# Value: metadata for availability and issue details
books = {}


def normalize_title(book_title):
    return book_title.strip().upper()


def calculate_fine(late_days):
    if late_days <= 0:
        return 0

    fine = 0
    for day in range(1, late_days + 1):
        week_number = ((day - 1) // 7) + 1
        multiplier = 1
        for value in range(1, week_number + 1):
            multiplier *= value
        fine += 10 * multiplier
    return fine


def issue_details(student_name, days_allowed):
    issued_on = date.today()
    due_date = issued_on.fromordinal(issued_on.toordinal() + days_allowed)
    return {
        "student_name": student_name.strip().title(),
        "issued_on": issued_on,
        "days_allowed": days_allowed,
        "due_date": due_date,
    }
