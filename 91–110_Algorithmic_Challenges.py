# 91. Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# 92. Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# 93. Selection Sort
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# 94. Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# 95. Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# 96. Binary Search
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# 97. Linear Search
def linear_search(arr, target):
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1

# 98. Knuth Shuffle (Fisher-Yates Shuffle)
import random

def fisher_yates_shuffle(arr):
    for i in range(len(arr) - 1, 0, -1):
        j = random.randint(0, i)
        arr[i], arr[j] = arr[j], arr[i]
    return arr

# 99. Matrix Addition
def matrix_addition(mat1, mat2):
    rows, cols = len(mat1), len(mat1[0])
    result = [[mat1[i][j] + mat2[i][j] for j in range(cols)] for i in range(rows)]
    return result

# 100. Matrix Multiplication
def matrix_multiplication(mat1, mat2):
    rows1, cols1 = len(mat1), len(mat1[0])
    rows2, cols2 = len(mat2), len(mat2[0])
    if cols1 != rows2:
        return None  # Incompatible dimensions
    result = [[sum(mat1[i][k] * mat2[k][j] for k in range(cols1)) for j in range(cols2)] for i in range(rows1)]
    return result

# 101. Transposition of a Matrix
def transpose_matrix(matrix):
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]

# 102. Check if a Matrix is Symmetric
def is_symmetric(matrix):
    return matrix == transpose_matrix(matrix)

# 103. Longest Common Substring
def longest_common_substring(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    longest = 0
    end_idx = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > longest:
                    longest = dp[i][j]
                    end_idx = i
    return str1[end_idx - longest:end_idx]

# 104. Longest Common Subsequence (LCS)
def longest_common_subsequence(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[""] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + str1[i - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], key=len)
    return dp[m][n]

# 105. Coin Change (Greedy)
def coin_change_greedy(coins, target):
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        if target == 0:
            break
        count += target // coin
        target %= coin
    return count if target == 0 else -1

# 106. Coin Change (DP)
def coin_change_dp(coins, target):
    dp = [float('inf')] * (target + 1)
    dp[0] = 0
    for coin in coins:
        for i in range(coin, target + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[target] if dp[target] != float('inf') else -1

# 107. Knapsack Problem (0/1 DP)
def knapsack(values, weights, capacity):
    n = len(values)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
    return dp[n][capacity]

# 108. Permutations of a List
from itertools import permutations

def generate_permutations(lst):
    return list(permutations(lst))

# 109. Backtracking: N-Queens
def solve_n_queens(n):
    board = [-1] * n
    solutions = []

    def is_safe(row, col):
        for prev_row in range(row):
            if board[prev_row] == col or abs(board[prev_row] - col) == abs(prev_row - row):
                return False
        return True

    def place_queen(row):
        if row == n:
            solutions.append(board[:])
            return
        for col in range(n):
            if is_safe(row, col):
                board[row] = col
                place_queen(row + 1)

    place_queen(0)
    return solutions

# 110. Shortest Path in a Grid
from collections import deque

def shortest_path(grid):
    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (1, 0)]
    queue = deque([(0, 0, 0)])  # (row, col, steps)
    visited = set()
    while queue:
        r, c, steps = queue.popleft()
        if (r, c) == (rows - 1, cols - 1):
            return steps
        if (r, c) in visited:
            continue
        visited.add((r, c))
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                queue.append((nr, nc, steps + 1))
    return -1
