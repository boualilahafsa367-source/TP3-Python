
from document import Document


class Livre(Document):

    def __init__(self, titre, annee, auteur):
        # Récupérer le titre et l'année depuis la classe parent
        super().__init__(titre, annee)

        # Ajouter l'auteur du livre
        self.auteur = auteur

    def afficher(self):
        # Présenter les informations spécifiques au livre
        print(
            f"Livre : {self.titre}, "
            f"auteur : {self.auteur}, "
            f"année : {self.annee}"
        )
