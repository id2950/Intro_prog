class Entreprise:
    def __init__(self, nom: str, commune: str, chiffre_affaires: int):
        self.nom = nom
        self.commune = commune
        self.chiffre_affaires = chiffre_affaires

        self._nombre_demissions = 0
        self._nombre_licenciements = 0
        self._nombre_ruptures_amiable = 0
    
    __property
    def nombre_demissions(self):
        return self._nombre_demissions

    __property
    def nombre_licenciements(self):
        return self._nombre_licenciements

    __property
    def nombre_ruptures_amiable(self):
        return self._nombre_ruptures_amiable
    

    def incrementer_nombre_demissions(self):
        self._nombre_demissions += 1

    def incrementer_nombre_licenciements(self):
        self._nombre_licenciements += 1

    def incrementer_nombre_rupture_amiable(self):
        self._nombre_ruptures_amiable += 1