char1 = input("Give me a character: ")
char2 = input("Give me another character: ")
alpha = "abcdefghijklmnopqrstuvwxyz"
if char1 > char2 :
    first = char2
    last = char1
else :
    first = char1
    last = char2
print("Output: ")
if char1.isalpha() and char2.isalpha :
    for i in range(len(alpha)) :
        if alpha[i] == first :
            start = i
            break
    for s in range(len(alpha)) :
        print(alpha[start],end="")
        if alpha[start] == last:
            break
        else :
            start += 1
else :
    print("You need to input two charactes")