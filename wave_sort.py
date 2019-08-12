a = [10, 5, 6, 3, 2, 20, 100, 80]

def swap(a,b):
    temp = a
    a = b
    b = temp
    return (a,b)

def wave_sort(a):
    for i in range(len(a)-1):
        if i%2 == 0:
            if a[i]<a[i+1]:
                a[i],a[i+1] = swap(a[i], a[i+1])
        else:
            if a[i]>a[i+1]:
                a[i],a[i+1] = swap(a[i], a[i+1])
    return a
print(wave_sort(a))
