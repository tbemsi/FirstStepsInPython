__author__ = 'bemsibom'

from numbers import Number
from math import *
from input_validation import *


def rhombus_perimeter(side: Number) -> Number:
    """
    Calculate perimeter of a rhombus from side length.
    :param side: the side length
    :return: the perimeter (same units as side length)

    >>> rhombus_perimeter(4)
    16

    """
    if dim_validate_argument(side):
        if dim_validate_number(side):
            if dim_validate_positive(side):
                return 4*side
            else:
                raise ValueError("All dimensions must be positive: "+str(side))
        else:
            raise TypeError("Only numerical values allowed for dimensions: "+str(side))
    else:
        raise AttributeError("Argumentation incomplete. Please input all dimensions")

if __name__ == "__main__":
    sampleSide = 4
    print("Perimeter of rhombus:",
          rhombus_perimeter(sampleSide))


def rhombus_area_bh(base: Number, height: Number) -> Number:
    """
    Calculate area of a rhombus from base and height
    :param base: the base of the rhombus
    :param height: the height of the rhombus
    :return: the area of the rhombus
    >>> rhombus_area_bh(4,6)
    24
    """

    if dim_validate_argument(base) and dim_validate_argument(height):
        if dim_validate_number(base) and dim_validate_number(height):
            if dim_validate_positive(base) and dim_validate_positive(height):
                return base*height
            else:
                raise ValueError("All dimensions must be positive: "+str(base)+str(" ")+str(height))
        else:
            raise TypeError("Only numerical values accepted for dimensions: "+str(base)+str(" ")+str(height))
    else:
        raise AttributeError("Argumentation incomplete. Please input all dimensions")


if __name__ == "__main__":
    samplebase = 4
    sampleheight = 7
    print("Area: of rhombus",
          rhombus_area_bh(samplebase, sampleheight))


def rhombus_area_dd(diagonal1: Number, diagonal2: Number) -> Number:
    """
    Calculates the area of a rhombus from two diagonals
    :param diagonal1: The length of the first diagonal
    :param diagonal2: The length of the second diagonal
    :return: The are of the rhombus
    >>> rhombus_area_dd(4, 6)
    12.0
    """

    if dim_validate_argument(diagonal1) and dim_validate_argument(diagonal2):
        if dim_validate_number(diagonal1) and dim_validate_number(diagonal2):
            if dim_validate_positive(diagonal1) and dim_validate_positive(diagonal2):
                return (diagonal1*diagonal2)/2
            else:
                raise ValueError("All dimensions must be positive: "+str(diagonal1)+str(" ")+str(diagonal2))
        else:
            raise TypeError("Only numerical values accepted for dimensions: "+str(diagonal1)+str(" ")+str(diagonal2))
    else:
        raise AttributeError("Argumentation incomplete. Please input all dimensions")

if __name__ == "__main__":
    sample_diagonal1 = 4
    sample_diagonal2 = 6
    print("Area of rhombus:",
          rhombus_area_dd(sample_diagonal1, sample_diagonal2))


def rhombus_area_sin(side: Number, angle: Number) -> Number:
    """
    Calculates the area of a rhombus from the length of a side and the size of any angle
    :param side: The length of a side
    :param angle: The size of the angle
    :return: The area of the rhombus
    >>> rhombus_area_sin(4, pi/2)
    16.0
    """

    if dim_validate_argument(side) and dim_validate_argument(angle):
        if dim_validate_number(side) and dim_validate_number(angle):
            if dim_validate_positive(side) and dim_validate_positive(angle):
                return side**2*sin(angle)
            else:
                raise ValueError("All dimensions must be positive: "+str(side)+str(" ")+str(angle))
        else:
            raise TypeError("Only numerical values accepted for dimensions: "+str(side)+str(" ")+str(angle))
    else:
        raise AttributeError("Argumentation incomplete. Please input all dimensions")

if __name__ == "__main__":
    sampleSide = 4
    sampleAngle = pi/2
    print("Area of rhombus:",
          rhombus_area_sin(sampleSide, sampleAngle))


