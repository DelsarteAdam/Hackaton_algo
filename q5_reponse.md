## Q5 — Réponse correcte : **C**

**Explication détaillée :**

- **Le problème de la récursion :** bien que `@lru_cache` résolve le problème de la complexité temporelle (la ramenant à $O(n)$ en évitant les recalculs), la fonction reste **récursive**. Chaque appel empile un niveau dans la pile d'exécution (_call stack_) de Python.
- **La limite :** pour un grand $n$ (généralement autour de 1000 en Python par défaut), la pile d'appels dépasse sa taille maximale, provoquant un `RecursionError`. À l'inverse, une approche itérative _bottom-up_ (avec une boucle `for`) n'utilise pas la pile d'appels récursive et peut calculer de très grands nombres sans ce risque.
