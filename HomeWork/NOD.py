def gcd(a, b):
    while b:
        a, b = b, a % b
        print(a)
    return a


x = int(input('a = '))
y = int(input('b = '))
print('НОД =', gcd(x, y))
