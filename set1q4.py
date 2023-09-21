import random
width = int(input("Rectange width: "))
height= int(input("Rectange height: "))
thick = int(input("Rectange thickness: "))

for i in range(height):
    if i < thick or i >= height - thick :
        for s in range(width) :
            print(random.choice(["#","$","*"]),end="")
    else :
        for s in range(thick):
            print(random.choice(["#","$","*"]) * thick,end="")
            print(" " * (width - 2 * thick),end="")
    print()
