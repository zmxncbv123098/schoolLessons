

a = input()
a = a[:a.rfind(" ")-1]
a = a.upper()
print(a)
b = [0] * 26
for i in range(len(a)):
    if (64 < ord(a[i])) and (ord(a[i]) < 91):
        b[ord(a[i])-65] += 1
c = max(b)
