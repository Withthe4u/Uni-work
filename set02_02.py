age,name = input("Please enter your information: ").split(",")
age = int(age)
if 0 <= age <= 120 and name.isalpha:
    print("Your name is %s." % (name))
    print("Your age is %d." % (age))
else:
    print("Please enter your complete information")