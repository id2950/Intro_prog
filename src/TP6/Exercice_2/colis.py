from .courrier import Courrier


class Colis(Courrier):
    def __init__(
        self, poid: int, expedition: str,
        mode: str, destination: str, volume: int
    ):
        super().__init__(destination, expedition, poid, mode)
        self.volume = volume

        if volume <= 0:
            raise ValueError("le volume doit être positif")

    def calcul_affranchissement(self):
        self._afranchissement = self.volume / 4 + self.poid

    def __str__(self):
        return (f"Le colis pèse {self.poid}"
                f"Il part de {self.expedition} à {self.destination} "
                f"Son mode d'éxpédition est {self.mode} "
                f"Le prix est de {self.calcul_affranchissement}")
