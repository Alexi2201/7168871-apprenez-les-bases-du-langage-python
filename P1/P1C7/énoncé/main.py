#creation du dictionnaire fruits.
fruits = {
    "pomme":"rouge",
    "banane":"jaune",
    "orange":"orange",}
print(fruits)
#on ajoute la clé "kiwi" et la valeur "vert".
fruits["kiwi"] = "vert"
print(fruits)
#on met la valeur de banane dans la variable "couleur_banane.
couleur_banane = fruits["banane"]
print(couleur_banane)
#on a modifier la clé pomme pour changer sa valeur "rouge" à "vert".
fruits["pomme"] = "vert"
print(fruits["pomme"])
#on supprime la clé "orange"
fruits.pop("orange")
print(fruits)
