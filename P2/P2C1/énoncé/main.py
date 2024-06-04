def main():
    # Ecrivez votre code ici !
    # Attention tout votre code doit être indenté comme ce commentaire
    #les variable pour le calcul
    nombre_a_gauche = input("entré votre premier nombre: ")
    nombre_a_droite = input("entré votre deuxieme nombre: ")
    symbole = input("entrez le symbole entre (+, -, *, / ): ")
    resultat = 0
    #j'ai utiliser la maniére demander de faire avec le isnumeric() pour savoir si le nombre est entier ou pas
    #mais sinon je prefere utilisé l'autre maniere qui est de faire int(input("nombre entier ")) 
    # se qui oblige la personne de mettre un nombre en tier
    if not nombre_a_gauche.isnumeric() or not nombre_a_droite.isnumeric():
            print("les deux nombres ne sont pas des entier")
    else:
        #on passe les nombre en int ducoup entier 
        nombre_a_gauche = int(nombre_a_gauche)
        nombre_a_droite = int(nombre_a_droite)
        #on fait les calcule avec les symbole qu'ont mettra a
        match symbole:
            case "+":
                resultat = nombre_a_gauche + nombre_a_droite
            case "-":
                resultat = nombre_a_gauche - nombre_a_droite
            case "*":
                resultat = nombre_a_gauche * nombre_a_droite
            case "/":
                if nombre_a_droite == 0:
                    print("Erreur: impossible de diviser par zéro.")
                else:
                    resultat = nombre_a_gauche / nombre_a_droite
            case _:
    
                print("Le symbole n'est pas pris en charge")
    print("le resultat est :" ,resultat)


# Ne touchez pas le code ci-dessous
if __name__ == "__main__":
    main()
