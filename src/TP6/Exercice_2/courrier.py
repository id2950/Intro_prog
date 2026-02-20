from abc import ABC, abstractmethod


class Courrier(ABC):
    def __init__(self, destination: str, expedition: str,
                 poid: float, mode: str):

        if not isinstance(destination, str) or not destination:
            raise ValueError("Adresse destination invalide")

        if not isinstance(expedition, str) or not expedition:
            raise ValueError("Adresse expédition invalide")

        if poid <= 0:
            raise ValueError("Poids invalide")

        if mode not in ("normal", "rapide"):
            raise ValueError("Mode invalide")

        self.destination = destination
        self.expedition = expedition
        self.poid = poid
        self.mode = mode

    def _facteur_mode(self, montant: float) -> float:
        if self.mode == "rapide":
            return montant * 2
        return montant

    @abstractmethod
    def calcul_affranchissement(self):
        pass

    @abstractmethod
    def __str__(self):
        pass
