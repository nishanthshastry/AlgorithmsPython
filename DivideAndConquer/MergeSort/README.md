# Merge Sort

## Merge Sort - Divide And Conquer phases

- **Divide** Phase: Divide the list or array recursively into two halves until it can no more be divided.
- **Conquer** Phase: Each subarray is sorted individually using the merge sort algorithm.
- **Merge** Phase: The sorted subarrays are merged back together in sorted order. The process continues until all elements from both subarrays have been merged.

## Algorithm

**Algorithm Merge** (A, p, q, r)
```bash
    n1 = q - p + 1
    n2 = r - q
    let L[1 ... n1 + 1] and R[1 ... n2 + 1] be new arrays
    for i = 1 to n1
        L[i] = A[p + i - 1]
    endfor
    for j = 1 to n2
        R[j] = A[q + j]
    endfor
    L[n1 + 1] = ∞
    R[n2 + 1] = ∞
    i = 1
    j = 1
    for k = p to r
        if L[i] <= R[j] then
            A[k] = L[i]
            i = i + 1
        else
            A[k] = R[j]
            j = j + 1
        endif
    endfor
```

**Algorithm MergeSort** (A, p, r)
```bash
    if p < r then
        q = ⌊(p + r)/2⌋
        MergeSort(A, p, q)
        MergeSort(A, q + 1, r)
        Merge(A, p, q, r)
```

**Time complexity**: The time complexity of Merge Sort is **O(n log n)** (_applies to both average and worst-case scenarios_)

_Recursive nature_: Merge Sort works by recursively dividing the input array into halves until single elements are reached, then merging the sorted halves back together. <br/>
_Merge operation_: The key step is the "merge" operation, where two sorted subarrays are combined into one sorted array, taking O(n) time for an array of size n. <br/>
_Logarithmic divisions_: Since the array is divided in half at each recursive step, the number of levels in the recursion tree is log(n). <br/> <br/>
Therefore, the overall time complexity is **O(n log n)** because we perform O(n) operations at each of the log(n) levels of recursion.

### NOTE - The code implements the above algorithm along with python based concepts for better working and efficient code

(_Ref stackoverflow link_ - _[https://stackoverflow.com/questions/71311126/mergesort-resulting-in-error-in-clrs-3rd-edition](https://stackoverflow.com/questions/71311126/mergesort-resulting-in-error-in-clrs-3rd-edition)_)

## Example Run

```bash
cd DivideAndConquer/MergeSort
```

```bash
python3 main.py

Enter 'Msort' or 'exit' choice : Msort
Enter number of elements : 5

Enter array elements : 1 10 11 2 4

Your Array is -  [1, 10, 11, 2, 4]

Array when sorted with 'Merge Sort' is -  [1, 2, 4, 10, 11]

Enter 'Msort' or 'exit' choice : Msort
Enter number of elements : 6

Enter array elements : 1000 9 200 30 0 10

Your Array is -  [1000, 9, 200, 30, 0, 10]

Array when sorted with 'Merge Sort' is -  [0, 9, 10, 30, 200, 1000]

Enter 'Msort' or 'exit' choice : exit
```

## Example of error handling

```bash
python3 main.py

Enter 'Msort' or 'exit' choice : de

Sorry that was an incorrect input - please type 'Msort' or 'exit' to stop.

Enter 'Msort' or 'exit' choice : rr

Sorry that was an incorrect input - please type 'Msort' or 'exit' to stop.

Enter 'Msort' or 'exit' choice : 2

Sorry that was an incorrect input - please type 'Msort' or 'exit' to stop.

Enter 'Msort' or 'exit' choice : sort

Sorry that was an incorrect input - please type 'Msort' or 'exit' to stop.

Enter 'Msort' or 'exit' choice : exit
```
