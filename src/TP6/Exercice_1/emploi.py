from datetime import date

from .entreprise import Entreprise
from .personne import Personne


class Poste:
    def __init__(self, employe: Personne, entreprise: Entreprise,
                 type_contrat: str, date_debut: date, date_fin: date):

        self.employe = employe
        self.entreprise = entreprise
        self.type_contrat = type_contrat
        self.date_debut = date_debut
        self.date_fin = date_fin

    def prolonger_contrat(self, nouvelle_date_fin: date):
        if nouvelle_date_fin <= self.date_fin:
            raise ValueError("La nouvelle date doit être supérieur à la date actuelle.")
        self.date_fin = nouvelle_date_fin

    def rupture_contrat(self, nouvelle_date_fin: date, motif: str):
        self.date_fin = nouvelle_date_fin

        if motif == "demission":
            self.employe.mise_a_jour_demission()
            self.entreprise.incrementer_nombre_demissions()

        elif motif == "licenciement":
            self.employe.mise_a_jour_licenciement()
            self.entreprise.incrementer_nombre_licenciements()

        elif motif == "rupture_amiable":
            self.employe.mise_a_jour_rupture_amiable()
            self.entreprise.incrementer_nombre_rupture_amiable()

        else:
            raise ValueError("Motif invalide.")

        def __str__(self):
            return (f"Poste occupé par {self.employe.prenom} {self.employe.nom} "
                    f"chez {self.entreprise.nom} {self.type_contrat} "
                    f"du {self.date_debut} au {self.date_fin} ")
