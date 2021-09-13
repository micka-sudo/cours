Trier une liste de tuples - Solution

    SOLUTION

    liste = [("Harry Potter", 5), ("Wall-E", 3), ("Blade Runner", 4)]
    liste.sort(key=lambda x: x[1])
    print(liste)

    EXPLICATION

Pas besoin d'aller chercher très loin pour résoudre cet exercice. En effet, la fonction sort accepte un argument dénommé 'key', qui va vous permettre de trier la liste selon des critères spécifiques.

Dans ce cas-ci, nous donnons comme argument au paramètre key une fonction anonyme, qui elle même nous retourne l'élément 1 de la variable qui est passée à x.

L'élément 1 du tuple correspond à la note du film, la fonction sort va donc trier les éléments de notre liste en fonction de cette élément et donc trier notre liste en fonction de la note accordée à chaque film.

    POINTS IMPORTANTS À RETENIR

    La fonction sort accepte un argument 'key', auquel nous pouvons passer une fonction lambda pour trier une liste selon des critères spécifiques.