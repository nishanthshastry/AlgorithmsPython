def karatsuba(x, y):
    # Base case: if x or y is a single digit, use standard multiplication
    if x < 10 or y < 10:
        return x * y

    # Determine the size of the numbers
    n = max(len(str(x)), len(str(y)))
    m = n // 2

    # Split x and y into two halves
    high1, low1 = divmod(x, 10**m)
    high2, low2 = divmod(y, 10**m)

    # Recursively compute three products
    z0 = karatsuba(low1, low2)  # BD
    z1 = karatsuba((low1 + high1), (low2 + high2))  # (A+B)(C+D)
    z2 = karatsuba(high1, high2)  # AC

    # Combine results using the Karatsuba formula
    return (z2 * 10**(2*m)) + ((z1 - z2 - z0) * 10**m) + z0

def karatsuba_Optimized(x, y):
    # Handle negative numbers
    sign = 1
    if x < 0 and y < 0:
        x, y = -x, -y  # Both negative, result is positive
    elif x < 0 or y < 0:
        x, y = abs(x), abs(y)  # One negative, result is negative
        sign = -1

    # Base case: single-digit multiplication
    if x < 10 or y < 10:
        return sign * (x * y)

    # Determine the number of digits
    n = max(len(str(x)), len(str(y)))
    m = n // 2  # Halfway point

    # Split x and y into high and low parts
    high1, low1 = divmod(x, 10**m)
    high2, low2 = divmod(y, 10**m)

    # Recursive multiplications
    z0 = karatsuba(low1, low2)      # BD
    z1 = karatsuba((low1 + high1), (low2 + high2))  # (A+B)(C+D)
    z2 = karatsuba(high1, high2)    # AC

    # Combine results using Karatsuba's formula
    result = (z2 * 10**(2*m)) + ((z1 - z2 - z0) * 10**m) + z0

    return sign * result  # Adjust sign based on input