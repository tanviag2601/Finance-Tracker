import sqlite3
from tabulate import tabulate
conne = sqlite3.connect("expenses.db")  #creating database file
cursor = conne.cursor()
# to view the table
cursor.execute("""SELECT * FROM Expense""")
rows= cursor.fetchall()
headers=[i[0] for i in cursor.description]
print(tabulate(rows, headers=headers, tablefmt="grid"))
conne.close()