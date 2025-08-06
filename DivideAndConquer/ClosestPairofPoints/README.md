# Closest Pair of Points

## Closest Pair of Points - Divide And Conquer phases

*Before the algorithm starts sort the points by x-coordinate.*

- **Divide** Phase: Split the points into two halves by a vertical line L.

- **Conquer** Phase: Recursively find the closest pair in each half.

- **Combine** Phase: Find the closest pair where one point is in the left half and the other is in the right half (the "strip" case).

## Algorithm

**Algorithm ClosestPairofPoints** (Px, Py)
```bash
    if |Px| ≤ 3
        Compute and return the closest pair by brute force
    else
        Let Qx, Rx = left and right halves of Px
        Let midpoint x̄ = x-coordinate of last point in Qx
        Partition Py into Qy and Ry, where Qy has points in Qx, Ry in Rx
        (dL, pairL) = Closest-Pair(Qx, Qy)
        (dR, pairR) = Closest-Pair(Rx, Ry)
        (d, bestPair) = min((dL, pairL), (dR, pairR))
        Build Sy = all points in Py such that |x - x̄| < d
        for i = 1 to |Sy| - 1
            for j = i+1 to min(i+7, |Sy|)
                if distance(Sy[i], Sy[j]) < d
                    (d, bestPair) = (distance(Sy[i], Sy[j]), (Sy[i], Sy[j]))
    return (d, bestPair)
```

### Closest Pair of Points - Divide And Conquer phases (_Detail breakdown_)

- **Divide** Phase:
    - Split Px into Qx and Rx (left and right halves), using the median x.
    - Partition Py into Qy and Ry corresponding to Qx and Rx.

- **Conquer** Phase:
    - Recursively compute closest pairs in each half.

- **Combine** Phase:
    - Compute minimum distance d from the two halves.
    - Construct the strip S: points within d of the dividing line, sorted by y.
    - For each point in S, check at most the next 7 points in S (this is a geometric property proved in CLRS).
    - Update the minimum if a closer pair is found in the strip.

**Time complexity**: The time complexity of Closest pair of Points algorithm is **O(n log n)**.
- Sorting by x and y at the start is O(n log n).
- Each recursive level splits in half and merging takes O(n) (processing the strip).
- There are O(logn) levels, so overall:
    - T(n) = 2T(n/2) + O(n) ⟹ T(n) = O(n log n) (by Master Theorem).

### NOTE 1 - The code implements the above algorithm along with python based concepts for better working and efficient code

### NOTE 2 - The algorithm and concepts are referenced from the textbook "*Introduction to Algorithms 3rd edition* by - *Cormen, Leiserson, Rivest and Stein (CLRS)*"

## Example Run

```bash
cd DivideAndConquer/ClosestPairofPoints
```

```bash
python3 main.py

Enter 'CPP' or 'exit' choice : CPP
Enter number of points : 6

Enter each point as two numbers separated by space (e.g., 1 2):
Point 1: 2 3
Point 2: 12 30
Point 3: 40 50
Point 4: 5 1
Point 5: 12 10
Point 6: 3 4

Points you provided are -  [(2.0, 3.0), (12.0, 30.0), (40.0, 50.0), (5.0, 1.0), (12.0, 10.0), (3.0, 4.0)]

The closest pair of points is: ((2.0, 3.0), (3.0, 4.0))

Distance between them: 1.414214

Enter 'CPP' or 'exit' choice : exit
```

## Example of error handling

```bash
python3 main.py

Enter 'CPP' or 'exit' choice : c

Sorry that was an incorrect input - please type 'CPP' or 'exit' to stop.

Enter 'CPP' or 'exit' choice : e

Sorry that was an incorrect input - please type 'CPP' or 'exit' to stop.

Enter 'CPP' or 'exit' choice : 12

Sorry that was an incorrect input - please type 'CPP' or 'exit' to stop.

Enter 'CPP' or 'exit' choice : 1 2

Sorry that was an incorrect input - please type 'CPP' or 'exit' to stop.

Enter 'CPP' or 'exit' choice : exit
```