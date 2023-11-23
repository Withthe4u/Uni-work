n = int(input("enter an integer: "))
factor = []
def main():
    for i in range(1,n+1,1):
        if n % i == 0:
            factor.append(i)
        else:
            continue
    print("Output:", factor)
main()