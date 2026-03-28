import sqlite3
conne = sqlite3.connect("expenses.db")  #creating database file
cursor = conne.cursor()
def table_name(month):
    match month:
        case "January":
            create_table(month)
        case "Februray":
            create_table(month)
        case "March":
            create_table(month)
        case "April":
            create_table(month)
        case "May":
            create_table(month)
        case "June":
            create_table(month)
        case "July":
            create_table(month)
        case "August":
            create_table(month)
        case "September":
            create_table(month)
        case "October":
            create_table(month)
        case "November":
            create_table(month)
        case "December":
            create_table(month)
        case _:
            return "Unknown Status"
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
    item=input("Enter the name of the item")
    price=float(input("Enter the price of the item"))
    date=input("Enter date (YYYY-MM-DD):")
    cursor.execute(f"""
                INSERT INTO {month}(ITEM_NAME,PRICE,DATE)
                VALUES(?,?,?)""",
                (item,price,date)
                )
    conne.commit()

def total_amount(month):
    cursor.execute(f"""SELECT SUM(PRICE) FROM {month}""")
    amount=cursor.fetchone()
    return amount[0]
    conne.close()




    

