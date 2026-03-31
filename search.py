import sqlite3

def search_item():  # to search item

    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    months = [
        "January","February","March","April","May","June",
        "July","August","September","October","November","December"
    ]
    item = input("Enter item to search: ").lower()
    found = False
    for month in months:
        try:
            cursor.execute(f"SELECT ITEM_NAME, PRICE, DATE FROM {month}")
            rows = cursor.fetchall()

            for name, price, date in rows:

                if name.lower() == item:
                    print(f"Found in {month}: {name} - {price} on {date}")
                    found = True

        except:
            # table may not exist
            pass
    conn.close()
    if not found:
        print("Item not found in any month.")