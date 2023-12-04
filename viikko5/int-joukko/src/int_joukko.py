class IntJoukko:
    def __init__(self, kapasiteetti=5, kasvatuskoko=5):
        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko
        self.lukujono = self._luo_lista(self.kapasiteetti)
        self.alkioiden_lukumaara = 0

    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko

    def kuuluu(self, n):
        return n in self.lukujono


    def lisaa(self, n):
        if self.mahtavuus() == len(self.lukujono):
                taulukko_old = self.lukujono[:]
                self.lukujono = self._luo_lista(self.mahtavuus() + self.kasvatuskoko)
                self.tayta_lista_alusta(taulukko_old, self.lukujono)
        # elif not self.kuuluu(n):
        #     self.lukujono[self.mahtavuus()] = n


        if not self.kuuluu(n):
            self.lukujono[self.mahtavuus()] = n
            self.alkioiden_lukumaara += 1

    def poista(self, n):
        kohta = -1
        apu = 0
    
        for i in range(0, self.mahtavuus()):
            if n == self.lukujono[i]:
                kohta = i  # siis luku löytyy tuosta kohdasta :D
                self.lukujono[kohta] = 0
                break

        if kohta != -1:
            for j in range(kohta, self.alkioiden_lukumaara - 1):
                apu = self.lukujono[j]
                self.lukujono[j] = self.lukujono[j + 1]
                self.lukujono[j + 1] = apu

            self.alkioiden_lukumaara -= 1
            return True

        return False

    def tayta_lista_alusta(self, nykyinen_lukujono, taulukko_old):
        for i in range(0, len(nykyinen_lukujono)):
            taulukko_old[i] = nykyinen_lukujono[i]

    def mahtavuus(self):
        nollien_maara = self.lukujono.count(0)
        alkioiden_maara = len(self.lukujono) - nollien_maara
        return alkioiden_maara

    def to_int_list(self):
        taulu = self._luo_lista(self.mahtavuus())
        for i in range(0, len(taulu)):
            taulu[i] = self.lukujono[i]

        return taulu

    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            x.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            x.lisaa(b_taulu[i])

        return x

    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    y.lisaa(b_taulu[j])
        return y

    def erotus(eka_joukko, toka_joukko):
        kolmas_joukko = IntJoukko()
        eka_joukko_taulu = eka_joukko.to_int_list()
        toka_joukko_taulu = toka_joukko.to_int_list()

        for _, alkio in enumerate(eka_joukko_taulu):
            kolmas_joukko.lisaa(alkio)

        for _, alkio in enumerate(toka_joukko_taulu):
            kolmas_joukko.poista(alkio)

        return kolmas_joukko

    def __str__(self):
        if self.mahtavuus() == 0:
            return "{}"
        elif self.mahtavuus() == 1:
            return "{" + str(self.lukujono[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.mahtavuus() - 1):
                tuotos = tuotos + str(self.lukujono[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.lukujono[self.mahtavuus() - 1])
            tuotos = tuotos + "}"
            return tuotos