def parallelogram_perimeter(base_length: Number, side_length: Number) -> Number:
    """
    Calculates the perimeter of a parallelogram
    :param base_length: the base length of the parallelogram
    :param side_length: the side length of the parallelogram
    :return:The perimeter of the parallelogram
    >>> parallelogram_perimeter(2, 2)
    8
    """

    if dim_validate_argument(base_length) and dim_validate_argument(side_length):
        if dim_validate_number(base_length) and dim_validate_number(side_length):
            if dim_validate_positive(base_length) and dim_validate_positive(side_length):
                return 2*(base_length + side_length)
            else:
                raise ValueError("All dimensions must be positive: "+str(base_length)+str(" ")+str(side_length))
        else:
            raise TypeError("Only numerical values accepted for dimensions: "+str(base_length)+str(" ")+str(side_length))
    else:
        raise AttributeError("Argumentation incomplete. Please input all dimensions")

if __name__ == "__main__":
    sample_base_length = 2
    sample_side_length = 2
    print("Perimeter of parallelogram:",
          parallelogram_perimeter(sample_base_length, sample_side_length))


def area_regular_polygon_sd(n: Number, s: Number) -> Number:
    """
    Calculates the area of any rectangular polygon, given the number of sides and the length of a side
    :param n: Number of sides in the polygon
    :param s: length of a side in the polygon
    :return:The area of the polygon
    >>> area_regular_polygon_sd(10, 2)
    30.776835371752536
    """

    if dim_validate_argument(n) and dim_validate_argument(s):
        if dim_validate_number(n) and dim_validate_number(s):
            if dim_validate_positive(n) and dim_validate_positive(s):
                return s**2*n/(4*tan(radians(180/n)))
            else:
                raise ValueError("All dimensions must be positive: "+str(n)+str(" ")+str(s))
        else:
            raise TypeError("Only numerical values accepted for dimensions: "+str(n)+str(" ")+str(s))
    else:
        raise AttributeError("Argumentation incomplete. Please input all dimensions")

if __name__ == "__main__":
    sample_n = 10
    sample_s = 2
    print("Area of regular polygon:",
          area_regular_polygon_sd(sample_n, sample_s))


def area_regular_polygon_rad(radius: Number, n: Number) -> Number:
    """
    Calculates the area of any regular polygon given the circumradius and the number of sides
    :param radius: the circumradius (perpendicular distance from the center to any side)
    :param n: number of sides
    :return: the are of the polygon
    >>> area_regular_polygon_rad(5, 10)
    73.47315653655915
    """

    if dim_validate_argument(radius) and dim_validate_argument(n):
        if dim_validate_number(radius) and dim_validate_number(n):
            if dim_validate_positive(radius) and dim_validate_positive(n):
                return (radius**2*n*sin(radians(360/n)))/2
            else:
                raise ValueError("All dimensions must be positive: "+str(radius)+str(" ")+str(n))
        else:
            raise TypeError("Only numerical values accepted for dimensions: "+str(radius)+str(" ")+str(n))
    else:
        raise AttributeError("Argumentation incomplete. Please input all dimensions")

if __name__ == "__main__":
    sample_radius = 5
    sample_n = 10
    print("Area of regular polygon:",
          area_regular_polygon_rad(sample_radius, sample_n))


def area_regular_polygon_apotheon(apoth: Number, n: Number) -> Number:
    """
    Calculates the area of any regular polygon given the apotheon and the number of sides
    :param apoth: the apotheon of the polygon
    :param n: the number of sides the polygon has
    :return:the area of the polygon
    >>> area_regular_polygon_apotheon(5, 10)
    81.22992405822657
    """

    if dim_validate_argument(apoth) and dim_validate_argument(n):
        if dim_validate_number(apoth) and dim_validate_number(n):
            if dim_validate_positive(apoth) and dim_validate_positive(n):
                return apoth**2*n*tan(radians(180/n))
            else:
                raise ValueError("All dimensions must be positive: "+str(apoth)+str(" ")+str(n))
        else:
            raise TypeError("Only numerical values accepted for dimensions: "+str(apoth)+str(" ")+str(n))
    else:
        raise AttributeError("Argumentation incomplete. Please input all dimensions")

