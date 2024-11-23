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

Line 3 - Check if element is present at middle position <br/>
Line 6 - If element is greater, ignore left half <br/>
Line 9 - If element is smaller, ignore right half <br/>

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

Line 3 - Check if element is present at the middle itself <br/>
Line 6 - If element is smaller than middle element, then it can only be present in left subarray <br/>
Line 9 - Else Condition -> the element can only be present in right subarray <br/>

**Time complexity**: Binary search has a logarithmic time complexity **O(log n)** which makes it significantly faster than linear search for large datasets. 

## Example Run

```bash
cd DivideAndConquer/BinarySearch
```

```bash
python3 main.py
Enter 'iter' or 'recu' choice in Binary search : iter
Enter number of elements : 5

Enter the numbers : 1 10 11 2 4

Your Array is -  [1, 10, 11, 2, 4]

Your Array when sorted is -  [1, 2, 4, 10, 11]
Enter the search number from your array : 4
Element is present and its at position 2 in the sorted array
Enter 'iter' or 'recu' choice in Binary search : recu
Enter number of elements : 5

Enter the numbers : 1 3 8 2 0

Your Array is -  [1, 3, 8, 2, 0]

Your Array when sorted is -  [0, 1, 2, 3, 8]
Enter the search number from your array : 0
Element is present and its at position 0 in the sorted array
Enter 'iter' or 'recu' choice in Binary search : exit
```

## Example of error handling

```bash
python3 main.py
Enter 'iter' or 'recu' choice in Binary search : ite

Sorry that was an incorrect input - please type 'iter' or 'recu' or 'exit' to stop.
Enter 'iter' or 'recu' choice in Binary search : rec

Sorry that was an incorrect input - please type 'iter' or 'recu' or 'exit' to stop.
Enter 'iter' or 'recu' choice in Binary search : test

Sorry that was an incorrect input - please type 'iter' or 'recu' or 'exit' to stop.
Enter 'iter' or 'recu' choice in Binary search : exit
```
