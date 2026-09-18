## Q4 — Réponse correcte : **A**

**Explication détaillée :**

- **Le problème :** la ligne `memo = {}` est placée **à l'intérieur** de la fonction. Par conséquent, à chaque fois que la fonction s'appelle elle-même (pour calculer `n-1` puis `n-2`), un tout nouveau dictionnaire vide est créé.
- **La conséquence :** lorsque la fonction vérifie `if n in memo:`, le dictionnaire vient d'être créé et est toujours vide. Le cache ne retient donc aucun résultat intermédiaire d'un appel à l'autre. Pour corriger ce bug, il faudrait soit passer le dictionnaire en paramètre avec une valeur par défaut (ex : `def fibonacci_bug(n, memo=None):`), soit utiliser le décorateur `@lru_cache` de Python.
