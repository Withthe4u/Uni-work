pattern = int(input("Input: "))
if pattern >= 3 :
    for i in range(1,pattern+1) : # top part
        if i == 1 :
            print("*" + (" " * ((pattern * 2) - 2)) + "*")
        elif i % 2 == 0 : #even
             seq = int(i / 2)
             gap = int((pattern - i) * 2)
             print(("*0" * seq) + (" " * gap) + ("0*" * seq))
        elif i % 2 == 1 : #odd
             seq = int(i / 2)
             gap = int((pattern - i) * 2)
             print (("*0" * seq) + "*" + (" " * (gap)) + "*" + ("0*" * seq))
        elif i == pattern : #middle
             seq = int(i % 2)
             print(("*0" * seq) + "**" + ("0*" * seq))
    for s in range(pattern-1,0,-1): #bottom part
         if s == 1 :
            print("*" + (" " * ((pattern * 2) - 2)) + "*")
         elif s % 2 == 0 :
             seq = int(s / 2)
             gap = int((pattern - s) * 2)
             print(("*0" * seq) + (" " * gap) + ("0*" * seq))
         elif s % 2 == 1 :
             seq = int(s / 2)
             gap = int((pattern - s) * 2)
             print (("*0" * seq) + "*" + (" " * (gap)) + "*" + ("0*" * seq))
else:
    print("Your input is invalid")