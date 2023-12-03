class Komentopino:
    def __init__(self):
        # self.summa = komennot[Komento.SUMMA]
        # self.erotus = komennot[Komento.EROTUS]
        # self.nollaus = komennot[Komento.NOLLAUS]
        self.pino = []

    def puske(self, edellinen_arvo: int):
        print("edellinen_arvo:", edellinen_arvo)
        print("type:", type(edellinen_arvo))
        # def puske(self, edellinen_operaatio, syote):
        # tila = {
        #     "edellinen_state": edellinen_state,
        #     "edellinen_operaatio": (edellinen_operaatio, syote)
        # }
        self.pino.append(edellinen_arvo)
        print(self.pino)


    def _ota(self):
        return self.pino.pop(-1)

    def anna_edellinen(self):
        print(self.pino)
        if len(self.pino) > 1:
            edellinen = self._ota()
            return edellinen
        elif len(self.pino) == 1 and self.pino[-1] == 0:
            return 0
