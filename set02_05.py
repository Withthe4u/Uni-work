a,b,c = input("a,b,c = ").split(" ")

if a == "True" or a == "False" or b == "True" or b == "False" or c == "True" or c == "False" :
    if a == "False" and b == "False" and c == "True":
        print("Deny")
    elif a == "False" and b == "True" and c == "False":
        print("Deny")
    elif a == "False" and b == "True" and c == "True":
        print("Deny")
    else :
        print("Grant")
else :
    print("Invalid output")