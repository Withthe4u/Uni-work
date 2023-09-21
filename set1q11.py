a= int(input("Input: a=? "))
b= int(input("Input: b=? "))
c= int(input("Input: c=? "))
if a <= 0 or b <= 0 or c<= 0 :
   print("Some input is not a number")
else :
    if a >= b + c or b >= a + c or c >= a + b :
        print("Output: Can't form a triangle")
    else :
        print("Output:Form a triangle")
    
