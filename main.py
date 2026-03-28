from store import insert_table, create_table, total_amount
from view import view_table
import recommend
import predict
create_table()
str="Y"
while str== "Y":
    print("The Menu:")
    print("1: To store the expenses")
    print("2: To view the expense table")
    print("3: To recommend")
    print("4: To predict the expenses")
    print("5: To view total expenses")
    choice=int(input("Enter the choice"))
    if(choice==1):
        insert_table()
    elif(choice==2):
        view_table()
    elif(choice==3):
        recommend()
    elif(choice==4):
        predict()
    elif(choice==5):
        amt=total_amount()
        print("The total amount spent is: ",amt)    
    str=input("Do you want to continue the program? ")
print("The program is terminated")    
    


