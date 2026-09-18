## A. Énoncé du problème — Fibonacci

### Mise en situation

L’objectif est de calculer le **n-ième terme de la suite de Fibonacci** et de comparer plusieurs façons de résoudre le même problème.

La suite de Fibonacci est définie ainsi :

```text
F(0) = 0
F(1) = 1
F(n) = F(n-1) + F(n-2)
```

Exemple :

```text
Entrée : n = 6
Sortie : 8
```

La suite commence donc comme ceci :

```text
0, 1, 1, 2, 3, 5, 8...
```

Ce problème permet de montrer l’intérêt de la **programmation dynamique** : éviter de recalculer plusieurs fois les mêmes résultats.

### Comparaison des approches

| Approche | Principe | Temps | Espace |
|---|---|---:|---:|
| Récursive naïve | Récursion simple avec de nombreux calculs répétés | `O(2^n)` | `O(n)` |
| Récursive + `@lru_cache` | Récursion avec mémoïsation des résultats déjà calculés | `O(n)` | `O(n)` |
| Bottom-up | Calcul itératif de `F(0)` jusqu’à `F(n)` | `O(n)` | `O(n)` |

La version **récursive naïve** est simple mais inefficace, car elle recalcule plusieurs fois les mêmes valeurs.

La version **récursive avec `@lru_cache`** mémorise les résultats déjà calculés afin de les réutiliser.

L’approche **bottom-up** évite la récursion et construit progressivement les résultats à partir de `F(0)` et `F(1)`.