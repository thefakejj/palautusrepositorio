class Suorita:
    def __init__(self, sovelluslogiikka, lue_syote):
        self.sovelluslogiikka = sovelluslogiikka
        self.lue_syote = lue_syote

class Summa(Suorita):
    def suorita(self):
        self.sovelluslogiikka.plus(self.lue_syote())

class Erotus(Suorita):
    def suorita(self):
        self.sovelluslogiikka.miinus(self.lue_syote())

class Nollaus(Suorita):
    def suorita(self):
        self.sovelluslogiikka.nollaa()

class Kumoa(Suorita):
    def suorita(self):
        pass
