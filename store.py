import sqlite3
conne = sqlite3.connect("expenses.db")  #creating database file
cursor = conne.cursor()

# to create a table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Expense(
        ITEM_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        ITEM_NAME TEXT,
        PRICE INTEGER,
        DATE TEXT
    )
""")
# to insert into table
item=input("Enter the name of the item")
price=float(input("Enter the price of the item"))
date=input("Enter date (YYYY-MM-DD):")
cursor.execute("""
            INSERT INTO Expense(ITEM_NAME,PRICE,DATE)
               VALUES(?,?,?)""",
               (item,price,date)
               )
conne.commit()
conne.close()


