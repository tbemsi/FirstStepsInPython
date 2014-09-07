__author__ = 'bemsibom'

import turtle
from math import *
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np


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
            ": area : "+str(self.area) + \
            ": perimeter: "+str(self.perimeter)


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
        return super(Square, self).__str__() +\
            ": side length: "+str(self.side_length)

    def __cmp__(self, other):
        if not isinstance(other, Square):
            raise TypeError
        else:
            return self.side_length - other.side_length

    def draw(self):
        for i in range(0, 4):
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
        return super(Rhombus, self).__str__() + \
            ": side length: "+str(self.side_length)

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
        print(err.args[0], sq.shapes_created, Rh.rhombi_created)


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
        return super(Parallelogram, self).__str__() + \
            ": side length: "+str(self.side_length) + "base_length: "+str(self.base_length)

    def __cmp__(self, other):
        if not isinstance(other, Parallelogram):
            raise TypeError
        else:
            return self.base_length - other.side_length

    def draw(self):
        turtle.forward(self.base_length)
        turtle.left(45)
        turtle.forward(self.side_length)
        turtle.left(135)
        turtle.forward(self.base_length)
        turtle.left(45)
        turtle.forward(self.side_length)
        turtle.done()


if __name__ == "__main__":
    para = Parallelogram(50, 75)
    print()
    para.draw()

    try:
        sq2 = Rhombus("a string")
    except TypeError as err:
        print(err.args[0], sq.shapes_created, para.parallelograms_created)


class Octagon(Shape):
    """a class representation of an octagon"""
    octagons_created = 0

    def __init__(self, side: (int, float)):
        super(Octagon, self).__init__(side=side)
        self.octagons_created += 1
        self.side = side
        self.area = self.side**2 * 2 * (1+sqrt(2))
        self.perimeter = self.side * 8

    def __str__(self):
        return super(Octagon, self).__str__() + \
            ": side: "+str(self.side)

    def __cmp__(self, other):
        if not isinstance(other, Octagon):
            raise TypeError
        else:
            return self.side - other.side

    def draw(self):
        for i in range(8):
            turtle.forward(self.side)
            turtle.left(45)
        turtle.done()

if __name__ == "__main__":
    Oct = Octagon(50)
    print(sq)
    Oct.draw()

    try:
        Oct1 = Octagon("a string")
    except TypeError as err:
        print(err.args[0], Oct.shapes_created, Oct.octagons_created)


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
        return super(Circle, self).__str__() + \
            ": radius: "+str(self.radius)

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
    print(cir)
    cir.draw()

    try:
        cir2 = Circle("a string")
    except TypeError as err:
        print(err.args[0], cir.shapes_created, cir.circles_created)


class Sector(Shape):
    """a class representation of a circle sector"""
    sectors_created = 0

    def __init__(self, radius: (int, float), angle: (int, float)):
        super(Sector, self).__init__(radius=radius, angle=angle)
        self.sectors_created += 1
        self.radius = radius
        self.angle = angle
        self.area = self.radius**2 * angle/360 * pi
        self.perimeter = self.radius * 2 + self.angle * self.angle * 2 * pi/360

    def __str__(self):
        return super(Sector, self).__str__() + \
            ": radius: "+str(self.radius) + \
            ": angle: "+str(self.angle)

    def __cmp__(self, other):
        if not isinstance(other, Sector):
            raise TypeError
        else:
            return self.radius - other.radius

    def draw(self):
        turtle.forward(self.radius)
        turtle.left(90)
        turtle.circle(self.radius, extent=self.angle)
        turtle.left(90)
        turtle.forward(self.radius)
        turtle.done()


if __name__ == "__main__":
    sec = Sector(50, 90)
    print(sec)
    sec.draw()

    try:
        sec1 = Sector("a string")
    except TypeError as err:
        print(err.args[0], sec.shapes_created, sec.sectors_created)


class Solid(object):
    solids_created = 0

    def __init__(self, **kwargs):
        dim_checker(**kwargs)
        self.solids_created += 1

    def __str__(self):
        return self.__class__.__name__ +\
            ": surface_area : "+str(self.surface_area) + \
            ": volume: "+str(self.volume)


