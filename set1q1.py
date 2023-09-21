hour,minute,sec = input("Input:").split(":")
hour = int(hour)
minute = int(minute)
sec = int(sec)


if 0 <= hour <= 23 and 0 <= minute <= 59 and 0 <= sec <= 59 :
    time = (hour * 3600) + (minute * 60) + (sec)
    print("The number of seconds = %d" % (time))
else:
    print("Invalid time")