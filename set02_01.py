import math as m

shape = input("Input a shape T/S/C: ")
shape = str(shape)

if shape == "T" or shape == "S" or shape == "C" :
    if shape == "T" :
        length = input("Input a length: ")
        length = float(length)
        if length >= 0 :
            tri = (length^2)/4
            print("The surface of a triangle is %.2f" % (tri))
        else :
            print("Length must be more than zero")
    elif shape == "S" :
        length = input("Input a length: ")
        length = float(length)
        if length >= 0 :
            squ = (length^2)/2
            print("The surface of a square is %.2f" % (squ))
        else :
            print("Length must be more than zero")
    elif shape == "C" :
        length = input("Input a length: ")
        length = float(length)
        if length >= 0 :
            cir = m.pi*(length/2)** 2
            print("The surface of a circle is %.2f" % (cir))
        else :
            print("Length must be more than zero")
else :
    print("Type must be only T/S/C")