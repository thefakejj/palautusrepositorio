from komentopino import Komentopino

class Suorita:
    def __init__(self, sovelluslogiikka, lue_syote):
        self.sovelluslogiikka = sovelluslogiikka
        self.lue_syote = lue_syote
        self._komentopino = Komentopino()

class Summa(Suorita):
    def suorita(self):
        if type(self.lue_syote()) == int:
            self.sovelluslogiikka.plus(self.lue_syote())

class Erotus(Suorita):
    def suorita(self):
        if type(self.lue_syote()) == int:
            self.sovelluslogiikka.miinus(self.lue_syote())

class Nollaus(Suorita):
    def suorita(self):
        self.sovelluslogiikka.nollaa()

class Kumoa(Suorita):
    def suorita(self):
        self.sovelluslogiikka.kumoa()
