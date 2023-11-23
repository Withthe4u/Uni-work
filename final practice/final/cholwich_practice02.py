from operator import itemgetter
dictt = {}
def namescore(dictt):
    name, score = profile.split()
    if name.isalpha() and score.isnumeric() and 0 <= int(score) <= 100 :
        if name in dictt.keys():
            print("Duplicate name!")
        else :
            dictt[name] = int(score)
        dictt = dict(sorted(dictt.items(),key = itemgetter(1),reverse = True))
    else :
            print("Invalid Score")
    return dictt

while True :
    profile = input("Enter student name and score: ")
    if profile == "end 0":
        break
    else :
        namescore(dictt)

print("List:")
for key in dictt:
    print(key,dictt[key],"test")