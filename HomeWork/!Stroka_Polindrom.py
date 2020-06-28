'''

Определяет полиндром ли данная строка

'''

a = input().replace(' ', '')
count2 = -1
boolean = 0
for count in range((len(a) // 2)):
    if a[count] == a[count2]:
        count2 -= 1
    else:
        boolean = 1
        break
if boolean == 0:
    print("YES")
else:
    print("NO")
