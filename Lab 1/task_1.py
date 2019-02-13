Total_Amount = 0
Deposit = 0
Withdraw = 0
choice = 0

#print(choice)
while(choice != 4):
    choice = input("Press\t1 for Deposit\n\t\t2 for Withdrawal\n\t\t3 to show Total Amount\n\t\t4 to Exit-\n")
    if (int(choice) == 1):
        Deposit = input("Deposit-\n")
        Total_Amount = Total_Amount + int(Deposit)#adding deposit to total amount.
    elif (int(choice) == 2):
        Withdraw = input("Withdraw-\n")
        Total_Amount = Total_Amount - int(Withdraw)#subtracting withdraw amount from total amount
    elif (int(choice) == 3):
        print("Total Amount - ${0}".format(Total_Amount))
    else:
        break








