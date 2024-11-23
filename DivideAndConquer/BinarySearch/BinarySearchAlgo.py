def binary_search_iter(array, low, high, ele):
    array = sorted(array)
    while low <= high:
        mid = low + (high - low) // 2
        if array[mid] == ele:
            return mid
        elif array[mid] < ele:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def binary_search_recur(array, low, high, ele):
    array = sorted(array)
    if high >= low:
        mid = low + (high - low) // 2
        if array[mid] == ele:
            return mid
        elif array[mid] > ele:
            return binary_search_recur(array, low, mid-1, ele)
        else:
            return binary_search_recur(array, mid + 1, high, ele)
    else:
        return -1