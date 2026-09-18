# QCM : Récursion, Mémoïsation et Optimisation — L'exemple de Fibonacci

---

## Q1 (Complexité) : La récursion naïve vs optimisée de Fibonacci

**Question :** Quelle est la complexité temporelle d'une fonction récursive **naïve** pour calculer le $n$-ième terme de la suite de Fibonacci, et comment cette complexité évolue-t-elle lorsqu'on applique la **mémoïsation** (ou une approche _bottom-up_) ?

- **A)** Naïve : $O(n)$ | Mémoïsée : $O(1)$
- **B)** Naïve : $O(2^n)$ | Mémoïsée : $O(n)$
- **C)** Naïve : $O(n^2)$ | Mémoïsée : $O(\log n)$
- **D)** Naïve : $O(2^n)$ | Mémoïsée : $O(2^n)$

---

## Q2 (Edge Case) : Le comportement avec un cas limite (nombre négatif)

**Question :** Que se passe-t-il si on exécute la fonction récursive naïve de Fibonacci suivante avec un nombre entier négatif (par exemple, `n = -1`) ?

```python
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
```

- **A)** Elle retourne `0` immédiatement car les nombres négatifs sont plus petits que `1`.
- **B)** Elle entre dans une récursion infinie, ce qui finit par lever une erreur de type `RecursionError` (dépassement de pile).
- **C)** Elle convertit automatiquement le nombre négatif en sa valeur positive.
- **D)** Elle retourne `-1` par convention mathématique.

---

## Q3 (Piège / Effet de bord) : Le piège de l'argument par défaut mutable

**Question :** Observez la fonction de Fibonacci suivante utilisant un dictionnaire en argument par défaut pour la mémoïsation. Quel effet de bord majeur cela peut-il provoquer lors de multiples appels successifs ?

```python
def fibonacci_memo(n, memo={}):
    if n <= 1:
        return n
    if n in memo:
        return memo[n]
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]
```

- **A)** Le dictionnaire `memo` est réinitialisé à vide à chaque nouvel appel de la fonction, ce qui rend la mémoïsation inefficace.
- **B)** Le dictionnaire `memo` persiste entre les différents appels de la fonction, ce qui fait que les résultats calculés lors d'un premier appel restent stockés et sont réutilisés dans les appels suivants (ce qui peut causer des comportements inattendus ou une persistance d'état non désirée).
- **C)** Python lève une exception `TypeError` car un dictionnaire ne peut pas être passé en argument par défaut.
- **D)** Le code plante avec une erreur `KeyError` dès le deuxième appel.

---

## Q4 (Trouver le Bug) : Une mémoïsation inefficace à cause de l'initialisation

**Question :** L'extrait de code suivant tente d'implémenter une fonction récursive de Fibonacci avec de la mémoïsation. Cependant, un bug de conception rend la mémoïsation totalement inefficace et la fonction garde une complexité exponentielle $O(2^n)$. Quel est ce bug ?

```python
def fibonacci_bug(n):
    memo = {}
    if n <= 1:
        return n
    if n in memo:
        return memo[n]
    memo[n] = fibonacci_bug(n - 1) + fibonacci_bug(n - 2)
    return memo[n]
```

- **A)** Le dictionnaire `memo` est recréé et réinitialisé à vide (`{}`) à **chaque appel récursif**, ce qui fait que le cache est effacé en permanence et n'enregistre rien d'utile.
- **B)** La syntaxe pour vérifier la présence d'une clé avec `in` est incorrecte en Python.
- **C)** Il manque un opérateur `return` lors du stockage de la valeur dans `memo[n]`.
- **D)** La condition d'arrêt (`n <= 1`) empêche d'atteindre le dictionnaire `memo`.

---

## Q5 (Optimisation) : `@lru_cache` vs Approche Bottom-Up

**Question :** Vous devez calculer le $n$-ième terme de Fibonacci pour un grand nombre $n$ (par exemple $n = 500$). Entre l'utilisation d'une fonction récursive décorée avec `@lru_cache(maxsize=None)` et une approche itérative _bottom-up_ (avec un tableau ou deux variables), quelle est la principale limite de la version avec `@lru_cache` en Python ?

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib_lru(n):
    if n <= 1:
        return n
    return fib_lru(n - 1) + fib_lru(n - 2)
```

- **A)** Elle est beaucoup plus lente que l'approche _bottom-up_ en raison du temps de recherche dans le dictionnaire du cache.
- **B)** Elle ne fonctionne pas avec les nombres entiers et lève une exception.
- **C)** Elle risque de provoquer une erreur de type `RecursionError` (dépassement de pile) si $n$ dépasse la limite de récursion maximale de Python, contrairement à l'approche _bottom-up_ itérative.
- **D)** Elle consomme exponentiellement plus de mémoire que l'approche _bottom-up_.

---

---
