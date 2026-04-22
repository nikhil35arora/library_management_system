# Library Management System - Python 📚

A comprehensive, modular Library Management System designed to handle book inventory, student issuance, and automated fine calculation. This system utilizes a clean command-line interface and focuses on precise date management and a dynamic, tiered fine structure.

---

## 🌟 Key Features

### 📖 Inventory Management
* **Book Entry**: Add new titles to the library records with automatic title normalization to prevent duplicate entries.
* **Real-time Status**: View a complete list of books showing whether they are "Available" or "Issued".
* **Metadata Tracking**: When a book is issued, the system displays the student's name, the issue date, and the specific due date.

### ✍️ Issuance & Returns
* **Smart Issuing**: Assign books to students for a specific number of days.
* **Validation**: Prevents issuing books that are already out or adding empty book/student names.
* **Automated Returns**: Updates availability status immediately upon return and calculates performance based on the due date.

### 💰 Dynamic Fine Engine
The system features a unique, non-linear fine calculation for late returns:
* **Week 1**: Rs. 10/day.
* **Week 2**: Rs. 20/day.
* **Week 3**: Rs. 60/day.
* **Week N**: Calculated using a factorial-based multiplier: $10 \times N!$ per day.

---

## 📁 Project Structure

This project follows high-quality modular programming standards by separating functions into dedicated files:

| File | Role |
| :--- | :--- |
| **`main.py`** | The central menu hub for user interaction. |
| **`utils.py`** | Core utilities: fine logic, date formatting, and the global book database. |
| **`add_book.py`** | Logic for expanding the library inventory. |
| **`show_book.py`** | Formats and displays the current library state. |
| **`issue_book.py`** | Manages the transition of books from library to student. |
| **`return_book.py`** | Handles returns, date comparisons, and fine assessment. |

---

## 🚀 Getting Started

### Prerequisites
* **Python 3.x** installed on your machine.

### Execution
1.  Save all modules in a single directory.
2.  Launch the system via the terminal:
    ```bash
    python main.py
    ```

---

## 🛠️ Technical Details

* **Date Handling**: Uses Python's `datetime` module to accurately track `issued_on` and `due_date`.
* **Data Normalization**: Book titles are normalized to uppercase keys to ensure "The Great Gatsby" and "the great gatsby" are recognized as the same book.
* **Input Safety**: Includes error handling for non-numeric input when entering the number of days allowed.

---

## 📜 License
This project is open-source and intended for educational use. Feel free to modify and expand its features!
