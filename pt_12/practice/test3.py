import math


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        halfperim = (self.a + self.b + self.c) / 2
        return math.sqrt(
            halfperim
            * (halfperim - self.a)
            * (halfperim - self.b)
            * (halfperim - self.c)
        )

    def show(self):
        print(
            f"Стороны треугольника:\n1-ая сторона:{self.a}\n2-ая сторона:{self.b}\n3-ая сторона:{self.c}"
        )


tr1 = Triangle(3, 4, 5)
tr1.show()
print(tr1.area())
