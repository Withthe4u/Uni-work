from operator import itemgetter
dictt = {}
overall = []

def namescore(dictt):
    name, score = profile.split()
    overall.append(int(score))
    if name.isalpha() and score.isnumeric() :
        if name in dictt.keys():
            print("Duplicated player")
        else :
            dictt[name] = int(score)
    else :
            print("Invalid input")
    return dictt

while True :
    profile = input("Input: ")
    if profile == "done":
        break
    else :
        namescore(dictt)
        dictt = dict(sorted(dictt.items(),key = itemgetter(1),reverse = True))

for key in dictt :
    if dictt[key] == max(overall) :
        print(key,dictt[key],"Gold")
    elif dictt[key] > sum(overall)/ len(overall):
        print(key,dictt[key],"Silver")
    else :
        print(key,dictt[key])