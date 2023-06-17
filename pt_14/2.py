class Rectangle:
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def print_size(self):
        print(f"{self.width} на {self.len}")

my_rectangle = Rectangle(10,24)
my_rectangle.print_size()
