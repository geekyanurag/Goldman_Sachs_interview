def ugly(n):
    ugly_no = [1]
    i2 = i3 = i5 = 0
    next_2 = ugly_no[i2]*2
    next_3 = ugly_no[i3]*3
    next_5 = ugly_no[i5]*5
    for i in range(1,n):
        min_a = min(next_2,next_3,next_5)
        ugly_no.append(min_a)

        if min_a == next_2:
            i2+=1
            next_2 = ugly_no[i2]*2
        if min_a == next_3:
            i3+=1
            next_3 = ugly_no[i3]*3
        if min_a == next_5:
            i5+=1
            next_5 = ugly_no[i5]*5
    return ugly_no[-1]

print(ugly(7))
