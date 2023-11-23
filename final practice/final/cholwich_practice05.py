def main():
    for i in range(1,user+1):
        print(" " * (user-i),end="")
        print((str(user) + " ") * i)
while True:
    user = int(input("Enter an integer number(0 to exit): "))
    if user == 0 :
        print("Exit program.Bye!")
        break
    elif user > 9 :
        print("Valid value is between 0 and 9!")
    else:
        main()