class Prism(Solid):
    """a class representation of a triangular prism"""
    prisms_created = 0

    def __init__(self, base: (int, float), height: (int, float), length: (int, float)):
        super(Prism, self).__init__(base=base, height=height, length=length)
        self.prisms_created += 1
        self.base = base
        self.height = height
        self.length = length
        self.surface_area = self.base * self.height + 2 * self.length * self.height + self.length * self.base
        self.volume = self.base * self.height * self.length * 0.5

    def __str__(self):
        return super(Prism, self).__str__() + \
            ": base: "+str(self.base) + \
            ": height: "+str(self.height) + \
            ": length: "+str(self.length)

    def __cmp__(self, other):
        if not isinstance(other, Prism):
            raise TypeError
        else:
            return self.base - other.base  # ----------------------------------check this!!!---------------------

    def draw(self):
        fig = plt.figure()
        ax = Axes3D(fig)

        # Face 1
        x1 = np.array([[0, 0, 1, 1, 0],
                       [0, 0, 0, 0, 0]])
        y1 = np.array([[0, 1, 1, 0, 0],
                       [0, 0, 0, 0, 0]])
        z1 = np.array([[0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0]])

        # Face 2
        x2 = np.array([[0, 0, 0.5, 0],
                       [0, 0, 0, 0]])
        y2 = np.array([[0, 1, 0.5, 0],
                       [0, 0, 0, 0]])
        z2 = np.array([[0, 0, 1, 0],
                       [0, 0, 0, 0]])
        # Face 3
        x3 = np.array([[1, 1, 0.5, 1],
                       [1, 1, 1, 1]])
        y3 = np.array([[0, 1, 0.5, 0],
                       [0, 0, 0, 0]])
        z3 = np.array([[0, 0, 1, 0],
                       [0, 0, 0, 0]])
        # Face 4
        x4 = np.array([[0, 1, 0.5, 0],
                       [0, 0, 0, 0]])
        y4 = np.array([[1, 1, 0.5, 1],
                       [1, 1, 1, 1]])
        z4 = np.array([[0, 0, 1, 0],
                       [0, 0, 0, 0]])
        # Face 5
        x5 = np.array([[1, 0, 0.5, 1],
                       [1, 1, 1, 1]])
        y5 = np.array([[0, 0, 0.5, 0],
                       [0, 0, 0, 0]])
        z5 = np.array([[0, 0, 1, 0],
                       [0, 0, 0, 0]])

        ax.plot_surface(x1, y1, z1)
        ax.plot_surface(x2, y2, z2)
        ax.plot_surface(x3, y3, z3)
        ax.plot_surface(x4, y4, z4)
        ax.plot_surface(x5, y5, z5)

        plt.show()

if __name__ == "__main__":
    pr = Prism(50, 100, 50)
    print(pr)
    pr.draw()

    try:
        pr1 = Prism("a string")
    except TypeError as err:
        print(err.args[0], pr.solids_created, pr.prisms_created)


