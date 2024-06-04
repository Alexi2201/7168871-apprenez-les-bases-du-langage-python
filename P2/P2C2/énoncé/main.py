def main():
    liste = input("choisiser une liste de nombre separer par des vergule (ex:1,2,3,4): ")
    liste = liste.split(",")
    print("la liste de nombre :",liste)
    #nous allons calculer la somme
    somme = 0
    for nombre in liste:
        somme += int(nombre)
    print("somme des nombres :", somme)
    moyenne = somme / len(liste)
    print("la moyenne des nombres :",moyenne)
    nombre_sup_moyenne = 0
    for nombre in liste:
        if int(nombre)>moyenne:
            nombre_sup_moyenne += 1
    print("nombre supérieurs à la moyenne :", nombre_sup_moyenne)
    paire = 0
    i = 0
    while i < len(liste):
        if int(liste[i]) % 2 ==0 :
            paire += 1

        i += 1
    print("nombre paire: " ,paire)



if __name__ == "__main__":
   main()
