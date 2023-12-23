#!/usr/bin/python3

class SzambolSzoveg:

    """
    Author: Máté Gál
    Date: 23-Dec-2023
    Contact: gal.mateo@gmail.com 
    This class converts integers to hungarian text
    Ez az osztály egész számokat alakít át szöveggé
    """

    def __init__(self):
        self.int_szam = 0
        self.szam_dict = {  0 : "", 1 : "egy", 2 : "kettő", 3  : "három", 4  : "négy", 5  : "öt", 6  : "hat", 7  : "hét", 8  : "nyolc", 9  : "kilenc",
                            10  : "tíz", 20  : "húsz", 30  : "harminc", 40  : "negyven", 50  : "ötven", 60  : "hatvan", 70  : "hetven", 80  : "nyolcvan", 90  : "kilencven" }

    def konverzio(self, szam):
        # Konverzió
        self.int_szam = szam
        if isinstance(self.int_szam, int):
            if self.int_szam < 10:
                return self.tizig()
            elif self.int_szam < 100:
                return self.szazig()
            elif self.int_szam < 1000:
                return self.ezerig()
            elif self.int_szam < 1000000:
                return self.millioig()
        else:
            raise AssertionError("A szám nem egész!")

    def tizig(self):        
        # Egyjegyűek
        if self.int_szam < 10:
            return self.szam_dict[self.int_szam]

    def szazig(self):
        # Kétjegyűek 
        if ((self.int_szam % 10) == 0):
            return self.szam_dict[self.int_szam]
        else:
            if (10 < self.int_szam < 20):
                return "tizen" + self.szam_dict[int(str(self.int_szam)[1])]
            if (20 < self.int_szam < 30):
                return "huszon" + self.szam_dict[int(str(self.int_szam)[1])]
            if (30 < self.int_szam < 100):
                return self.szam_dict[int(str(self.int_szam)[0])*10] + self.szam_dict[int(str(self.int_szam)[1])]

    def ezerig(self):
        # Háromjegyűek
        szaz = 'száz'
        szam_str = ''
        if (self.int_szam % 100) == 0:
            if self.int_szam != 100:
                szam_str += self.konverzio(int(str(self.int_szam)[0])) + szaz
            else:
                szam_str += szaz
        else:
            if 200 < self.int_szam:
                szam_str += self.szam_dict[int(str(self.int_szam)[0])] + szaz + self.konverzio(int(str(self.int_szam)[1:4]))
            else:
                szam_str += szaz + self.konverzio(int(str(self.int_szam)[1:4])) 
        return szam_str

    def millioig(self):
        # Négy- öt- és hatjegyűek
        ezer = 'ezer'
        szam_str = ''
        if (self.int_szam % 1000) == 0:
            if self.int_szam != 1000:
                szam_str += self.konverzio(int(str(self.int_szam)[0])) + ezer
            else:
                szam_str += ezer
        else:   
            if 100000 < self.int_szam:
                szazasok = int(str(self.int_szam)[0:3])
                ezresek = int(str(self.int_szam)[3:6])
                szam_str += self.konverzio(szazasok) + ezer + self.konverzio(ezresek)
            elif 10000 < self.int_szam:
                tizesek = int(str(self.int_szam)[0:2])
                ezresek = int(str(self.int_szam)[2:5])
                szam_str += self.konverzio(tizesek) + ezer + self.konverzio(ezresek)
            elif 2000 < self.int_szam:
                egyesek = int(str(self.int_szam)[0])
                ezresek = int(str(self.int_szam)[1:4])
                szam_str += self.szam_dict[egyesek] + ezer + self.konverzio(ezresek)
            else:
                szam_str += ezer + self.konverzio(int(str(self.int_szam)[1:4])) 
        return szam_str

z_lista = []
szambol_szoveg = SzambolSzoveg()
for szam in range(1000000, 0, -1):
    z_szamlalo = 0
    konvertalt = szambol_szoveg.konverzio(szam)
    if konvertalt:
        for char in konvertalt:
            if char == 'z':
                z_szamlalo += 1
        if z_szamlalo == 0:
            print(konvertalt, szam)
            break
