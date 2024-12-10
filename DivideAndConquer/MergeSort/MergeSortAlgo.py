def merge(a, p, q, r):
    n1 = q - p
    n2 = r - q
    left = a[p : q]
    right = a[q : r]
    i = 0
    j = 0
    for k in range(p, r):
        if j >= n2 or (i < n1 and left[i] <= right[j]):
            a[k] = left[i]
            i = i + 1
        else:
            a[k] = right[j]
            j = j + 1

def merge_sort(a, p, r):
    if r - p > 1:
        q = (p + r) // 2
        merge_sort(a, p, q)
        merge_sort(a, q, r)
        merge(a, p, q, r)