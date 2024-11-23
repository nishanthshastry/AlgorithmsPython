# Binary Search

## Binary Search - Divide And Conquer phases

- Divide Phase: In binary search, the "divide" step involves calculating the middle index of the current search space and comparing the target value to the element at that index.
- Conquer Phase: Based on the comparison, the algorithm "conquers" by narrowing the search space to either the left or right half of the array, depending on whether the target is smaller or larger than the middle element.
- Combine Phase: Since the search space is repeatedly halved, the algorithm quickly converges to the target value or determines that it is not present in the array.

### NOTE - The array must be sorted for binary search to work efficiently. 

## Algorithm

### Iterative Approach

**Algorithm BinarySearch** (Array, low, high, element)
```bash
   while low <= high:
       mid = low + (high - low) // 2
       if Array[mid] == element then
            return mid
       else
        if Array[mid] < element then
                low = mid + 1
        endif
       else
            high = mid - 1
       endif
   endWhile
   return “Element Not Present”
```

Line 3 - Check if element is present at middle position
Line 6 - If element is greater, ignore left half
Line 9 - If element is smaller, ignore right half

### Recursive Approach

**Algorithm BinarySearch** (Array, low, high, element)
```bash
    if high >= low then
        mid = low + (high - low) // 2
        if Array[mid] == element then
            return mid
        else 
            if Array[mid] > element then
                return binarySearch(Array, low, mid-1, element)
            endif
        else
            return binarySearch(Array, mid + 1, high, element)
        endif
    else
       return “Element Not Present”
    endif
```

Line 3 - Check if element is present at the middle itself
Line 6 - If element is smaller than middle element, then it can only be present in left subarray
Line 9 - Else Condition -> the element can only be present in right subarray

**Time complexity**: Binary search has a logarithmic time complexity O(log n) which makes it significantly faster than linear search for large datasets. 
