import math

num1,num2 = input("Please enter two integers: ").split(" ")
sum = 0

if num1.isnumeric and num2.isnumeric :
    num1,num2 = int(num1) , int(num2)
    if 1 <= num1 <= 30 and 1 <= num2 <= 30 :
        if num1 > num2 :
            low = num2
            high = num1
            print("The minimum number is %d" % (low))
            print("The maximum number is %d" % (high))
            for i in range(0,high-low+1) :
                sum += (low + i)
            final = math.sqrt(sum)
            print("The square root of the summation is %.2f" % (final))
        else :
            low = num1
            high = num2
            print("The minimum number is %d" % (low))
            print("The maximum number is %d" % (high))
            for i in range(0,high-low+1) :
                sum += (low + i)
            final = math.sqrt(sum)
            print("The square root of the summation is %.2f" % (final))
else:
    print("Invalid inputs")