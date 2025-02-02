# Quick Sort

## Quick Sort - Divide And Conquer phases

- **Divide** Phase: Choose a pivot and partition the array into two sub-arrays elements <= pivot and elements > pivot, placing the pivot in its correct position.
- **Conquer** Phase: Recursively apply Quick Sort to the left and right sub-arrays.
- **Merge** Phase: No explicit merge; the sorted sub-arrays and pivot naturally form the sorted array as recursion unwinds.

## Algorithm

**Algorithm QuickSort** (A, p, r)
```bash
    if p < r then
        q = Partition(A, q, r)
        QuickSort(A, p, q-1)
        QuickSort(A, q+1, r)
    endif
```

**Algorithm Partition** (A, q, r)
```bash
    x = A[r]
    i = p - 1
    for j = p to r - 1
        if A[j] <= x then
            i = i + 1
            exchange A[i] with A[j]
        endif
    endfor
    exchange A[i+1] with A[r]
    return i + 1
```

**Time complexity**: The time complexity of Quick Sort,
- Average Case: **(n log n)**
- Worst Case: **O(n<sup>2</sup>)**

### NOTE - The code implements the above algorithm along with python based concepts for better working and efficient code

(_Ref geeksforgeeks link_ - _[https://www.geeksforgeeks.org/quick-sort-algorithm/](https://www.geeksforgeeks.org/quick-sort-algorithm/)_)

## Example Run

```bash
cd DivideAndConquer/QuickSort
```

```bash
python3 main.py

Enter 'Qsort' or 'exit' choice : Qsort
Enter number of elements : 6

Enter array elements : 100 23 30 98 1 0

Your Array is -  [100, 23, 30, 98, 1, 0]

Array when sorted with 'Quick Sort' is -  [0, 1, 23, 30, 98, 100]

Enter 'Qsort' or 'exit' choice : Qsort
Enter number of elements : 5     

Enter array elements : 12 3 4 55 9

Your Array is -  [12, 3, 4, 55, 9]

Array when sorted with 'Quick Sort' is -  [3, 4, 9, 12, 55]

Enter 'Qsort' or 'exit' choice : exit
```

## Example of error handling

```bash
python3 main.py

Enter 'Qsort' or 'exit' choice : eer

Sorry that was an incorrect input - please type 'Qsort' or 'exit' to stop.

Enter 'Qsort' or 'exit' choice : 112

Sorry that was an incorrect input - please type 'Qsort' or 'exit' to stop.

Enter 'Qsort' or 'exit' choice : qsort

Sorry that was an incorrect input - please type 'Qsort' or 'exit' to stop.

Enter 'Qsort' or 'exit' choice : sort

Sorry that was an incorrect input - please type 'Qsort' or 'exit' to stop.

Enter 'Qsort' or 'exit' choice : exit
```