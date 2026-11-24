
class Document:

    def __init__(self, titre, annee):
        # Initialiser les informations communes aux documents
        self.titre = titre
        self.annee = annee

    def afficher(self):
        # Afficher les informations générales du document
        print(f"{self.titre} ({self.annee})")
