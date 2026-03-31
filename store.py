import sqlite3
conne = sqlite3.connect("expenses.db")  #creating database file
cursor = conne.cursor()
def create_table(month): # to create a table
    cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {month}(
            ITEM_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            ITEM_NAME TEXT,
            PRICE INTEGER,
            DATE TEXT
        )
    """)
    conne.commit()
amount=0
def insert_table(month):# to insert into table
    item=input("Enter the name of the item: ")
    price=float(input("Enter the price of the item: "))
    date=input("Enter date (YYYY-MM-DD): ")
    cursor.execute(f"""
                INSERT INTO {month}(ITEM_NAME,PRICE,DATE)
                VALUES(?,?,?)""",
                (item,price,date)
                )
    conne.commit()

def total_amount(month):    # to calculate total amount
    cursor.execute(f"""SELECT SUM(PRICE) FROM {month}""")
    amount=cursor.fetchone()
    return amount[0]
    conne.close()




    

