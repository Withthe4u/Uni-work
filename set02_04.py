special = str(input("Enter a special character: "))
size = int(input("Enter the size of the pattern: "))
option = int(input("Enter the option for the pattern: "))

if special == "#" or special == "$" or special == "@" or special == "*" or special == "^" :
    if size > 0 :
        if option == 1 :
            for i in range(size):
                    print("." * i,end="")
                    print(special,end="")
                    print("." * (size-i-1))
        elif option == 2 :
             for s in range(size):
                  print("." * (size-s-1),end="")
                  print(special,end="")
                  print("." * s,)
        else:
             print("Wrong input values")
else:
     print("Wrong input values")
            
    