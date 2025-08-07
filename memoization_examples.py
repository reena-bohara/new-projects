# memoization_examples.py

"""
This module provides detailed, real-world-inspired examples of memoization
in Python, especially relevant for optimization problems in e-commerce.
Each function includes documentation, comments, and practical value.
"""

from typing import Dict, Tuple

# -----------------------------------------------------------------------------
# 1. Fibonacci with Memoization (Basic Introduction)
# -----------------------------------------------------------------------------
def fibonacci(n: int, memo: Dict[int, int] = {}) -> int:
    """
    Compute the nth Fibonacci number using memoization to avoid redundant calls.

    Args:
        n: Position in the Fibonacci sequence.
        memo: Cache dictionary to store previously computed values.

    Returns:
        The nth Fibonacci number.
    """
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]

# -----------------------------------------------------------------------------
# 2. Price Combination Finder (Knapsack-like Problem)
# -----------------------------------------------------------------------------
def max_cart_value(prices: list, capacity: int, memo: Dict[Tuple[int, int], int] = {}) -> int:
    """
    Find the maximum total value we can achieve from a list of product prices
    without exceeding the cart capacity (similar to 0/1 knapsack).

    Args:
        prices: List of item prices (values).
        capacity: Budget or maximum allowed sum.
        memo: Dictionary for memoizing computed states.

    Returns:
        The maximum sum ≤ capacity.
    """
    def helper(i: int, remaining: int) -> int:
        if i == len(prices) or remaining == 0:
            return 0
        if (i, remaining) in memo:
            return memo[(i, remaining)]

        # Skip item
        without = helper(i + 1, remaining)

        # Take item if it fits
        with_item = 0
        if prices[i] <= remaining:
            with_item = prices[i] + helper(i + 1, remaining - prices[i])

        memo[(i, remaining)] = max(without, with_item)
        return memo[(i, remaining)]

    return helper(0, capacity)

# -----------------------------------------------------------------------------
# 3. Promotion Path Optimizer (Recursive Graph-Like Search)
# -----------------------------------------------------------------------------
def promotion_paths(promo_map: Dict[str, list], start: str, end: str, memo=None) -> int:
    """
    Count the number of unique promotion paths from `start` to `end`.

    Args:
        promo_map: Dict representing directed promo transition paths.
        start: Starting promotion step.
        end: Target promotion step.
        memo: Cache of sub-path counts.

    Returns:
        Number of distinct valid paths.
    """
    if memo is None:
        memo = {}
    if start == end:
        return 1
    if start in memo:
        return memo[start]

    total_paths = 0
    for next_promo in promo_map.get(start, []):
        total_paths += promotion_paths(promo_map, next_promo, end, memo)

    memo[start] = total_paths
    return total_paths

# -----------------------------------------------------------------------------
# Main Execution with Demo
# -----------------------------------------------------------------------------
if __name__ == '__main__':
    print("\n--- Fibonacci Demo ---")
    print("Fibonacci(10):", fibonacci(10))

    print("\n--- Max Cart Value Demo ---")
    prices = [20, 10, 30, 25]
    capacity = 50
    print("Max cart value for capacity 50:", max_cart_value(prices, capacity))

    print("\n--- Promotion Path Optimizer Demo ---")
    promo_map = {
        'Start': ['A', 'B'],
        'A': ['C'],
        'B': ['C', 'D'],
        'C': ['End'],
        'D': ['End']
    }
    print("Total promotion paths from Start to End:", promotion_paths(promo_map, 'Start', 'End'))
