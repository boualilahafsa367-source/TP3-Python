
from employe import Employe


class Developpeur(Employe):

    def __init__(self, nom, salaire_base, technologie):
        # Initialiser les attributs hérités
        super().__init__(nom, salaire_base)

        # Enregistrer la technologie du développeur
        self.technologie = technologie

    def salaire_total(self):
        # Déterminer le bonus selon la technologie
        if self.technologie == "Python":
            bonus = 500
        else:
            bonus = 300

        # Retourner le salaire avec le bonus
        return self.salaire_base + bonus
