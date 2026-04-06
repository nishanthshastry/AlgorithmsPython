# Dynamic Programming

**Dynamic Programming** is a problem-solving strategy that involves breaking a problem into smaller overlapping sub-problems, solving each sub-problem once, and storing their results to avoid redundant computations.

**Dynamic Programming Phases**
- **Divide** Phase : Break the given problem into smaller overlapping sub-problems.
- **Conquer** Phase : Solve each sub-problem recursively or iteratively.
- **Store** Phase : Store the results of sub-problems (using memoization or tabulation) to avoid recomputation.
- **Combine** Phase : Use the stored results of sub-problems to construct the final solution.

**Key Insight** - Unlike Divide and Conquer, where sub-problems are independent, Dynamic Programming deals with overlapping sub-problems, making storage and reuse essential.

**Approaches in Dynamic Programming**
- Memoization (Top-Down Approach)
    - Uses recursion
    - Stores results in a cache (dictionary / array)
    - Avoids repeated calculations
- Tabulation (Bottom-Up Approach)
    - Uses iteration
    - Builds a table step-by-step
    - More efficient in terms of function call overhead

The Algorithms covered here are,
- Basic / Foundation DP
    - Fibonacci Sequence
    - Climbing Stairs
    - House Robber
- Knapsack Pattern
    - 0/1 Knapsack
    - Unbounded Knapsack
    - Subset Sum Problem
    - Partition Equal Subset Sum
- String DP
    - Longest Common Subsequence (LCS)
    - Longest Common Substring
    - Edit Distance (Levenshtein Distance)
    - Palindrome Partitioning
- Grid / Matrix DP
    - Unique Paths
    - Minimum Path Sum
    - Maximum Path Sum
- Sequence DP
    - Longest Increasing Subsequence (LIS)
    - Maximum Subarray (Kadane’s Algorithm)
- Advanced DP
    - Matrix Chain Multiplication
    - Coin Change (Minimum Coins / Number of Ways)
    - Rod Cutting Problem
    - Longest Palindromic Subsequence

