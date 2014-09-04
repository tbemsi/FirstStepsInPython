__author__ = 'bemsibom'

import turtle
from math import *


def dim_checker(**kwargs):
    errmsg = "All given arguments must be positive numbers; provided :"\
             + \
             str({k: v for k, v in kwargs.items() if v is not None})
    for name, arg in kwargs.items():
        if arg is None:
            pass # ignore nones, only checking provided arguments here
        elif not isinstance(arg, (int, float)):
            raise TypeError(errmsg)
        elif not arg >= 0:
            raise ValueError(errmsg)


class Shape(object):
    shapes_created = 0

    def __init__(self, **kwargs):
        dim_checker(**kwargs)
        self.shapes_created += 1

    def __str__(self):
        return self.__class__.__name__ +\
               "; area : "+str(self.area)+\
               "; perimeter: "+str(self.perimeter)


class Square(Shape):
    """a class representation of square"""
    squares_created = 0

    def __init__(self, side_length: (int, float)):
        super(Square, self).__init__(side_length=side_length)
        self.squares_created += 1
        self.side_length = side_length
        self.area = self.side_length**2
        self.perimeter = self.side_length*4

    def __str__(self):
        return super(Square, self).__str__()+\
               "; side length: "+str(self.side_length)

    def __cmp__(self, other):
        if not isinstance(other, Square):
            raise TypeError
        else:
            return self.side_length - other.side_length

    def draw(self):
        for i in range(0,4):
            turtle.forward(self.side_length)
            turtle.left(90)
        turtle.done()


if __name__ == "__main__":
    sq = Square(50)
    print(sq)
    sq.draw()

    try:
        sq2 = Square("a string")
    except TypeError as err:
        print(err.args[0], sq.shapes_created, sq.squares_created)


class Rhombus(Shape):
    """a class representation of square"""
    rhombi_created = 0

    def __init__(self, side_length: (int, float)):
        super(Rhombus, self).__init__(side_length=side_length)
        self.rhombi_created += 1
        self.side_length = side_length
        self.area = self.side_length**2
        self.perimeter = self.side_length*4

    def __str__(self):
        return super(Rhombus, self).__str__()+\
               "; side length: "+str(self.side_length)

    def __cmp__(self, other):
        if not isinstance(other, Rhombus):
            raise TypeError
        else:
            return self.side_length - other.side_length

    def draw(self):
        turtle.left(45)
        turtle.forward(self.side_length)
        turtle.left(90)
        turtle.forward(self.side_length)
        turtle.left(90)
        turtle.forward(self.side_length)
        turtle.left(90)
        turtle.forward(self.side_length)
        turtle.done()


if __name__ == "__main__":
    Rh = Rhombus(50)
    print(Rh)
    Rh.draw()

    try:
        sq2 = Square("a string")
    except TypeError as err:
        print(err.args[0], sq.shapes_created, sq.squares_created)


class Parallelogram(Shape):
    """a class representation of a parallelogram"""
    parallelograms_created = 0

    def __init__(self, base_length: (int, float), side_length: (int, float)):
        super(Parallelogram, self).__init__(base_length=base_length, side_length=side_length)
        self.parallelograms_created += 1
        self.side_length = side_length
        self.base_length = base_length
        self.area = self.side_length * self.base_length
        self.perimeter = (self.side_length + self.base_length) * 2

    def __str__(self):
        return super(Parallelogram, self).__str__()+\
               "; side length: "+str(self.side_length)
               "; base_length: "+str(self.base_length)

    def __cmp__(self, other):
        if not isinstance(other, Parallelogram):
            raise TypeError
        else:
            return self.base_length - other.side_length

    def draw(self):
        turtle.left(45)
        turtle.forward(self.side_length)
        turtle.left(90)
        turtle.forward(self.side_length)
        turtle.left(90)
        turtle.forward(self.side_length)
        turtle.left(90)
        turtle.forward(self.side_length)
        turtle.done()


if __name__ == "__main__":
    Rh = Rhombus(50)
    print(Rh)
    Rh.draw()

    try:
        sq2 = Rhombus("a string")
    except TypeError as err:
        print(err.args[0], sq.shapes_created, sq.squares_created)



class Circle(Shape):
    """a class representation of a circle"""
    circles_created = 0

    def __init__(self, radius: (int, float)):
        super(Circle, self).__init__(radius=radius)
        self.circles_created += 1
        self.radius = radius
        self.area = self.radius**2 * pi
        self.perimeter = self.radius * 2 * pi

    def __str__(self):
        return super(Circle, self).__str__()+\
               "; radius: "+str(self.radius)

    def __cmp__(self, other):
        if not isinstance(other, Circle):
            raise TypeError
        else:
            return self.radius - other.radius

    def draw(self):
        turtle.circle(self.radius)
        turtle.done()


if __name__ == "__main__":
    cir = Circle(50)
    print(sq)
    cir.draw()

    try:
        sq2 = Circle("a string")
    except TypeError as err:
        print(err.args[0], sq.shapes_created, sq.squares_created)
