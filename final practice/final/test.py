while True:
     a=int(input("enter an integer number(0 to exit:"))
     if a > 10 :
        print(" valid value is between 0 and 9 !")
     elif a==0:
        print("exit program")

     for i in range(a):
           print(" ",(a-i-1),end=" ")
           print(f"{a} "(i+1))