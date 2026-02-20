from .courrier import Courrier


class Lettre(Courrier):
    def __init__(
        self, poid: int, expedition: str,
        mode: str, destination: str, format: str
    ):
        super().__init__(destination, expedition, poid, mode)
        self.format = format

        if format != "A3" or "A4":
            raise ValueError("format inexistant")

    def calcul_affranchissement(self):
        if format == "A3":
            self._afranchissement = 3.5 + (self.poid) / 100
        else:
            self._afranchissement = 2.5 + (self.poid) / 100

    def __str__(self):
        return (f"La lettre pèse {self.poid}"
                f"Il part de {self.expedition} à {self.destination} "
                f"Son mode d'éxpédition est {self.mode} "
                f"Le prix est de {self.calcul_affranchissement}")
