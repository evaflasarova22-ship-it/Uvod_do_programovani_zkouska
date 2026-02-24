import random
import turtle

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



def vykresli_turtle(bludiste, cesta=None, velikost=20):
    screen = turtle.Screen()
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    turtle.tracer(0, 0)

    x_size = len(bludiste.mapa)
    y_size = len(bludiste.mapa[0])

    #posun, aby bylo bludiště uprostřed
    offset_x = - (y_size * velikost) / 2
    offset_y = (x_size * velikost) / 2

    #zdi
    for x in range(x_size):
        for y in range(y_size):
            policko = bludiste.mapa[x][y]

            start_x = offset_x + y * velikost
            start_y = offset_y - x * velikost

            if policko.zdi["nahoru"] != 0:
                t.penup()
                t.goto(start_x, start_y)
                t.pendown()
                t.goto(start_x + velikost, start_y)

            if policko.zdi["dolu"] != 0:
                t.penup()
                t.goto(start_x, start_y - velikost)
                t.pendown()
                t.goto(start_x + velikost, start_y - velikost)

            if policko.zdi["doleva"] != 0:
                t.penup()
                t.goto(start_x, start_y)
                t.pendown()
                t.goto(start_x, start_y - velikost)

            if policko.zdi["doprava"] != 0:
                t.penup()
                t.goto(start_x + velikost, start_y)
                t.pendown()
                t.goto(start_x + velikost, start_y - velikost)

    #cesta
    if cesta:
        t.penup()
        t.color("red")
        t.width(3)

        for i, (radek, sloupec) in enumerate(cesta):
            stred_x = offset_x + sloupec * velikost + velikost / 2
            stred_y = offset_y - radek * velikost - velikost / 2

            if i == 0:
                t.goto(stred_x, stred_y)
                t.pendown()
            else:
                t.goto(stred_x, stred_y)
                t.pendown()

    turtle.update()
    turtle.done()



bludiste = Bludiste(20, 20)
cesta = bludiste.bfs(0, 0)
vykresli_turtle(bludiste, cesta)