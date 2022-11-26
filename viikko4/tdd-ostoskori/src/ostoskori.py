from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.ostoskori = []
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        lukumaara = 0
        if len(self.ostoskori) > 0:
            for ostos in self.ostoskori:
                lukumaara += ostos.lukumaara()
        return lukumaara
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        hinta = 0
        if len(self.ostoskori) > 0:
            for ostos in self.ostoskori:
                hinta += ostos.hinta()
        return hinta
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        if len(self.ostoskori) == 0:
            ostos = Ostos(lisattava)
            self.ostoskori.append(ostos)
        else:
            for ostos in self.ostoskori:
                if ostos.tuotteen_nimi() == lisattava.nimi:
                    ostos.muuta_lukumaaraa(1)
                else:
                    ostos = Ostos(lisattava)
                    self.ostoskori.append(ostos)
        # lisää tuotteen

    def poista_tuote(self, poistettava: Tuote):
        pass
        # poistaa tuotteen

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        pass
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
