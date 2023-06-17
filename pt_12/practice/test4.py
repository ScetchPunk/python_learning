class Hexagon:
    def __init__(self, a, b, c, d, e, f):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f

    def calculate_perimeter(self):
        return self.a + self.b + self.c + self.d + self.e + self.f


hex1 = Hexagon(3, 4, 5, 6, 7, 8)
print(hex1.calculate_perimeter())
