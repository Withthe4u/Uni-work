pattern = str(input("Input: "))

for i in pattern:
    if i.isnumeric():
        i = int(i)
        print("**#" *(i // 3) + "*" * (i % 3))
    else :
        print("",end="")