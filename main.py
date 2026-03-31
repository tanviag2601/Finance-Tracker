from store import insert_table,create_table, total_amount
from view import view_table, graphical_view,monthly_graph
from search import search_item
str="Y"
while str== "Y":
    print("The Menu:")
    print("1: To store the expenses.")
    print("2: To view the expense table.")
    print("3: To view total expenses.")
    print("4: To view monthly graph.")
    print("5: To search the item.")
    choice=int(input("Enter the choice: "))
    months = ["January","February","March","April","May","June",
"July","August","September","October","November","December"]
    if(choice!=5):
        month_number = int(input("Enter month number (1-12): "))
        month = months[month_number-1]
        create_table(month)
    if(choice==1):
        insert_table(month)
    elif(choice==2):
        view_table(month)
        graphical_view(month)
    elif(choice==3):
        amt=total_amount(month)
        print("The total amount spent is: ",amt)
    elif(choice==4):
        monthly_graph(month_number)
    elif(choice==5):
        search_item()
    str=input("Do you want to continue the program? ")
print("The program is terminated")    
    