if __name__ == "__main__":
    sample_apoth = 5
    sample_n = 10
    print("Area of regular polygon: ",
          area_regular_polygon_apotheon(sample_apoth, sample_n))


def area_circle(radius: Number) -> Number:
    """
    Calculates the area of a circle
    :param radius: the radius of the circle
    :return:The area of the circle
    >>> area_circle(5)
    78.53981633974483
    """

    if dim_validate_argument(radius):
        if dim_validate_number(radius):
            if dim_validate_positive(radius):
                return pi*radius**2
            else:
                raise ValueError("All dimensions must be positive: "+str(radius))
        else:
            raise TypeError("Only numerical values allowed for dimensions: "+str(radius))
    else:
        raise AttributeError("Argumentation incomplete. Please input all dimensions")

if __name__ == "__main__":
    sample_radius = 5
    print("Area of circle: ",
          area_circle(sample_radius))


def perimeter_circle(radius: Number) -> Number:
    """
    Calculates the perimeter of a circle
    :param radius: the radius of the circle
    :return: The perimeter of the circle
    >>> perimeter_circle(5)
    31.41592653589793
    """

    if dim_validate_argument(radius):
        if dim_validate_number(radius):
            if dim_validate_positive(radius):
                return 2 * pi * radius
            else:
                raise ValueError("All dimensions must be positive: "+str(radius))
        else:
            raise TypeError("Only numerical values allowed for dimensions: "+str(radius))
    else:
        raise AttributeError("Argumentation incomplete. Please input all dimensions")

if __name__ == "__main__":
    sample_radius = 5
    print("Perimeter of circle: ",
          perimeter_circle(sample_radius))


def surface_area_cone(radius: Number, side_length: Number) -> Number:
    """
    Calculates the surface area of a cone
    :param radius: base radius
    :param side_length: length of the side
    :return: Surface area of the cone
    >>> surface_area_cone(5,5)
    157.07963267948966
    """

    if dim_validate_argument(radius) and dim_validate_argument(side_length):
        if dim_validate_number(radius) and dim_validate_number(side_length):
            if dim_validate_positive(radius) and dim_validate_positive(side_length):
                return pi*(radius*side_length + radius**2)
            else:
                raise ValueError("All dimensions must be positive: "+str(radius)+str(" ")+str(side_length))
        else:
            raise TypeError("Only numerical values accepted for dimensions: "+str(radius)+str(" ")+str(side_length))
    else:
        raise AttributeError("Argumentation incomplete. Please input all dimensions")



if __name__ == "__main__":
    sample_radius = 5
    sample_side_length = 5
    print("Surface Area of cone:",
          surface_area_cone(sample_radius, sample_side_length))


def volume_cone(radius: Number, height: Number) -> Number:
    """
    Calculates the volume of a cone
    :param radius: base radius of the cone
    :param height: height of cone
    :return:Volume of the cone
    >>> volume_cone(2,5)
    20.943951023931955
    """

    if dim_validate_argument(radius) and dim_validate_argument(height):
        if dim_validate_number(radius) and dim_validate_number(height):
            if dim_validate_positive(radius) and dim_validate_positive(height):
                return pi*radius**2*height/3
            else:
                raise ValueError("All dimensions must be positive: "+str(radius)+str(" ")+str(height))
        else:
            raise TypeError("Only numerical values accepted for dimensions: "+str(radius)+str(" ")+str(height))
    else:
        raise AttributeError("Argumentation incomplete. Please input all dimensions")

if __name__ == "__main__":
    sample_radius = 2
    sample_height = 5
    print("Volume of cone:",
          volume_cone(sample_radius, sample_height))


def surface_area_cylinder(radius: Number, height: Number) -> Number:
    """
    Calculates the surface area of a cylinder
    :param radius: radius of cylinder
    :param height: height of cylinder
    :return:Surface area of the cylinder
    >>> surface_area_cylinder(2, 5)
    87.96459430051421
    """

    if dim_validate_argument(radius) and dim_validate_argument(height):
        if dim_validate_number(radius) and dim_validate_number(height):
            if dim_validate_positive(radius) and dim_validate_positive(height):
                return 2*pi*(radius**2 + radius*height)
            else:
                raise ValueError("All dimensions must be positive: "+str(radius)+str(" ")+str(height))
        else:
            raise TypeError("Only numerical values accepted for dimensions: "+str(radius)+str(" ")+str(height))
    else:
        raise AttributeError("Argumentation incomplete. Please input all dimensions")

