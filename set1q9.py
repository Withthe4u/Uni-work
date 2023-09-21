speed = int(input("Enter speed in mph: "))
distance = int(input("Enter distance in miles: "))
output = str(input("Enter output format (D or M): "))

if speed >= 0 and distance >= 0 :
    time = distance / speed
    if output == "D" :
        print("At %d mph, it will take" % (speed))
        print("%.2f hours to travel %d miles." % (time,distance))
    elif output == "M" :
        hour = time // 1
        minute = (time % 1) * 60
        print("At %d mph, it will take" % (speed))
        print("%d hours and %d minutes to travel %d miles." % (hour,minute,distance))
    else :
        print("Invalid input")

else :
    print("Invalid input")