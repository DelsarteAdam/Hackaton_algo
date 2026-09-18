
from functools import lru_cache
from doctest import testmod

# retire la limite de cache pour bypass un possible overflow -> peut causer des crash
@lru_cache(maxsize=None)


def fib(n):

    """

    Approche brute de la suite de fibonacci
    teste chaque opération et sous-opération

    définition des inputs et outputs f(arg : int):

    >>> f(5)
    5

    >>> f(6)
    8

    >>> f(7)
    13
    
    """

    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib.__doc__)

# appel la fonction 'testmod' pour tester la fonction 'fig'
if __name__ == '__main__': 
    testmod(name ='factorial', verbose = True)