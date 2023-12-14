from luo_peli import luo_peli


def main():
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()

        vastauksen_loppu = vastaus[-1]

        if vastauksen_loppu in ("a", "b", "c"):
            print(
                "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
            )
            peli = luo_peli(vastauksen_loppu)
            peli.pelaa()
        else:
            break


if __name__ == "__main__":
    main()
