class Komentopino:
    def __init__(self):
        self.pino = []

    def puske(self, edellinen_arvo: int):
        self.pino.append(edellinen_arvo)


    def _ota(self):
        return self.pino.pop(-1)

    def anna_edellinen(self):
        if len(self.pino) > 1:
            edellinen = self._ota()
            return edellinen
        elif len(self.pino) == 1 and self.pino[-1] == 0:
            return 0
