dna = str(input("DNA: "))
base = str(input("base: "))
counter = 0
if base == "A" :
    for i in dna :
        if i in "A" :
            print("c: %s" % (i))
            print("True if test")
            counter += 1
        else:
            print("c: %s" % (i))
    print("There are %d times that base %s occur in this DNA." % (counter,base))
elif base == "C" :
    for i in dna :
        if i in "C" :
            print("c: %s" % (i))
            print("True if test")
            counter += 1
        else:
            print("c: %s" % (i))
    print("There are %d times that base %s occur in this DNA." % (counter,base))
elif base == "G" :
    for i in dna :
        if i in "G" :
            print("c: %s" % (i))
            print("True if test")
            counter += 1
        else:
            print("c: %s" % (i))
    print("There are %d times that base %s occur in this DNA." % (counter,base))
elif base == "T" :
    for i in dna :
        if i in "T" :
            print("c: %s" % (i))
            print("True if test")
            counter += 1
        else:
            print("c: %s" % (i))
    print("There are %d times that base %s occur in this DNA." % (counter,base))
else :
    print("This is not DNA String")