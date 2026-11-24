
from livre import Livre
from magazine import Magazine


if __name__ == "__main__":

    # Créer différents documents pour la bibliothèque
    doc1 = Livre("Les mystères du désert", 2018, "Amine Rami")

    doc2 = Magazine("Science et Découverte", 2024, 128)

    doc3 = Livre("Voyage au bout du monde", 2021, "Sara Benali")

    # Regrouper les documents dans une seule collection
    collection = [doc1, doc2, doc3]

    # Afficher les informations de chaque document
    print("=== Catalogue de la bibliothèque ===")

    for document in collection:
        document.afficher()
