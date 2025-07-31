# Karatsuba Algorithm

## Karatsuba Algorithm - Divide And Conquer phases

- **Divide** Phase: Split the input numbers into smaller parts.
    - Given two `n`-digit numbers `X` and `Y`, split them as follows:
    - `X = 10^m * A + B`
    - `Y = 10^m * C + D`
    - Where:
        - `A` and `B` are the high and low halves of `X`
        - `C` and `D` are the high and low halves of `Y`
        - `m = n // 2` (approximately half the number of digits)

    This transforms the original multiplication `X * Y` into **three smaller multiplications** of half-sized numbers.
- **Conquer** Phase: Recursively solve the smaller subproblems.
    - Compute:
        1. `P1 = Karatsuba(A, C)`  → High part product `(A * C)`
        2. `P2 = Karatsuba(B, D)`  → Low part product `(B * D)`
        3. `P3 = Karatsuba(A + B, C + D)` → Sum product `(A+B) * (C+D)`
    
    Each recursive call continues splitting the numbers until reaching the **base case**, where standard multiplication is used.

- **Merge (_Combine_)** Phase: Reconstruct the final product using the recursive results.<br/>
    Using the **Karatsuba formula**:
        XY = 10<sup>2m</sup> * P1 + 10<sup>m</sup> * (P3 - P1 - P2) + P2

    - 10<sup>(2m)</sup> * P1 shifts the high part (A*C) to the correct place.
    - 10<sup>m</sup> * (P3 - P1 - P2) calculates the middle terms efficiently.
    - `P2` is the contribution of the lower part (B*D).

    This results in the final product **without requiring four multiplications**, saving computational time.

## Algorithm

**Algorithm Karatsuba** (X, Y, n)
```bash
    If n is small, return X * Y using the standard method
    Split X into A, B (higher and lower halves)
    Split Y into C, D (higher and lower halves)
    Compute
        P1 = Karatsuba(A, C)
        P2 = Karatsuba(B, D)
        P3 = Karatsuba(A + B, C + D)
    return P1 * 10^(2m) + (P3 - P1 - P2) * 10^m + P2
```

**Time complexity**: 

The **recurrence relation** for Karatsuba is:

T(n) = 3T(n/2) + O(n)

Using the **Master Theorem**, the solution is:

O(n<sup>log<sub>2</sub>3</sup>) ≈ O(n<sup>1.585</sup>)

This is **faster than traditional O(n²) multiplication** and is useful for **large number multiplications**.

### NOTE 1 - The code implements the above algorithm along with python based concepts for better working and efficient code

### NOTE 2 - The algorithm and concepts are completely referenced from the textbook "*Introduction to Algorithms 3rd edition* by - *Cormen, Leiserson, Rivest and Stein (CLRS)*"

(_Ref stackoverflow link 1_ - _[https://www.geeksforgeeks.org/dsa/karatsuba-algorithm-for-fast-multiplication-using-divide-and-conquer-algorithm/](https://www.geeksforgeeks.org/dsa/karatsuba-algorithm-for-fast-multiplication-using-divide-and-conquer-algorithm/)_)

(_Ref stackoverflow link 2_ - _[https://www.geeksforgeeks.org/dsa/karatsuba-algorithm-for-fast-multiplication-of-large-decimal-numbers-represented-as-strings/](https://www.geeksforgeeks.org/dsa/karatsuba-algorithm-for-fast-multiplication-of-large-decimal-numbers-represented-as-strings/)_)

## Example Run

```bash
cd DivideAndConquer/KaratsubaAlgorithm
```

```bash
python3 main.py

Enter 'KMultiply' or 'NegativeMultiply' or 'exit' choice : KMultiply
Enter first number : 123456
Enter second number : 986374
Multiplication of 123456 and 986374 is 121773788544

Enter 'KMultiply' or 'NegativeMultiply' or 'exit' choice : NegativeMultiply    
Enter first number : 123456
Enter second number : -34567
Negative Multiplication of 123456 and -34567 is -4267503552

Enter 'KMultiply' or 'NegativeMultiply' or 'exit' choice : exit
```

## Example of error handling

```bash
python3 main.py

Enter 'KMultiply' 'NegativeMultiply' or 'exit' choice : Kmulti

Sorry that was an incorrect input - please type 'KMultiply' or 'exit' to stop.

Enter 'KMultiply' 'NegativeMultiply' or 'exit' choice : Negative

Sorry that was an incorrect input - please type 'KMultiply' or 'exit' to stop.

Enter 'KMultiply' 'NegativeMultiply' or 'exit' choice : Multi

Sorry that was an incorrect input - please type 'KMultiply' or 'exit' to stop.

Enter 'KMultiply' 'NegativeMultiply' or 'exit' choice : exit
```