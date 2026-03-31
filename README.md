# Finance-Tracker
## Project Overview

This project is a **command-line based Expense Tracker** developed in Python.
It allows users to store, view, and search their monthly expenses. The system keeps track of expenses such as item name, price, and date, and stores them in a local SQLite database.

The project is developed as part of the **Fundamentals of AI/ML course** and demonstrates concepts such as search strategies, knowledge representation, and modular program design.

---

## Features

- Store expenses for different months
- View stored expenses in a formatted table
- Search for a specific expense item
- Graphical visualization of expenses
- Bar chart for individual month expenses
- Bar chart comparing total expenses across months
- Data persistence using SQLite database
- Command line interface execution

---

## Project Structure

```
Expense-Tracker
│
├── main.py        # Main program that runs the menu system
├── store.py       # Handles storing expenses in the database
├── view.py        # Displays stored expense tables
├── search.py      # Searches for specific expense records
├── expenses.db    # SQLite database file (generated automatically)
└── README.md
```

---

## Technologies Used

* Python
* SQLite
* Tabulate (for formatted table output)
* Command Line Interface

---

## AI Concepts Used

### 1. Search Strategy

The project implements a **Linear Search** approach to locate a specific expense item in the database.

* **State Space:** All stored expense records
* **Initial State:** First record in the table
* **Goal State:** Record that matches the user query
* **Search Method:** Sequential search through records

### 2. Knowledge Representation

Expense data is stored in structured tables inside a SQLite database, representing knowledge in the form of:

* Item Name
* Price
* Date
* Month

This structured storage allows efficient retrieval and searching of information.

### 3. Simple Software Agent Behavior

The system acts as a simple agent:

```
User Input → System Processing → Output
```

Example:

```
User requests to search for an item
↓
System scans stored expense records
↓
Matching result is displayed
```

---

## Installation

1. Clone the repository

```
git clone https://github.com/tanviag2601/Finance-Tracker.git
```

2. Navigate to the project folder

```
cd expense-tracker
```

3. Install required library

```
pip install tabulate
```

---

## Running the Project

Run the program using:

```
python main.py
```

The program will display a menu where users can choose actions such as storing, viewing, or searching expenses.

---

## Example Menu

```
The Menu:
1: To store the expenses.
2: To view the expense table.
3: To view total expenses.
4: To view monthly graph.
5: To search the item.
Enter the choice:
```

---

## Screenshots

### 🔹 The Library Menu
<img width="702" height="187" alt="Screenshot 2026-03-31 172652" src="https://github.com/user-attachments/assets/4f03f188-a515-48f6-84fd-a90e28866dfd" />


### 🔹 Item-wise expense distribution for a month.
<img width="1832" height="958" alt="Screenshot 2026-03-31 173657" src="https://github.com/user-attachments/assets/1e9ecb71-1f71-4cd2-8843-75c8c4e3e2ce" />


### 🔹 Comparison of total expenses across months.
<img width="1741" height="968" alt="Screenshot 2026-03-31 175414" src="https://github.com/user-attachments/assets/3a16dc4e-2459-4085-bc3d-60a926e0eebf" />


### 🔹 Expense search result.
<img width="715" height="238" alt="Screenshot 2026-03-31 173957" src="https://github.com/user-attachments/assets/db98c6fa-ab11-42f2-9b08-f598691ceba7" />

---

## Database

The database file `expenses.db` is automatically created when the program runs.
It stores monthly expense tables and persists data locally.

---

## Future Improvements

- Expense category analysis (Food, Travel, Shopping etc.)
- Budget limit alerts
- Export expense reports to CSV
- Advanced search (search by date or price range)