if __name__ == "__main__":
    sample_radius = 2
    sample_height = 5
    print("Surface Area of cylinder:",
          surface_area_cylinder(sample_radius, sample_height))


def volume_cylinder(radius: Number, height: Number) -> Number:
    """
    Calculates the volume of a cylinder
    :param radius: radius of the cylinder
    :param height: height of cylinder
    :return:Area of cylinder
    >>> volume_cylinder(2, 5)
    62.83185307179586
    """

    if dim_validate_argument(radius) and dim_validate_argument(height):
        if dim_validate_number(radius) and dim_validate_number(height):
            if dim_validate_positive(radius) and dim_validate_positive(height):
                return pi*radius**2*height
            else:
                raise ValueError("All dimensions must be positive: "+str(radius)+str(" ")+str(height))
        else:
            raise TypeError("Only numerical values accepted for dimensions: "+str(radius)+str(" ")+str(height))
    else:
        raise AttributeError("Argumentation incomplete. Please input all dimensions")

if __name__ == "__main__":
    sample_radius = 2
    sample_height = 5
    print("Volume of cylinder: ",
          volume_cylinder(sample_radius, sample_height))


def surface_area_pyramid(base: Number, height: Number) -> Number:
    """
    Calculates the surface area of a square-based pyramid
    :param base: side of base
    :param height: height of pyramid
    :return:Surface area of pyramid
    >>> surface_area_pyramid(2,2)
    12
    """

    if dim_validate_argument(base) and dim_validate_argument(height):
        if dim_validate_number(base) and dim_validate_number(height):
            if dim_validate_positive(base) and dim_validate_positive(height):
                return 2*base*height + base**2
            else:
                raise ValueError("All dimensions must be positive: "+str(base)+str(" ")+str(height))
        else:
            raise TypeError("Only numerical values accepted for dimensions: "+str(base)+str(" ")+str(height))
    else:
        raise AttributeError("Argumentation incomplete. Please input all dimensions")

if __name__ == "__main__":
    sample_base = 2
    sample_height = 2
    print("Surface Area of pyramid: ",
          surface_area_pyramid(sample_base, sample_height))


def volume_pyramid(base: Number, height: Number) -> Number:
    """
    Calculates the volume of a square-based pyramid
    :param base: side of base
    :param height: height of pyramid
    :return: volume of pyramid
    >>> volume_pyramid(2,2)
    2.6666666666666665
    """

    if dim_validate_argument(base) and dim_validate_argument(height):
        if dim_validate_number(base) and dim_validate_number(height):
            if dim_validate_positive(base) and dim_validate_positive(height):
                return base**2*height/3
            else:
                raise ValueError("All dimensions must be positive: "+str(base)+str(" ")+str(height))
        else:
            raise TypeError("Only numerical values accepted for dimensions: "+str(base)+str(" ")+str(height))
    else:
        raise AttributeError("Argumentation incomplete. Please input all dimensions")

if __name__ == "__main__":
    sample_base = 2
    sample_height = 2
    print("Volume of pyramid: ",
          volume_pyramid(sample_base, sample_height))


def surface_area_triangular_prism(base: Number, height: Number, length: Number) -> Number:
    """
    Calculates the surface area of and isosceles triangular prism
    :param base: triangle base
    :param height: triangle height
    :param length: length of prism
    :return:Surface area of the prism
    >>> surface_area_triangular_prism(2, 2, 2)
    16
    """

    if dim_validate_argument(base) and dim_validate_argument(height) and dim_validate_argument(length):
        if dim_validate_number(base) and dim_validate_number(height) and dim_validate_number(length):
            if dim_validate_positive(base) and dim_validate_positive(height) and dim_validate_positive(length):
                return base*height + 2*length*height + length*base
            else:
                raise ValueError("All dimensions must be positive: "+str(base)+str(" ")+str(height)+str(" ")+str(length))
        else:
            raise TypeError("Only numerical values accepted for dimensions: "+str(base)+str(" ")+str(height)+str(" ")+str(length))
    else:
        raise AttributeError("Argumentation incomplete. Please input all dimensions")

