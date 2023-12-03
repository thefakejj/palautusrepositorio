from komentopino import Komentopino

class Sovelluslogiikka:
    def __init__(self, arvo=0):
        self._arvo = arvo
        self._komentopino = Komentopino()

    def miinus(self, operandi):
        self._komentopino.puske(self.arvo())
        self._arvo = self._arvo - operandi

    def plus(self, operandi):
        self._komentopino.puske(self.arvo())
        self._arvo = self._arvo + operandi

    def nollaa(self):
        self._komentopino.puske(self.arvo())
        self._arvo = 0

    def kumoa(self):
        edellinen_arvo = self._komentopino.anna_edellinen()
        self.aseta_arvo(edellinen_arvo)

    def aseta_arvo(self, arvo):
        self._arvo = arvo

    def arvo(self):
        return self._arvo
