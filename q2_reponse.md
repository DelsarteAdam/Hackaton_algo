## Q2 — Réponse correcte : **C**

**Explication détaillée :**

- **Le problème :** la condition d'arrêt de la fonction est `if n == 0 or n == 1: return n`, une **égalité stricte** et non une inégalité (`<=`). Si on passe `n = -1`, cette condition n'est jamais vraie : la fonction calcule `fibonacci(-2) + fibonacci(-3)`, puis `fibonacci(-3) + fibonacci(-4)`, etc. Au lieu de s'approcher de `0` ou `1`, les valeurs s'éloignent de plus en plus vers des nombres négatifs de plus en plus grands en valeur absolue.
- **La conséquence :** la pile d'appels (_call stack_) grandit indéfiniment jusqu'à atteindre la limite maximale autorisée par Python, déclenchant un `RecursionError: maximum recursion depth exceeded`. C'est un cas limite classique (_edge case_) qui montre l'importance de valider les entrées (par exemple en ajoutant une condition `if n < 0: raise ValueError`).
- **Remarque :** si la condition d'arrêt avait été écrite avec une inégalité (`if n <= 1: return n`), alors `fibonacci(-1)` aurait retourné `-1` immédiatement, sans aucune récursion — d'où l'importance de bien distinguer `==` et `<=` dans ce type de garde-fou.
