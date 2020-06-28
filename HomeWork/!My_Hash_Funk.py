# Производит хеш числа или строки(много коллизий)
b = input()


def hash_(a):
    hash_end = 0

    for pos in range(len(a)):
        hash_end += ord(a[pos]) * (30 ** pos)

    return hash_end % 50000
