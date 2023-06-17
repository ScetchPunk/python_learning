class Shape:
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def print_size(self):
        print(
            """{} на {}
            """.format(
                self.width, self.len
            )
        )


class Rectangle(Shape):
    def area(self):
        return self.width * self.len

my_shape = Shape(20, 25)
my_shape.print_size()

a_rectangle=Rectangle(20,20)
