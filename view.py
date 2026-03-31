import sqlite3
from matplotlib import pyplot as plt
from tabulate import tabulate
import numpy as np
def view_table(month):  # to view the table
    conne = sqlite3.connect("expenses.db")  #creating database file
    cursor = conne.cursor()
    # to view the table
    cursor.execute(f"""SELECT * FROM {month}""")
    rows= cursor.fetchall()
    headers=[i[0] for i in cursor.description]
    print("MONTH: ",month)
    print(tabulate(rows, headers=headers, tablefmt="grid"))
    conne.close()

def graphical_view(month):# to view monthly expense graph
    conne = sqlite3.connect("expenses.db")  #creating database file
    cursor = conne.cursor()
    cursor.execute(f"SELECT ITEM_NAME, PRICE FROM {month}")
    rows = cursor.fetchall()
    items = []
    prices = []
    for item, price in rows:
        items.append(item)
        prices.append(price)
    plt.barh(items,prices,color="plum")    #horizontal bar
    plt.xlabel("PRICE")
    plt.ylabel("ITEMS")
    plt.title(f"{month} Finance Table")
    plt.show()

def monthly_graph(c):   # to view total amount of each month
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    months = [
        "January","February","March","April","May","June",
        "July","August","September","October","November","December"
    ]
    month_names = []
    totals = []
    for i in range(0,c):
        try:
            cursor.execute(f"SELECT SUM(PRICE) FROM {months[i]}")
            total = cursor.fetchone()[0]
            if total is not None:
                month_names.append(months[i])
                totals.append(total)

        except:
            # table might not exist yet
            pass
    conn.close()
    if len(month_names) == 0:
        print("No data available")
        return
    plt.bar(month_names, totals, color="salmon")
    plt.xlabel("Month")
    plt.ylabel("Total Expense")
    plt.title("Monthly Expense Summary")
    plt.xticks(rotation=45)
    plt.show()


