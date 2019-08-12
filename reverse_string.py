def reverseWords(s):
    s1=s.split(".")[::-1]
    s1 = ".".join(s1)
    return s1

t = int(input())
for i in range(t):
    s = input()
    print(reverseWords(s))
