l = [1,2,3,4,5,100,-9,-1]
max = l[0]
min = l[0]
for i in range(1,len(l)):
    if l[i-1] < l[i] :
        max = l[i]
    else :
        continue
for i in range(1,len(l)):
    if l[i-1] > l[i] :
        min = l[i]
    else :
        continue
print(max,min)