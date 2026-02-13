import random

class Policko:
    def __init__(self, x, y, x_size=50, y_size=50):
        self.souradnice = (x, y)
        self.zdi = {"nahoru": 1, "doleva": 1, "dolu": 1, "doprava": 1}
        if x == 0:
            self.zdi["nahoru"] = 2
        if y == 0:
            self.zdi["doleva"] = 2
        if x == x_size - 1:
            self.zdi["dolu"] = 2
        if y == y_size - 1:
            self.zdi["doprava"] = 2
        self.navstiveno = None

class Bludiste:
    def __init__(self, x_size=50, y_size=50):
        self.mapa = [[Policko(x, y, x_size, y_size) for y in range(y_size)] for x in range(x_size)]
        self.gen_bludiste(0, 0)

    def gen_bludiste(self, x, y):
        policko = self.mapa[x][y]
        zdi = []
        for pozice, zed in policko.zdi.items():
            if zed == 1:
                zdi.append(pozice)
        if zdi == []:
            self.end = (x, y)
            return
        zborit = random.choice(zdi)
        if zborit == "nahoru":
            policko.zdi["nahoru"] = 0
            self.mapa[x - 1][y].zdi["dolu"] = 0
            self.gen_bludiste(x-1, y)

        if zborit == "dolu":
            policko.zdi["dolu"] = 0
            self.mapa[x + 1][y].zdi["nahoru"] = 0
            self.gen_bludiste(x+1, y)

        if zborit == "doleva":
            policko.zdi["doleva"] = 0
            self.mapa[x][y - 1].zdi["doprava"] = 0
            self.gen_bludiste(x, y-1)

        if zborit == "doprava":
            policko.zdi["doprava"] = 0
            self.mapa[x][y + 1].zdi["doleva"] = 0
            self.gen_bludiste(x, y+1)

    def bfs(self, x, y):
        policko = self.mapa[x][y]
        policko.navstiveno = [(x, y)]

        fronta = [policko]
        while len(fronta) > 0:
            policko = fronta.pop(0)
            x, y = policko.souradnice
            if (x, y) == self.end:
                return policko.navstiveno

            if policko.zdi["dolu"] == 0 and self.mapa[x+1][y].navstiveno is None:
                self.mapa[x+1][y].navstiveno = policko.navstiveno + [(x+1, y)]
                fronta.append(self.mapa[x+1][y])

            if policko.zdi["nahoru"] == 0 and self.mapa[x-1][y].navstiveno is None:
                self.mapa[x-1][y].navstiveno = policko.navstiveno + [(x-1, y)]
                fronta.append(self.mapa[x-1][y])

            if policko.zdi["doprava"] == 0 and self.mapa[x][y+1].navstiveno is None:
                self.mapa[x][y+1].navstiveno = policko.navstiveno + [(x, y+1)]
                fronta.append(self.mapa[x][y+1])

            if policko.zdi["doleva"] == 0 and self.mapa[x][y-1].navstiveno is None:
                self.mapa[x][y-1].navstiveno = policko.navstiveno + [(x, y-1)]
                fronta.append(self.mapa[x][y-1])


bludiste = Bludiste()
print(bludiste.end)
print(bludiste.bfs(0, 0))