initial = 100

def calcpoint(initial):
    action, number = command.split()
    number = int(number)
    if action == "P" and number >= 0 :
        points = number // 50
        initial += points
        print("You earned %d points" % (points))
        print("You accumlated %d points" % (initial))
    elif action == "R" :
        if number >= initial :
            print("Not enough points")
        else :
            initial -= number
            print("You redeemed %d points" % (number))  
            print("You accumlated %d points" % (initial))
    else :  
        print("Invalid Command")
    return initial
while True :
    command = input("Command: ")
    if command == "done 0" :
        break
    else :
        calcpoint(initial)