
from document import Document


class Magazine(Document):

    def __init__(self, titre, annee, numero):
        # Initialiser les attributs hérités
        super().__init__(titre, annee)

        # Enregistrer le numéro du magazine
        self.numero = numero

    def afficher(self):
        # Présenter les informations spécifiques au magazine
        print(
            f"Magazine : {self.titre}, "
            f"numéro : {self.numero}, "
            f"année : {self.annee}"
        )