class Pyramid(Solid):
    """a class representation of a pyramid"""
    pyramids_created = 0

    def __init__(self, base: (int, float), height: (int, float)):
        super(Pyramid, self).__init__(base=base, height=height)
        self.pyramids_created += 1
        self.base = base
        self.height = height
        self.surface_area = 2 * self.base * self.height + self.base**2
        self.volume = self.base**2 * self.height/3

    def __str__(self):
        return super(Pyramid, self).__str__() + \
            ": base: "+str(self.base) + \
            ": height: "+str(self.height)

    def __cmp__(self, other):
        if not isinstance(other, Pyramid):
            raise TypeError
        else:
            return self.base - other.base  # ----------------------------------check this!!!---------------------

    def draw(self):
        fig = plt.figure()
        ax = Axes3D(fig)

        # Face 1
        x1 = np.array([[0, 0, 1, 1, 0],
                       [0, 0, 0, 0, 0]])
        y1 = np.array([[0, 1, 1, 0, 0],
                       [0, 0, 0, 0, 0]])
        z1 = np.array([[0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0]])

        # Face 2
        x2 = np.array([[0, 0, 0.5, 0],
                       [0, 0, 0, 0]])
        y2 = np.array([[0, 1, 0.5, 0],
                       [0, 0, 0, 0]])
        z2 = np.array([[0, 0, 1, 0],
                       [0, 0, 0, 0]])
        # Face 3
        x3 = np.array([[1, 1, 0.5, 1],
                       [1, 1, 1, 1]])
        y3 = np.array([[0, 1, 0.5, 0],
                       [0, 0, 0, 0]])
        z3 = np.array([[0, 0, 1, 0],
                       [0, 0, 0, 0]])
        # Face 4
        x4 = np.array([[0, 1, 0.5, 0],
                       [0, 0, 0, 0]])
        y4 = np.array([[1, 1, 0.5, 1],
                       [1, 1, 1, 1]])
        z4 = np.array([[0, 0, 1, 0],
                       [0, 0, 0, 0]])
        # Face 5
        x5 = np.array([[1, 0, 0.5, 1],
                       [1, 1, 1, 1]])
        y5 = np.array([[0, 0, 0.5, 0],
                       [0, 0, 0, 0]])
        z5 = np.array([[0, 0, 1, 0],
                       [0, 0, 0, 0]])

        ax.plot_surface(x1, y1, z1)
        ax.plot_surface(x2, y2, z2)
        ax.plot_surface(x3, y3, z3)
        ax.plot_surface(x4, y4, z4)
        ax.plot_surface(x5, y5, z5)

        plt.show()

if __name__ == "__main__":
    py = Pyramid(50, 50)
    print(py)
    py.draw()

    try:
        py1 = Pyramid("a string")
    except TypeError as err:
        print(err.args[0], py.solids_created, py.pyramids_created)


class Cylinder(Solid):
    """a class representation of a cylinder"""
    cylinders_created = 0

    def __init__(self, radius: (int, float), height: (int, float)):
        super(Cylinder, self).__init__(radius=radius, height=height)
        self.cylinders_created += 1
        self.radius = radius
        self.height = height
        self.surface_area = 2 * pi * (self.radius**2 + self.radius * self.height)
        self.volume = pi * self.radius**2 * self.height

    def __str__(self):
        return super(Cylinder, self).__str__() + \
            ": radius: "+str(self.radius) + \
            ": height: "+str(self.height)

    def __cmp__(self, other):
        if not isinstance(other, Cylinder):
            raise TypeError
        else:
            return self.base - other.base  # ----------------------------------check this!!!---------------------

    def draw(self):
        fig = plt.figure()
        ax = Axes3D(fig)

        x = np.linspace(-1, 1, 40)
        z = np.linspace(0, self.height, 40)

        X, Z = np.meshgrid(x, z)
        Y = np.sqrt(1-X**2)

        ax.plot_wireframe(X, Y, Z)
        ax.plot_wireframe(X, -Y, Z)

        ax.set_xlabel('x-axis')
        ax.set_ylabel('y-axis')
        ax.set_zlabel('z-axis')

        plt.show()

if __name__ == "__main__":
    cy = Cylinder(50, 50)
    print(cy)
    cy.draw()

    try:
        cy1 = Cylinder("a string")
    except TypeError as err:
        print(err.args[0], cy.solids_created, cy.cylinders_created)


class Cone(Solid):
    """a class representation of a cone"""
    cones_created = 0

    def __init__(self, radius: (int, float), height: (int, float)):
        super(Cone, self).__init__(radius=radius, height=height)
        self.cones_created += 1
        self.radius = radius
        self.height = height
        self.surface_area = pi * (self.radius*self.height + self.radius**2)
        self.volume = pi * self.radius**2 * self.height/3

    def __str__(self):
        return super(Cone, self).__str__() + \
            ": radius: "+str(self.radius) + \
            ": height: "+str(self.height)

    def __cmp__(self, other):
        if not isinstance(other, Cone):
            raise TypeError
        else:
            return self.base - other.base  # ----------------------------------check this!!!---------------------

    #def draw(self):  #---------------------------------research on how to plot cone in 3d!!!-------------------


if __name__ == "__main__":
    co = Cone(50, 50)
    print(co)
    # co.draw()

    try:
        co1 = Cone("a string")
    except TypeError as err:
        print(err.args[0], co.solids_created, co.cones_created)
