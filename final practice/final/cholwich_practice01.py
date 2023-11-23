b = int(input("Enter the initial balance: "))
while True:
    x, y = str(input("Transaction type and amount (\"done 0\" to exit): ")).split()
    if x == "done" and y == "0" :
        break
    elif x == "D" and y.isnumeric() and int(y) > 0 :
        b = b + int(y)
        print("Deposit = %d THB, current balance = %d THB" % (int(y),b))
    elif x == "W" and y.isnumeric() and int(y) > 0 :
        b = b - int(y)
        print("Withdrawal = %d THB, current balance = %d THB" % (int(y),b))
    else :
        print("Invalid input!")

print("Current balance: %d" % (b))