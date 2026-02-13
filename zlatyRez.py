import math


class ZlatyRez:

    def __init__(self, funkce, a: int, b: int, eps=1e-5):
        self.f = funkce
        self.a = a
        self.b = b
        self.eps = eps
        self.konst = (math.sqrt(5) - 1)/2   #konstanta zlatého řezu

    def hledej_minimum(self):
        a, b = self.a, self.b

        x1 = b - self.konst * (b - a)
        x2 = a + self.konst * (b - a)

        f1 = self.f(x1)
        f2 = self.f(x2)

        while abs(b - a) > self.eps:
            if f1 < f2:
                b = x2
                x2 = x1
                f2 = f1
                x1 = b - self.konst * (b - a)
                f1 = self.f(x1)
            else:
                a = x1
                x1 = x2
                f1 = f2
                x2 = a + self.konst * (b - a)
                f2 = self.f(x2)

        return (a + b) / 2




def f1(x):
    return x**2 + 2*x + 1

def f2(x):
    return x**3 + 2*x**2 - x + 1

def f3(x):
    return math.sin(x)

def f4(x):
    return math.cos(x)

def f5(x):
    return math.exp(x)


funkce = [f1, f2, f3, f4, f5]
intervaly = [(-6, 3), (-3, 2), (-3, 0), (-2, 1), (-3, 5)]

for i, (f, (a, b)) in enumerate(zip(funkce, intervaly), start=1):
    zr = ZlatyRez(f, a, b, eps=1e-5)
    minimum = zr.hledej_minimum()
    print(f"Minimum funkce f{i} se nachází přibližně v bodě x = {minimum:.6f}")