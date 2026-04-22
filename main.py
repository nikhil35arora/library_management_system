from add_book import add_book
from issue_book import issue_book
from show_book import show_book
from return_book import return_book


def library():
    while True:
        print("\n========== Library Management System ==========")
        print("1. Add Book")
        print("2. Show Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_book()
        elif choice == "2":
            show_book()
        elif choice == "3":
            issue_book()
        elif choice == "4":
            return_book()
        elif choice == "5":
            print("Thank you for visiting the library.")
            break
        else:
            print("Invalid choice. Please select a valid option (1-5).")


library()
