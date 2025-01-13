def exchange(a, i, j):
    a[i], a[j] = a[j], a[i]

def partition(a, p, r):
    x = a[r]
    i = p - 1
    for j in range(p, r):
        if a[j] < x:
            i += 1
            exchange(a, i, j)
    exchange(a, i + 1, r)
    return i + 1

def quick_sort(a, p, r):
    if p < r:
        q = partition(a, p, r)
        quick_sort(a, p, q - 1)
        quick_sort(a, q + 1, r)