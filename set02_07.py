import math

a,b,c = input("Please enter an input: ").split("*")
option = int(input("Please enter your choice (1 or 2): "))
if a.isnumeric and b.isnumeric and c.isnumeric :
    if option == 1:
            a,b,c = int(a),int(b),int(c)
            result1 = a + math.sqrt((b**2) + (c**3))
            print("The output is %.2f" % (result1))
    elif option == 2:
          ab = a + b
          ab,c = int(ab),int(c)
          result2 = (ab % c)
          print("The output is %.2f" % (result2))
    else:
          print("Invalid inputs")
else:
      print("Invalid inputs")