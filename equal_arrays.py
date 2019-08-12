t = int(input())
for i in range(t):
    n = int(input())
    a1 = [int(x) for x in input().split()]
    a2 = [int(x) for x in input().split()]
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
    if d1 == d2:
        print(1)
    else:
        print(0)
