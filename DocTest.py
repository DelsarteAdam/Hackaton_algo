#region Top Down Brute

from functools import lru_cache
from doctest import testmod

# retire la limite de cache pour bypass les overflows
# peut causer des crash
@lru_cache(maxsize = None)
def fib(n):

    """

    Approche brute de la suite de fibonacci
    teste chaque opération et sous-opération

    définition des inputs et outputs fib(arg : int) -> int:

    >>> fib(-1)
    -1

    >>> fib(5)
    5

    >>> fib(6)
    8

    >>> fib(7)
    13
    
    """

    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib.__doc__)

# appel la fonction 'testmod'
if __name__ == '__main__': 
    testmod(name ='Dynamique Programming', verbose = True)

#endregion

#region Top Down Memoization

def fib_mem(n, memo):

    """
    
    Approche recursive de la suite de fibonacci
    teste chaque opération et sous-opération
    et garde en mémoire les opérations et sous-opérations
    déjà effectuées pour gagner en vitesse d'exécution
    
    définition des inputs et outputs fib_mem(arg : int) -> int:
    
    >>> fib_mem(-1)
    -1
    
    >>> fib_mem(5)
    5
    
    >>> fib_mem(6)
    8
    
    >>> fib_mem(7)
    13
        
    """

    if n <= 1:
        return n

    if memo[n] != -1:
        return memo[n]

    memo[n] = fib_tab(n - 1, memo) + fib_tab(n - 2, memo)
    return memo[n]

def fib(n):
    memo = [-1] * (n + 1)
    return fib_mem(n, memo)

print(fib_mem.__doc__)

# appel la fonction 'testmod'
if __name__ == '__main__': 
    testmod(name ='Dynamique Programming', verbose = True)

#endregion

#region Bottom Up Tabulation

def fib_tab(n):

    """
    
    Approche iterative de la suite de fibonacci
    teste chaque opération et sous-opération
    et garde en mémoire les opérations et sous-opérations
    déjà effectuées pour gagner en vitesse d'exécution
    
    définition des inputs et outputs fib(arg : int) -> int:
    
    >>> fib_tab(-1)
    -1
    
    >>> fib_tab(5)
    5
    
    >>> fib_tab(6)
    8
    
    >>> fib_tab(7)
    13
        
    """

    dp = [0] * (n + 1)

    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]

print(fib_tab.__doc__)

# appel la fonction 'testmod'
if __name__ == '__main__': 
    testmod(name ='Dynamique Programming', verbose = True)

#endregion