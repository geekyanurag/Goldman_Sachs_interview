a1 = [1,2,3,6]
a2 = [1,2,2,2]
d1 = {}
d2 = {}
for i in a1:
    if i in d1:
        d1[i]+=1
    else:
        d1[i]=1

for i in a2:
    if i in d2:
        d2[i]+=1
    else:
        d2[i]=1

print(d1 == d2)