if __name__ == "__main__":
    sample_base = 2
    sample_height = 2
    sample_length = 2
    print("Surface area of triangular prism: ",
          surface_area_triangular_prism(sample_base, sample_height, sample_length))


def volume_triangular_prism(base: Number, height: Number, length: Number) -> Number:
    """
    Calculates the volume of an isosceles triangular prism
    :param base: triangle base
    :param height: triangle height
    :param length: length of prism
    :return:Surface area of the prism
    >>> volume_triangular_prism(2,3,5)
    15.0
    """

    if dim_validate_argument(base) and dim_validate_argument(height) and dim_validate_argument(length):
        if dim_validate_number(base) and dim_validate_number(height) and dim_validate_number(length):
            if dim_validate_positive(base) and dim_validate_positive(height) and dim_validate_positive(length):
                return base*height*length/2
            else:
                raise ValueError("All dimensions must be positive: "+str(base)+str(" ")+str(height)+str(" ")+str(length))
        else:
            raise TypeError("Only numerical values accepted for dimensions: "+str(base)+str(" ")+str(height)+str(" ")+str(length))
    else:
        raise AttributeError("Argumentation incomplete. Please input all dimensions")

if __name__ == "__main__":
    sample_base = 2
    sample_height = 3
    sample_length = 5
    print("Volume: of triangular prism: ",
          volume_triangular_prism(sample_base, sample_height, sample_length))


def area_circle_sector(theta: Number, radius: Number) -> Number:
    """
    Calculates the area of a sector of a circle from its radius and sector angle
    :param theta: angle of sector
    :param radius: radius of circle
    :return:The area of the sector
    >>> area_circle_sector(pi, 5)
    39.269908169872416
    """

    if dim_validate_argument(theta) and dim_validate_argument(radius):
        if dim_validate_number(theta) and dim_validate_number(radius):
            if dim_validate_positive(theta) and dim_validate_positive(radius):
                return theta*radius**2/2
            else:
                raise ValueError("All dimensions must be positive: "+str(theta)+str(" ")+str(radius))
        else:
            raise TypeError("Only numerical values accepted for dimensions: "+str(theta)+str(" ")+str(radius))
    else:
        raise AttributeError("Argumentation incomplete. Please input all dimensions")


if __name__ == "__main__":
    sample_theta = pi
    sample_radius = 5
    print("Area of sector: ",
          area_circle_sector(sample_theta, sample_radius))


def surface_area_icosahedron(side: Number) -> Number:
    """
    Calculates the surface area of an icosahedron from the length of its side
    :param side: length of one side
    :return: Surface area of icosahedron
    >>> surface_area_icosahedron(5)
    216.50635094610965
    """

    if dim_validate_argument(side):
        if dim_validate_number(side):
            if dim_validate_positive(side):
                return 5*sqrt(3)*side**2
            else:
                raise ValueError("All dimensions must be positive: "+str(side))
        else:
            raise TypeError("Only numerical values allowed for dimensions: "+str(side))
    else:
        raise AttributeError("Argumentation incomplete. Please input all dimensions")

if __name__ == "__main__":
    sample_side = 5
    print("Surface area of icosahedron:",
          surface_area_icosahedron(sample_side))


def volume_icosahedron(side: Number) -> Number:
    """
    Calculates the volume of an icosahedron from the length of its side
    :param side: length of one side
    :return: The volume of the icosahedron
    >>> volume_icosahedron(5)
    272.71187382811405
    """

    if dim_validate_argument(side):
        if dim_validate_number(side):
            if dim_validate_positive(side):
                return side**3*5*(3+sqrt(5))/12
            else:
                raise ValueError("All dimensions must be positive: "+str(side))
        else:
            raise TypeError("Only numerical values allowed for dimensions: "+str(side))
    else:
        raise AttributeError("Argumentation incomplete. Please input all dimensions")

if __name__ == "__main__":
    sample_side = 5
    print("Volume of icosahedron: ",
          volume_icosahedron(sample_side))


