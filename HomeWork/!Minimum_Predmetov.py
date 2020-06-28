n, m = map(int, input().split())
mass = [int(i) for i in input().split()]

a = [0] * 100000

for i in range(n):
    for j in range(m, 0, -1):
        if a[j] != 0:
            if a[j + mass[i]] != 0:
                a[j + mass[i]] = min(a[j + mass[i]], 1 + a[j])
            else:
                a[j + mass[i]] = a[j] + 1

    a[mass[i]] = 1

print(a[m])
