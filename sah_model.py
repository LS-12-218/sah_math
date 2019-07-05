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


class Igra:
    def __init__(self):
        sahovnica = [[(2, "trdnjava"), (2, "konj"), (2, "lovec"), (2, "kraljica"), (2, "kralj"), (2, "lovec"), (2, "konj"), (2, "trdnjava")]] + [8 * [(2, "kmet")]] + 4 * [8 * [(0, "")]] + [8 * [(1, "kmet")]] + [[(1, "trdnjava"), (1, "konj"), (1, "lovec"), (1, "kraljica"), (1, "kralj"), (1, "lovec"), (1, "konj"), (1, "trdnjava")]]
        sahovnica = [list(vrsta) for vrsta in sahovnica]
        self.sahovnica = sahovnica
        self.igralec = 1
        self.kralj_1 = (7, 4)
        self.kralj_2 = (0, 4)
        self.sah = set()
        self.premiki_1 = (set(), set())
        self.premiki_2 = (set(), set())
        self.ne_premakni_1 = {}
        self.ne_premakni_2 = {}
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

    def veljaven_premik_kralj(self, barva, i, j, upostevaj_vse = False):
        if self.veljaven_premik(barva, i, j, upostevaj_vse):
            if barva == 1 and (i, j) not in self.premiki_2[0]:
                return True
            elif barva == 2 and (i, j) not in self.premiki_1[0]:
                return True
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

    def premik_indeks(self, barva, i, j):
        if self.barva(i, j) in [0, barva]:
            return 0
        else:
            return 1

    def mozni_premiki(self, i, j, preveri = False):
        barva = self.barva(i, j)
        figura = self.figura(i, j)
        premiki = set()

        if figura == "kmet":
            if barva == 1:
                if i == 6 and self.barva(4, j) == 0 and not preveri:
                    premiki.add((4, j))
                ii = i - 1
            elif barva == 2:
                if i == 1 and self.barva(3, j) == 0 and not preveri:
                    premiki.add((3, j))
                ii = i + 1
            if self.veljaven_premik(barva, ii, j) and self.barva(ii, j) == 0 and not preveri:
                premiki.add((ii, j))
            premiki.update({(ii, j + k) for k in [-1, 1] if self.veljaven_premik(barva, ii, j + k, preveri) and (self.barva(ii, j + k) != 0 or preveri)})

        elif figura == "konj":
            for k in [-2, 2]:
                for l in [-1, 1]:
                    if self.veljaven_premik(barva, i + k, j + l, preveri):
                        premiki.add((i + k, j + l))
                    if self.veljaven_premik(barva, i + l, j + k, preveri):
                        premiki.add((i + l, j + k))

        elif figura in ["lovec", "kraljica"]:
            for k in [-1, 1]:
                for l in [-1, 1]:
                    ii = i + k
                    jj = j + l
                    while self.veljaven_premik(barva, ii, jj, preveri):
                        premiki.add((ii, jj))
                        if self.barva(ii, jj) != 0:
                            if preveri and self.barva(ii, jj) != barva:
                                self.ne_premakni(barva, ii, jj, k, l)
                            break
                        else:
                            ii += k
                            jj += l

        if figura in ["trdnjava", "kraljica"]:
            for k in [-1, 1]:
                ii = i + k
                while self.veljaven_premik(barva, ii, j, preveri):
                    premiki.add((ii, j))
                    if self.barva(ii, j) != 0:
                        if preveri and self.barva(ii, j) != barva:
                            self.ne_premakni(barva, ii, j, k, 0)
                        break
                    else:
                        ii += k
                jj = j + k
                while self.veljaven_premik(barva, i, jj, preveri):
                    premiki.add((i, jj))
                    if self.barva(i, jj) != 0:
                        if preveri and self.barva(i, jj) != barva:
                            self.ne_premakni(barva, i, jj, 0, k)
                        break
                    else:
                        jj += k

        elif figura == "kralj":
            for k in range(-1, 2):
                for l in range(-1, 2):
                    if self.veljaven_premik_kralj(barva, i + k, j + l, preveri) and [k, l] != [0, 0]:
                        premiki.add((i + k, j + l))

        if barva == 1 and (i, j) in self.ne_premakni_1:
            k, l = self.ne_premakni_1[(i, j)]
            prepovedano = {(i + k * a, j + l * a) for a in range(-8, 9)}
            if figura == "kralj":
                premiki -= prepovedano
            else:
                premiki &= prepovedano
        elif barva == 2 and (i, j) in self.ne_premakni_2:
            k, l = self.ne_premakni_2[(i, j)]
            prepovedano = {(i + k * a, j + l * a) for a in range(-8, 9)}
            if figura == "kralj":
                premiki -= prepovedano
            else:
                premiki &= prepovedano

        if self.stanje == 2 and figura != "kralj":
            return premiki & self.sah
        else:
            return premiki

    def ne_premakni(self, barva, i, j, k, l):
        if barva == 1:
            ne_premaknil = self.ne_premakni_2
            kralj = self.kralj_2
        else:
            ne_premaknil = self.ne_premakni_1
            kralj = self.kralj_1
        if (i, j) == kralj:
            ne_premaknil[(i, j)] = (k, l)
        ii = i + k
        jj = j + l
        while self.veljaven_premik(barva, ii, jj):
            if (ii, jj) == kralj:
                ne_premaknil[(i, j)] = (k, l)
            if self.barva(ii, jj) != 0:
                break
            ii += k
            jj += l
        if barva == 1:
            self.ne_premakni_2 = ne_premaknil
        else:
            self.ne_premakni_1 = ne_premaknil

    def vse_figure(self):
        figure = []
        sahovnica = self.sahovnica
        for i in range(8):
            for j in range(8):
                if sahovnica[i][j][0] == self.igralec:
                    figure.append((i, j))
        return figure

    def vsi_premiki(self):
        kralja = (self.kralj_1, self.kralj_2)
        ostalo = set()
        for polje in self.vse_figure():
            if polje in kralja:
                kralj = self.mozni_premiki(*polje, True)
            else:
                ostalo.update(self.mozni_premiki(*polje, True))
        return (kralj | ostalo, ostalo)

    def sah_polja(self, i, j):
        barva = self.barva(i, j)
        if barva == 1:
            k, l = self.kralj_2[0] - i, self.kralj_2[1] - j
        elif barva == 2:
            k, l = self.kralj_1[0] - i, self.kralj_1[1] - j
        g = max(abs(k), abs(l))
        k //= g
        l //= g
        return {(i + k * a, j + l * a) for a in range(g)}


    def preveri_sah(self, i, j):
        figura = self.figura(i, j)
        if figura in ["lovec", "trdnjava", "kraljica"]:
            sah = self.sah_polja(i, j)
        else:
            sah = {(i, j)}
        if self.igralec == 1 and sah & self.premiki_2[1] == set() and self.mozni_premiki(*self.kralj_2) == set():
            self.konec_igre()
        elif self.igralec == 2 and sah & self.premiki_1[1] == set() and self.mozni_premiki(*self.kralj_1) == set():
            self.konec_igre()
        else:
            self.stanje = 2
            self.sah = sah
            print(sah)

    def igraj(self, iz_i, iz_j, na_i, na_j):
        igralec = self.igralec
        if igralec == 1:
            self.ne_premakni_2 = {}
        else:
            self.ne_premakni_1 = {}
        self.premakni(iz_i, iz_j, na_i, na_j)
        premiki = self.mozni_premiki(na_i, na_j)
        vsi_premiki = self.vsi_premiki()
        if igralec == 1:
            self.premiki_1 = vsi_premiki
        elif igralec == 2:
            self.premiki_2 = vsi_premiki
        if self.kralj_1 in premiki or self.kralj_2 in premiki:
            self.preveri_sah(na_i, na_j)
        else:
            self.stanje = 1
            self.sah = set()
        igralec = 1 + igralec % 2
        self.igralec = igralec

    def konec_igre(self):
        self.stanje = 3
        print("Zmaga za", self.igralec)






treto = Igra()
treto.igraj(7, 5, 3, 1)
treto.mozni_premiki(1, 3)
treto.igraj(0, 0, 0, 0)
treto.igraj(0, 0, 0, 0)
treto.igraj(0, 4, 6, 1)
treto.igraj(7, 7, 7, 1)