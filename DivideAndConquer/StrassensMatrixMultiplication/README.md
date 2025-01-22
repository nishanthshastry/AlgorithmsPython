# Strassen's Matrix Multiplication

## Strassen's Matrix Multiplication - Divide And Conquer phases

- **Divide** Phase: Split each input matrix into four equal-sized submatrices.
- **Conquer** Phase: Recursively compute 7 intermediate matrix multiplications using Strassen's formulas.
- **Merge** Phase: Construct the final result matrix by adding and subtracting the intermediate results.

## Algorithm

**Algorithm Strassen** (A, B, n):
```bash
    if n == 1:
        return A * B
    else:
        Divide A and B into n/2 submatrices
        M1 ← Strassen(A11 + A22, B11 + B22)
        M2 ← Strassen(A21 + A22, B11)
        M3 ← Strassen(A11, B12 - B22)
        M4 ← Strassen(A22, B21 - B11)
        M5 ← Strassen(A11 + A12, B22)
        M6 ← Strassen(A21 - A11, B11 + B12)
        M7 ← Strassen(A12 - A22, B21 + B22)
        
        C11 ← M1 + M4 - M5 + M7
        C12 ← M3 + M5
        C21 ← M2 + M4
        C22 ← M1 - M2 + M3 + M6
        
        Combine C11, C12, C21, C22 into C
        return C
    endif
```

**Time complexity**: Strassen's algorithm follows the recurrence relation,

<p align="center"> T(n) = 7T(n/2) + O(n²) </p>

Using the <strong>Master Theorem</strong>, the complexity is,

<p align="center"> T(n) = O(n<sup>log₂ 7</sup>) ≈ O(n<sup>2.81</sup>) </p>

This is an improvement over the traditional <code>O(n³)</code> complexity.

#### Explanation of the Code

**strassen** function:
- Recursively divides matrices into four submatrices.
- Computes the 7 Strassen intermediate matrices.
- Combines submatrices to get the final result.

**next_power_of_2** function:
- Ensures the input matrices have dimensions that are powers of 2 by padding them with zeros.

**strassen_multiply** function:
- Pads non-power-of-2 matrices and removes padding after computation.

### NOTE 1
"**pads**" means adding extra rows and/or columns filled with zeros to a matrix to make its dimensions a power of 2.

**Why Padding is Needed?** <br/>
Strassen's algorithm requires the matrix size to be a power of 2 (e.g., 2x2, 4x4, 8x8, etc.) for
efficient recursive division. If the input matrix has a size that is not a power of 2, padding is used
to adjust the size before performing the multiplication.

##### Example of Padding

Suppose you have a `3x3` matrix: <br/>
<p align="center"> 
[1 2 3]<br/>
[4 5 6]<br/>
[7 8 9]<br/>
</p>

Since 3 is **not** a power of 2, padding will be applied to make it a `4x4` matrix by adding zeros:
<p align="center"> 
[1 2 3 0]<br/>
[4 5 6 0]<br/>
[7 8 9 0]<br/>
[0 0 0 0]<br/>
</p>

Now the matrix size is a power of 2 (`4x4`), making it suitable for Strassen's recursive division.

**Explanation**:
- The 3x3 matrix is shown first.
- Padding is added to make the matrix size a 4x4 matrix.
- The final result after padding is displayed.

##### In the Code,
In the function **strassen_multiply**(), padding is done using,
```bash
A_pad = np.pad(A, ((0, m - n), (0, m - n)), mode='constant')
```

- `A` is the original matrix.
- `m` is the next power of 2.
- The `np.pad()` function fills the extra rows and columns with zeros.

After the multiplication, the extra padded rows and columns are removed to restore the original matrix size.

##### Key Points About Padding,
- **Purpose**: Ensures Strassen's algorithm works correctly for non-power-of-2 matrices.
- **Effect**: Additional zeros do not affect the multiplication result.
- **Removal**: Padding is removed after multiplication to return the correct-sized result.

### NOTE 2 - The code implements the above algorithm along with python based concepts for better working and efficient code

### NOTE 3 - The algorithm and concepts are completely referenced from the textbook "*Introduction to Algorithms 3rd edition* by - *Cormen, Leiserson, Rivest and Stein (CLRS)*"

## Example Run

```bash
cd DivideAndConquer/StrassensMatrixMultiplication
```

```bash
python3 main.py

Enter 'SMultiply!' or 'exit' choice : SMultiply!
Enter the size of square matrices (e.g., 2, 4, 8): 4
Enter the elements of matrix A row by row (space-separated):
Row 1: 1 2 4 5
Row 2: 5 6 8 7
Row 3: 9 10 11 23
Row 4: 12 2 4 5
Enter the elements of matrix B row by row (space-separated):
Row 1: 8 9 10 11
Row 2: 12 3 4 2
Row 3: 67 32 4 3
Row 4: 22 3 4 8 

Matrix A:
[[ 1  2  4  5]
 [ 5  6  8  7]
 [ 9 10 11 23]
 [12  2  4  5]]

Matrix B:
[[ 8  9 10 11]
 [12  3  4  2]
 [67 32  4  3]
 [22  3  4  8]]

Result of Strassen Matrix Multiplication:
[[ 410  158   54   67]
 [ 802  340  134  147]
 [1435  532  266  336]
 [ 498  257  164  188]]

Enter 'SMultiply!' or 'exit' choice : exit
```

## Example of error handling

```bash
python3 main.py

Enter 'SMultiply!' or 'exit' choice : SMultiply!
Enter the size of square matrices (e.g., 2, 4, 8): 2
Enter the elements of matrix A row by row (space-separated):
Row 1: 1 2 3
Error: Each row must have exactly 2 elements.

Enter 'SMultiply!' or 'exit' choice : SMultiply

Sorry that was an incorrect input - please type 'SMultiply!' or 'exit' to stop.

Enter 'SMultiply!' or 'exit' choice : SMultiply!
Enter the size of square matrices (e.g., 2, 4, 8): 2
Enter the elements of matrix A row by row (space-separated):
Row 1: 1 2
Row 2: 3 4
Enter the elements of matrix B row by row (space-separated):
Row 1: 5 6 
Row 2: 6 7 8
Error: Each row must have exactly 2 elements.

Enter 'SMultiply!' or 'exit' choice : exit
```