
class Employe:

    def __init__(self, nom, salaire_base):
        # Initialiser les informations communes
        self.nom = nom
        self.salaire_base = salaire_base

    def salaire_total(self):
        # Un employé standard reçoit uniquement son salaire de base
        return self.salaire_base

    def __str__(self):
        # Afficher le nom et le salaire calculé
        return f"{self.nom} gagne {self.salaire_total()} €"
