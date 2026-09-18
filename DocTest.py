#region Bottom Up

from functools import lru_cache
from doctest import testmod

# retire la limite de cache pour bypass les overflows
# peut causer des crash
@lru_cache(maxsize=None)
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

# appel la fonction 'testmod' pour tester la fonction 'fib'
# par rapport à sa documentation
if __name__ == '__main__': 
    testmod(name ='factorial', verbose = True)

#endregion