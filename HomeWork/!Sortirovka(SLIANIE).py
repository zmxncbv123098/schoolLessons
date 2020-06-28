""" Сортировка слиянием. """


def merge(left, right):
    """Merge two lists in ascending order."""
    lst = []
    while left and right:
        if left[0] < right[0]:
            lst.append(left.pop(0))
        else:
            lst.append(right.pop(0))
    if left:
        lst.extend(left)
    if right:
        lst.extend(right)
    return lst


def mergesort(lst):
    length = len(lst)
    if length >= 2:
        mid = int(length / 2)
        lst = merge(mergesort(lst[:mid]), mergesort(lst[mid:]))
    return lst

print(''.join(mergesort(list("98765432108976143501"))))
print(''.join(mergesort(list("defgaabcdef"))))
