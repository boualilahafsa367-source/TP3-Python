
from employe import Employe


class Manager(Employe):

    def __init__(self, nom, salaire_base, prime):
        # Réutiliser le constructeur de la classe parent
        super().__init__(nom, salaire_base)

        # Ajouter l'attribut spécifique au manager
        self.prime = prime

    def salaire_total(self):
        # Ajouter la prime au salaire de base
        return self.salaire_base + self.prime
