figure = {
    "": "",
    "kralj": "♚",
    "kraljica": "♛",
    "trdnjava": "♜",
    "lovec": "♝",
    "konj": "♞",
    "kmet": "♟"
}

barve = {0: "brez", 1: "beli", 2: "crni"}

def zamenjaj(barva):
    return 1 + barva % 2


class Igra:

    def __init__(self):
        sahovnica = [[(2, "trdnjava"), (2, "konj"), (2, "lovec"), (2, "kraljica"), (2, "kralj"), (2, "lovec"), (2, "konj"), (2, "trdnjava")]] + [8 * [(2, "kmet")]] + 4 * [8 * [(0, "")]] + [8 * [(1, "kmet")]] + [[(1, "trdnjava"), (1, "konj"), (1, "lovec"), (1, "kraljica"), (1, "kralj"), (1, "lovec"), (1, "konj"), (1, "trdnjava")]]
        sahovnica = [list(vrsta) for vrsta in sahovnica]
        self.sahovnica = sahovnica
        self.igralec = 1
        self.kralj_1 = (7, 4)
        self.kralj_2 = (0, 4)
        self.sah = []
        self.ne_premakni = {}
        self.stanje = 1

    def barva(self, i, j):
        return self.sahovnica[i][j][0]

    def barva_igra(self, i, j):
        return barve[self.barva(i, j)]

    def figura(self, i, j):
        return self.sahovnica[i][j][1]

    def figura_igra(self, i, j):
        return figure[self.figura(i, j)]

    def veljaven_premik(self, barva, i, j, upostevaj_vse = False):
        if 0 <= i <= 7 and 0 <= j <=7:
            return barva != self.barva(i, j) or upostevaj_vse
        else:
            return False

    def premakni(self, iz_i, iz_j, na_i, na_j):
        if self.figura(iz_i, iz_j) == "kralj":
            if self.barva(iz_i, iz_j) == 1:
                self.kralj_1 = (na_i, na_j)
            elif self.barva(iz_i, iz_j) == 2:
                self.kralj_2 = (na_i, na_j)
        sahovnica = self.sahovnica
        sahovnica[na_i][na_j] = sahovnica[iz_i][iz_j]
        sahovnica[iz_i][iz_j] = (0, "")
        self.sahovnica = sahovnica

    def premiki_ponavljaj(self, barva, i, j, k, l):
        premiki = []
        i += k
        j += l
        while self.veljaven_premik(barva, i, j):
            premiki.append((i, j))
            if self.barva(i, j) != 0:
                break
            else:
                i += k
                j += l
        return premiki

    def premiki_kmet(self, barva, i, j):
        premiki = []
        if barva == 1:
            if i == 6 and (self.barva(5, j), self.barva(4, j)) == (0, 0):
                premiki.append((4, j))
            i -= 1
        elif barva == 2:
            if i == 1 and (self.barva(3, j), self.barva(2, j)) == (0, 0):
                premiki.append((3, j))
            i += 1
        if self.veljaven_premik(barva, i, j) and self.barva(i, j) == 0:
            premiki.append((i, j))
        premiki += [(i, j + k) for k in (-1, 1) if self.veljaven_premik(barva, i, j + k) and self.barva(i, j + k) != 0]
        return premiki

    def premiki_konj(self, barva, i, j):
        premiki = []
        premiki += [(k, l) for k in (i - 2, i + 2) for l in (j - 1, j + 1) if self.veljaven_premik(barva, k, l)]
        premiki += [(k, l) for k in (i - 1, i + 1) for l in (j - 2, j + 2) if self.veljaven_premik(barva, k, l)]
        return premiki

    def premiki_lovec(self, barva, i, j):
        premiki = []
        for k in (-1, 1):
            for l in (-1, 1):
                premiki += self.premiki_ponavljaj(barva, i, j, k, l)
        return premiki

    def premiki_trdnjava(self, barva, i, j):
        premiki = []
        for k in (-1, 1):
            premiki += self.premiki_ponavljaj(barva, i, j, k, 0)
            premiki += self.premiki_ponavljaj(barva, i, j, 0, k)
        return premiki

    def premiki_kralj(self, barva, i, j):
        kralj = [(k, l) for k in range(i - 1, i + 2) for l in range(j - 1, j + 2) if self.veljaven_premik(barva, k, l)]
        self.sahovnica[i][j] = (0, "")
        kralj = [polje for polje in kralj if not self.preveri_sah(barva, *polje)]
        self.sahovnica[i][j] = (barva, "kralj")
        return kralj

    def dovoljen_premik(self, iz_i, iz_j, na_i, na_j, k, l):
        i, j = na_i - iz_i, na_j - iz_j
        if k == 0:
            return i == 0
        elif l == 0:
            return j == 0
        else:
            return abs(i) == abs(j) and i * j * k * l > 0

    def mozni_premiki_figura(self, figura, i, j):
        barva = self.barva(i, j)
        if figura == "kmet":
            return self.premiki_kmet(barva, i, j)
        elif figura == "konj":
            return self.premiki_konj(barva, i, j)
        elif figura == "lovec":
            return self.premiki_lovec(barva, i, j)
        elif figura == "trdnjava":
            return self.premiki_trdnjava(barva, i, j)
        elif figura == "kraljica":
            return (self.premiki_lovec(barva, i, j) + self.premiki_trdnjava(barva, i, j))
        elif figura == "kralj":
            return self.premiki_kralj(barva, i, j)

    def mozni_premiki(self, i, j):
        figura = self.figura(i, j)
        premiki = self.mozni_premiki_figura(figura, i, j)
        if (i, j) in self.ne_premakni:
            if figura == "kralj":
                premiki = [premik for premik in premiki if not self.dovoljen_premik(i, j, *premik, *self.ne_premakni[(i, j)])]
            else:
                premiki = [premik for premik in premiki if self.dovoljen_premik(i, j, *premik, *self.ne_premakni[(i, j)])]
        if self.stanje == 2 and figura != "kralj":
            return [premik for premik in premiki if premik in self.sah]
        else:
            return premiki

    def vse_figure(self):
        figure = []
        sahovnica = self.sahovnica
        for i in range(8):
            for j in range(8):
                if sahovnica[i][j][0] == self.igralec:
                    figure.append((i, j))
        return figure

    def ne_premakni_polja(self, i, j):
        polja = {}
        barva = zamenjaj(self.igralec)
        for k in range(-1, 2):
            for l in range(-1, 2):
                if (k, l) != (0, 0):
                    premik = self.premiki_ponavljaj(zamenjaj(barva), i, j, k, l)
                    if premik:
                        premik = premik[-1]
                        if self.barva(*premik) == barva and self.premiki_ponavljaj(barva, *premik, k, l) != []:
                            konec = self.premiki_ponavljaj(barva, *premik, k, l)
                            if konec:
                                konec = konec[-1]
                                if k * l == 0 and self.figura(*konec) in ("trdnjava", "kraljica"):
                                    polja[premik] = (k, l)
                                elif k * l != 0 and self.figura(*konec) in ("lovec", "kraljica"):
                                    polja[premik] = (k, l)
        return polja

    def sah_polja(self, iz_i, iz_j, na_i, na_j):
        k, l = na_i - iz_i, na_j - iz_j
        g = max(abs(k), abs(l))
        k //= g
        l //= g
        return [(iz_i + k * a, iz_j + l * a) for a in range(g)]

    def je_figura(self, figure, polja):
        return [polje for polje in polja if self.figura(*polje) in figure]

    def preveri_sah(self, barva, i, j, kralj = True):
        if barva == 1:
            kmet = [(i - 1, k) for k in (j - 1, j + 1) if self.veljaven_premik(barva, i - 1, k)]
        elif barva == 2:
            kmet = [(i + 1, k) for k in (j - 1, j + 1) if self.veljaven_premik(barva, i + 1, k)]
        sah = self.je_figura(["kmet"], kmet) + self.je_figura(["konj"], self.premiki_konj(barva, i, j)) + self.je_figura(["lovec", "kraljica"], self.premiki_lovec(barva, i, j)) + self.je_figura(["trdnjava", "kraljica"], self.premiki_trdnjava(barva, i, j))
        if kralj:
            kralj = [(k, l) for k in range(i - 1, i + 2) for l in range(j - 1, j + 2) if self.veljaven_premik(barva, k, l)]
            sah += self.je_figura(["kralj"], kralj)
        if sah == []:
            return None
        else:
            return sah[0]

    def kralj_nasprotni(self):
        if self.igralec == 1:
            return self.kralj_2
        elif self.igralec == 2:
            return self.kralj_1

    def je_sah(self, i, j):
        self.stanje = 2
        kralj = self.kralj_nasprotni()
        if self.figura(i, j) in ("lovec", "trdnjava", "kraljica"):
            sah = self.sah_polja(i, j, *kralj)
        else:
            sah = [(i, j)]
        if not any([self.preveri_sah(self.igralec, *polje, False) for polje in sah]) and self.mozni_premiki(*kralj) == []:
            self.konec_igre()
        else:
            self.stanje = 2
            self.sah = sah

    def igraj(self, iz_i, iz_j, na_i, na_j):
        kralj = self.kralj_nasprotni()
        igralec = self.igralec
        self.premakni(iz_i, iz_j, na_i, na_j)
        self.ne_premakni = self.ne_premakni_polja(*kralj)
        sah = self.preveri_sah(zamenjaj(igralec), *kralj)
        if sah:
            self.je_sah(*sah)
        else:
            self.stanje = 1
            self.sah = []
        self.igralec = zamenjaj(igralec)

    def konec_igre(self):
        self.stanje = 3
        print("Zmaga za", self.igralec)

class Sah:

    def __init__(self):
        self.igre = {}
        self.id_igre = 0

    def dodaj_igro(self):
        self.igre[self.id_igre] = Igra()
        self.id_igre += 1

    def odstrani_igro(self, id_igre):
        del self.igre[id_igre]

    def igra(self, id_igre):
        igre = self.igre
        if id_igre in igre:
            return igre[id_igre]
        else:
            return None

    def igraj(self, id_igre, iz_i, iz_j, na_i, na_j):
        nova_igra = self.igra(id_igre)
        if nova_igra:
            nova_igra.igraj(iz_i, iz_j, na_i, na_j)
            self.igre[id_igre] = nova_igra
            return nova_igra.stanje
        else:
            return 0