def salaire_mensuel(salaire_annuel):
    # Calcule le salaire mensuel à partir du salaire annuel
    return salaire_annuel / 12

def salaire_hebdomadaire(salaire_mensuel):
    # Calcule le salaire hebdomadaire à partir du salaire mensuel
    # Utilise une approximation plus précise du nombre de semaines par mois
    return salaire_mensuel / (52 / 12)

def salaire_horaire(salaire_hebdomadaire, heures_travaillees):
    # Calcule le salaire horaire à partir du salaire hebdomadaire et du nombre d'heures travaillées par semaine
    return salaire_hebdomadaire / heures_travaillees

def main():
    try:
        # Demande à l'utilisateur de saisir son salaire annuel et ses heures de travail par semaine
        salaire_annuel = float(input("Écrivez votre salaire annuel: "))
        heures_travaillees = float(input("Écrivez vos heures de travail par semaine: "))
        
        # Vérifie que les valeurs saisies sont valides
        if salaire_annuel < 0 or heures_travaillees <= 0:
            raise ValueError("Le salaire annuel doit être positif et les heures de travail doivent être supérieures à zéro.")
        
        # Calcule le salaire mensuel, hebdomadaire et horaire
        mensuel = salaire_mensuel(salaire_annuel)
        hebdomadaire = salaire_hebdomadaire(mensuel)
        horaire = salaire_horaire(hebdomadaire, heures_travaillees)
        
        # Affiche le salaire horaire avec deux décimales
        print(f"Votre salaire horaire est de {horaire:.2f} euros")
    except ValueError as e:
        # Affiche un message d'erreur en cas d'entrée invalide
        print(f"Entrée invalide: {e}")

if __name__ == "__main__":
    # Exécute la fonction main() si ce fichier est exécuté directement
    main()
