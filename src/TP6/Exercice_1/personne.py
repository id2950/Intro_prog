from datetime import date


class Personne:
    def __init__(self, nom: str, prenom: str, age: int,
                 education: str, experience_professionnelle: str):

        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.education = education
        self.experience_professionnelle = experience_professionnelle

        self._demission = False
        self._licenciement = False
        self._rupture_amiable = False


    @property
    def demission(self):
        return self._demission

    @property
    def licenciement(self):
        return self._licenciement

    @property
    def rupture_amiable(self):
        return self._rupture_amiable


    def mise_a_jour_demission(self):
        self._demission = True

    def mise_a_jour_licenciement(self):
        self._licenciement = True

    def mise_a_jour_rupture_amiable(self):
        self._rupture_amiable = True