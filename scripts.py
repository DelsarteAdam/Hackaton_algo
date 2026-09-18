
# Top-Down recursive -> 40,7 milliards d'appels pour nth_fibonacci(50)
# O(2^n)Time || O(n)Space
def nth_fibonacci(n):
    # base case
    if n <= 1:

        return n
    # sum of the two preceding 
    # Fibonacci numbers
    return nth_fibonacci(n - 1) + nth_fibonacci(n - 2)

# Top-Down recursive -> 99 appels pour nth_fibonacci_memoized(50)
# O(n)Time || O(n)Space
from functools import lru_cache

@lru_cache(maxsize=None)
def nth_fibonacci_memoized(n: int) -> int:
    # Cas de base
    if n <= 1:
        return n
      
    # Calcul récursif avec mise en cache automatique
    return nth_fibonacci_memoized(n - 1) + nth_fibonacci_memoized(n - 2)


# Bottom-Up -> 49 itérations pour nthFibonacci(50)
# O(n)Time || O(1)Space
def nthFibonacci(n):
    if n <= 1:
        return n
    # stores current Fibonacci number
    curr = 0
    # To store the previous 
    # two Fibonacci numbers
    prev1 = 1
    prev2 = 0

    for i in range(2, n + 1):
        curr = prev1 + prev2
        # Update previous two Fibonacci 
        # numbers for next number
        prev2 = prev1
        prev1 = curr

    return curr