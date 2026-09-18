## Q1 — Réponse correcte : **B**

**Explication détaillée :**

- **Version naïve :** sans mémoïsation, chaque appel de `fibonacci(n)` génère deux nouveaux appels (`n-1` et `n-2`). Cela crée un arbre d'appels récursifs dont le nombre de nœuds double presque à chaque niveau, menant à une explosion exponentielle de complexité en $O(2^n)$ (le code devient très lent dès que $n$ dépasse 35 ou 40).
- **Version mémoïsée / bottom-up :** en stockant les résultats déjà calculés (dans un dictionnaire ou un tableau), chaque valeur de $0$ à $n$ n'est calculée qu'**une seule fois**. On parcourt les nombres de façon linéaire, ce qui réduit la complexité à $O(n)$.
