import sqlite3
from store import create_table
from tabulate import tabulate
def view_table(month):
    conne = sqlite3.connect("expenses.db")  #creating database file
    cursor = conne.cursor()
    # to view the table
    cursor.execute(f"""SELECT * FROM {month}""")
    rows= cursor.fetchall()
    headers=[i[0] for i in cursor.description]
    print("MONTH: ",month)
    print(tabulate(rows, headers=headers, tablefmt="grid"))
    conne.close()