## Q3 — Réponse correcte : **D**

**Explication détaillée :**

- **Le piège Python :** en Python, les arguments par défaut sont évalués **une seule et unique fois**, au moment où la fonction est définie (lors du chargement du code), et non à chaque appel. Le dictionnaire `memo` est donc un objet unique et partagé.
- **L'effet de bord :** si vous appelez `fibonacci_memo(5)`, le dictionnaire se remplit. Si vous appelez ensuite `fibonacci_memo(3)` dans un autre contexte, la fonction réutilisera directement les valeurs de l'appel précédent stockées dans ce même dictionnaire. Bien que cela puisse paraître une optimisation, c'est un piège classique qui peut perturber les résultats si l'on s'attend à un état propre à chaque exécution, ou provoquer une consommation inutile de mémoire. La bonne pratique est d'utiliser `memo=None` et d'initialiser le dictionnaire à l'intérieur du corps de la fonction (`if memo is None: memo = {}`).
