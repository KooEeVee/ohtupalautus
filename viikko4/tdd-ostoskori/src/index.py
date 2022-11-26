""" from tuote import Tuote
from ostoskori import Ostoskori


def main():
    kori = Ostoskori()

    maito = Tuote("Maito", 3)
    leipa = Tuote("Leipä", 6)
    kori.lisaa_tuote(maito)
    print(kori.hinta())
    kori.lisaa_tuote(maito)
    kori.lisaa_tuote(leipa)
    print(kori.ostokset())


if __name__ == "__main__":
    main() """
