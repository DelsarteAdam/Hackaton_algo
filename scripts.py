from doctest import testmod

# Top-Down recursive -> 40,7 milliards d'appels pour nth_fibonacci(50)
# O(2^n)Time || O(n)Space
def nth_fibonacci(n):

    """
    
    Approche récursive de la suite de fibonacci
    teste chaque opération et sous-opération
    
    définition des inputs et outputs nth_fibonacci(arg : int) -> int:
    
    >>> nth_fibonacci(-1)
    -1
    
    >>> nth_fibonacci(5)
    5
    
    >>> nth_fibonacci(6)
    8
    
    >>> nth_fibonacci(7)
    13
        
    """

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

    """
        
    Approche récursive de la suite de fibonacci
    teste chaque opération et sous-opération

    et garde en mémoire les opérations et sous-opérations
    déjà effectuées pour gagner en vitesse d'exécution
        
    définition des inputs et outputs nth_fibonacci_memoized(arg : int) -> int:
        
    >>> nth_fibonacci_memoized(-1)
    -1
        
    >>> nth_fibonacci_memoized(5)
    5
        
    >>> nth_fibonacci_memoized(6)
    8
        
    >>> nth_fibonacci_memoized(7)
    13
            
    """

    # Cas de base
    if n <= 1:
        return n
      
    # Calcul récursif avec mise en cache automatique
    return nth_fibonacci_memoized(n - 1) + nth_fibonacci_memoized(n - 2)


# Bottom-Up -> 49 itérations pour nthFibonacci(50)
# O(n)Time || O(1)Space
def nthFibonacci(n):

    """
        
    Approche iterative de la suite de fibonacci
    teste chaque opération et sous-opération
    
    et garde en mémoire les opérations et sous-opérations
    déjà effectuées pour gagner en vitesse d'exécution
        
    définition des inputs et outputs nthFibonacci(arg : int) -> int:
        
    >>> nthFibonacci(-1)
    -1
        
    >>> nthFibonacci(5)
    5
        
    >>> nthFibonacci(6)
    8
        
    >>> nthFibonacci(7)
    13
        
    """

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

# appel la fonction 'testmod'
if __name__ == '__main__': 
    testmod(name ='Dynamique Programming', verbose = True)