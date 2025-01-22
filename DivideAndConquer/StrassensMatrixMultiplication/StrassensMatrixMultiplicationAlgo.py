import numpy as np

def strassen(A, B):
    """Multiply two matrices A and B using Strassen's algorithm."""
    n = len(A)

    # Base case: if the matrix is 1x1, multiply directly
    if n == 1:
        return A * B

    # Divide matrices into quadrants
    mid = n // 2
    A11, A12, A21, A22 = A[:mid, :mid], A[:mid, mid:], A[mid:, :mid], A[mid:, mid:]
    B11, B12, B21, B22 = B[:mid, :mid], B[:mid, mid:], B[mid:, :mid], B[mid:, mid:]

    # Compute the 7 products using Strassen's formula
    M1 = strassen(A11 + A22, B11 + B22)
    M2 = strassen(A21 + A22, B11)
    M3 = strassen(A11, B12 - B22)
    M4 = strassen(A22, B21 - B11)
    M5 = strassen(A11 + A12, B22)
    M6 = strassen(A21 - A11, B11 + B12)
    M7 = strassen(A12 - A22, B21 + B22)

    # Calculate the resulting submatrices
    C11 = M1 + M4 - M5 + M7
    C12 = M3 + M5
    C21 = M2 + M4
    C22 = M1 - M2 + M3 + M6

    # Combine submatrices into a single result matrix
    C = np.vstack((np.hstack((C11, C12)), np.hstack((C21, C22))))

    return C

def next_power_of_2(n):
    """Find the next power of 2 greater than or equal to n."""
    power = 1
    while power < n:
        power *= 2
    return power

def strassen_multiply(A, B):
    """Handles matrices that aren't powers of 2 by padding."""
    assert A.shape == B.shape, "Matrices must be the same size"
    
    # Get the original size
    n = A.shape[0]
    m = next_power_of_2(n)

    # Pad matrices to the next power of 2
    A_pad = np.pad(A, ((0, m - n), (0, m - n)), mode='constant')
    B_pad = np.pad(B, ((0, m - n), (0, m - n)), mode='constant')

    # Perform Strassen multiplication
    C_pad = strassen(A_pad, B_pad)

    # Remove padding to get the final result
    return C_pad[:n, :n]

def get_matrix_input(size, matrix_name):
    """Prompt the user to input a matrix of given size."""
    print(f"Enter the elements of matrix {matrix_name} row by row (space-separated):")
    matrix = []
    for i in range(size):
        row = list(map(int, input(f"Row {i+1}: ").strip().split()))
        if len(row) != size:
            raise ValueError(f"Each row must have exactly {size} elements.")
        matrix.append(row)
    return np.array(matrix)
