
from employe import Employe
from manager import Manager
from developpeur import Developpeur


if __name__ == "__main__":

    # Créer un employé standard
    personne1 = Employe("Nadia", 2800)

    # Créer un manager avec une prime
    personne2 = Manager("Karim", 3500, 950)

    # Créer un développeur spécialisé en Java
    personne3 = Developpeur("Imane", 3200, "Java")

    # Regrouper les différents employés dans une liste
    equipe = [personne1, personne2, personne3]

    # Afficher les informations de chaque employé
    print("=== Liste des employés ===")

    for personne in equipe:
        print(personne)
