class Quadrilateral:
    def __init__(self, a=0.0, b=0.0, c=0.0, d=0.0):
        """Quadrilateral figure initialization

        Args:
            a (float, optional): first size of the quadrilateral. Defaults to 0.
            b (float, optional): second size of the quadrilateral. Defaults to 0.
            c (float, optional): third size of the quadrilateral. Defaults to 0.
            d (float, optional): fourth size of the quadrilateral. Defaults to 0.
        """
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        

    def calc_perimeter(self):
        """Simply calculates the perimeter of the quadrilateral

        Returns:
            float: The perimeter of the quadrilateral
        """
        return self.a + self.b + self.c + self.d

    def resize_to_value(self, a=0.0, b=0.0, c=0.0, d=0.0):
        """This function resizes each side of the quadrilateral at some value

        Args:
            a (float, optional): Resizing 1st side at value. Defaults to 0.
            b (float, optional): Resizing 2nd side at value. Defaults to 0.
            c (float, optional): Resizing 3rd side at value. Defaults to 0.
            d (float, optional): Resizing 4th side at value. Defaults to 0.
        """
        self.a += a
        self.b += b
        self.c += c
        self.d += d

    def show_size(self):
        """Simply returns sizes of each side of the quadrilateral.
        This function returns nothing
        """
        print(
            f"1-ая сторона:{self.a}\n2-ая сторона:{self.b}\n3-ая сторона:{self.c}\n4-ая сторона:{self.d}\n",
            end="",
        )

    def what_am_i(self):
        """The way to know what type of quadrilateral we have"""
        print("Я - четырёхугольник!")

    def isExist(self):
        sides = [self.a, self.b, self.c, self.d]
        exists = True
        #Checking if sides equals zero or below zero
        if self.a < 0 or self.b < 0 or self.c < 0 or self.d < 0:
            exists = False
        for side in sides:
            subsum = sum(sides)
            subsum -= side
            if side > subsum:
                exists = False
        return exists


class Rectangle(Quadrilateral):
    def __init__(self, w=0, l=0):
        self.a = w
        self.b = l
        self.c = self.a
        self.d = self.b

    def resize_to_value(self, l=0, w=0):
        self.a += w
        self.b += l
        self.c += w
        self.d += l

    def what_am_i(self):
        print("Я - прямоугольник!")

    def area(self):
        return self.a * self.b


class Square(Rectangle):
    def __init__(self, l):
        self.a = l
        self.d = self.c = self.b = self.a

    def resize_to_value(self, l=0):
        self.a += l
        self.b += l
        self.c += l
        self.d += l

    def what_am_i(self):
        print("Я - квадрат!")


quadr1 = Quadrilateral(2, 3, 4, 5)
quadr1.what_am_i()
quadr1.show_size()
print(quadr1.calc_perimeter())
print()

rect1 = Rectangle(3, 4)
rect1.what_am_i()
rect1.show_size()
print(rect1.calc_perimeter())
print(rect1.area())
print()

sqr1 = Square(5)
sqr1.what_am_i()
sqr1.show_size()
print(sqr1.calc_perimeter())
print(sqr1.area())
print()
sqr1.resize_to_value(1)
sqr1.show_size()

quadr2 = Quadrilateral(2, 5, 5, 6)
quadr2.what_am_i()
quadr2.show_size()
print(f"Quadrilateral is {quadr2.isExist()} ")
