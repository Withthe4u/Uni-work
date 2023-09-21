customers = input("Input (Number of customers): ")
discount = input("Input (Discount code): ")
customers = int(customers)
discount = str(discount)
if 1 <= customers <= 3 :
    price = 399
    price = float(price)
    print("%d person x %.2f baht" % (customers,price))
    customers = float(customers)
    subtotal = customers * price
    print("A subtotal price is %.2f baht" % (subtotal))
    if discount == "CASH" :
        print("On-top discount 5%")
        final = subtotal * 0.95
        print("A total price is %.2f baht" % (final))
    elif discount == "BIRTHDAY" :
        print("On-top discount 10%")
        final = subtotal * 0.90
        print("A total price is %.2f baht" % (final))
    elif discount == "COVID" :
        print("On-top discount 30%")
        final = subtotal * 0.70
        print("A total price is %.2f baht" % (final))
    else :
        print("On-top discount 0%")
        print("A total price is %.2f baht" % (subtotal))
elif 4 <= customers <= 6 :
    price = 499
    price = float(price)
    print("%d person x %.2f baht" % (customers,price))
    customers = float(customers)
    subtotal = customers * price
    print("A subtotal price is %.2f baht" % (subtotal))
    if discount == "CASH" :
        print("On-top discount 5%")
        final = subtotal * 0.95
        print("A total price is %.2f baht" % (final))
    elif discount == "BIRTHDAY" :
        print("On-top discount 10%")
        final = subtotal * 0.90
        print("A total price is %.2f baht" % (final))
    elif discount == "COVID" :
        print("On-top discount 30%")
        final = subtotal * 0.70
        print("A total price is %.2f baht" % (final))
    else :
        print("On-top discount 0%")
        print("A total price is %.2f baht" % (subtotal))
elif  customers > 6 :
    price = 599
    price = float(price)
    print("%d person x %.2f baht" % (customers,price))
    customers = float(customers)
    subtotal = customers * price
    print("A subtotal price is %.2f baht" % (subtotal))
    if discount == "CASH" :
        print("On-top discount 5%")
        final = subtotal * 0.95
        print("A total price is %.2f baht" % (final))
    elif discount == "BIRTHDAY" :
        print("On-top discount 10%")
        final = subtotal * 0.90
        print("A total price is %.2f baht" % (final))
    elif discount == "COVID" :
        print("On-top discount 30%")
        final = subtotal * 0.70
        print("A total price is %.2f baht" % (final))
    else :
        print("On-top discount 0%")
        print("A total price is %.2f baht" % (subtotal))
else :
    print("error")