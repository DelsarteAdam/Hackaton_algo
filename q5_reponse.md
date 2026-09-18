## Q5 — Réponse correcte : **C**

**Explication détaillée :**

- **Le problème de la récursion :** bien que `@lru_cache` résolve le problème de la complexité temporelle (la ramenant à $O(n)$ en évitant les recalculs), la fonction reste **récursive**. Chaque appel empile un niveau dans la pile d'exécution (_call stack_) de Python.
- **La limite :** pour un grand $n$ (généralement autour de 1000 en Python par défaut), la pile d'appels dépasse sa taille maximale, provoquant un `RecursionError`. À l'inverse, une approche itérative _bottom-up_ (avec une boucle `for`, voir le code `fib_bottom_up` ci-dessus) n'utilise pas la pile d'appels récursive et peut calculer de très grands nombres sans ce risque.
- **Pourquoi l'option D est fausse :** `@lru_cache` stocke un résultat par valeur de `n` déjà calculée, donc une mémoire en $O(n)$ — exactement comme une version bottom-up qui utiliserait un tableau. La version bottom-up présentée ici va même plus loin en n'utilisant que deux variables (`a`, `b`), ce qui donne une mémoire en $O(1)$. La différence réelle entre `lru_cache` ($O(n)$) et le bottom-up optimisé ($O(1)$) est donc **linéaire**, pas **exponentielle** : le terme "exponentiellement" dans l'option D est incorrect, ce qui en fait une mauvaise réponse malgré une intuition de départ (lru_cache consomme bien un peu plus de mémoire) qui n'est pas totalement infondée.
