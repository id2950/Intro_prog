class Entreprise:
    def __init__(self, nom: str, commune: str, chiffre_affaires: int):
        self.nom = nom
        self.commune = commune
        self.chiffre_affaires = chiffre_affaires

        self._nombre_demissions = 0
        self._nombre_licenciements = 0
        self._nombre_ruptures_amiable = 0
    
    @property
    def __nombre_demissions__(self):
        return self._nombre_demissions

    @property
    def __nombre_licenciements__(self):
        return self._nombre_licenciements

    @property
    def __nombre_ruptures_amiable__(self):
        return self._nombre_ruptures_amiable
    

    def incrementer_nombre_demissions(self):
        self._nombre_demissions += 1

    def incrementer_nombre_licenciements(self):
        self._nombre_licenciements += 1

    def incrementer_nombre_rupture_amiable(self):
        self._nombre_ruptures_amiable += 1