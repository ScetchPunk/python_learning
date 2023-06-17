class Square:
    square_list = []

    def __init__(self, l):
        self.len = l
        self.square_list.append(self)

    def __repr__(self):
        return f"Квадрат со сторонами: {self.len} на {self.len} на {self.len} на {self.len}"


sqr1 = Square(2)
sqr2 = Square(3)
sqr3 = Square(4)
print(sqr3)
print(Square.square_list)
