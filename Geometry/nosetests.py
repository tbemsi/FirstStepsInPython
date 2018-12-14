__author__ = 'bemsibom'

from geom_formulae import *
from nose.tools import *


def test_rhombus_perimeter_int():
    assert rhombus_perimeter(1) == 4
    assert rhombus_perimeter(4) == 16
    s = 3
    assert rhombus_perimeter(s*2) == 4*rhombus_perimeter(s/2)


eps = 1e-6


def test_rhombus_area_bh():
    assert 4/10 - eps < rhombus_area_bh(0.1, 4.0) < 4/10 + eps


@raises(TypeError)
def test_rhombus_area_dd():
    rhombus_area_dd("a string")


@raises(TypeError)
def test_rhombus_area_sin():
    rhombus_area_sin("a string")


def test_parallelogram_perimeter():
    assert parallelogram_perimeter(0, 0) == 0
    assert parallelogram_perimeter(5, 5) == 20
    b = 4
    l = 6
    assert parallelogram_perimeter(b, l) == parallelogram_perimeter(l, b)


@raises(TypeError)
def test_area_regular_polygon_rad():
    area_regular_polygon_rad("a string")


@raises(TypeError)
def test_area_regular_polygon_apotheon():
    area_regular_polygon_apotheon("a string")


eps = 1e-2


def test_area_circle():
    assert pi - eps < area_circle(1) < pi + eps


eps = 1e-6


def test_perimeter_circle():
    assert 2*pi - eps < perimeter_circle(1) < 2*pi + eps


@raises(TypeError)
def test_surface_area_cone():
    surface_area_cone("a string")


def test_volume_cone():
    assert volume_cone(0, 0) == 0
    assert volume_cone(1, 3/pi) == 1
    r = 2
    h = 2
    assert volume_cone(r*2, h) == 4*volume_cone(r, h)


@raises(TypeError)
def test_surface_area_cylinder():
    surface_area_cylinder("a string")


eps = 1e-2


def test_volume_cylinder():
    assert pi - eps < volume_cylinder(1, 1) < pi + eps


@raises(TypeError)
def test_surface_area_pyramid(base, height):
    if base or height < 0:
        raise TypeError("Negative value for dimension")


@raises(TypeError)
def test_area_triangular_prism(base, height, length):
    if base or height or length < 0:
        raise TypeError("dimensions cannot be negative")


def test_volume_triangular_prism():
    assert volume_triangular_prism(0, 0, 0) == 0
    assert volume_triangular_prism(1, 2, 3) == 3
    l = 2
    b = 3
    h = 5
    assert volume_triangular_prism(l, b, h) == volume_triangular_prism(l, h, b) == volume_triangular_prism(b, l, h)


@raises(TypeError)
def test_area_circle_sector(radius):
    if radius < 0:
        raise TypeError("Wrong value for radius")


eps = 1e-6


def test_surface_area_icosahedron():
    5*sqrt(3) - eps < surface_area_icosahedron(1) < 5+sqrt(3) + eps


@raises(TypeError)
def test_volume_icosahedron(side):
    if side < 0:
        raise TypeError("Wrong value for side length")


__author__ = 'bemsibom'

from geom_formulae import *
from nose.tools import *

# rhombus perimeter


@raises(TypeError)
def test_rhombus_perimeter():
    rhombus_perimeter("a string")


@raises(ValueError)
def test_rhombus_perimeter():
    rhombus_perimeter(-6)


@raises(AttributeError)
def test_rhombus_perimeter():
    rhombus_perimeter(None)


#rhombus_area


@raises(ValueError)
def test_rhombus_area_bh():
    rhombus_area_bh(-4, 6)


@raises(AttributeError)
def test_rhombus_area_dd():
    rhombus_area_dd(None, None) or rhombus_area_dd(None, 6) or rhombus_area_dd(2, None)


@raises(TypeError)
def test_rhombus_area_sin():
    rhombus_area_sin(-5, "a string") or rhombus_area_sin("a string", 9)

    #parallelogram perimeter


@raises(TypeError)
def test_parallelogram_perimeter():
    parallelogram_perimeter("a string", 5) or parallelogram_perimeter(4, "a string") or parallelogram_perimeter(
        "a string", "a string")


@raises(ValueError)
def test_parallelogram_perimeter():
    parallelogram_perimeter(-5, 5) or parallelogram_perimeter(-4, -4) or parallelogram_perimeter(4, -6)


@raises(AttributeError)
def test_parallelogram_perimeter():
    parallelogram_perimeter(None, 5) or parallelogram_perimeter(3, None) or parallelogram_perimeter(None, None)


#Area of regular polygon


@raises(TypeError)
def test_area_regular_polygon_sd():
    area_regular_polygon_sd("string", 3) or area_regular_polygon_sd(3, "string") or area_regular_polygon_sd("string",
                                                                                                            "string")


@raises(ValueError)
def test_area_regular_polygon_rad():
    area_regular_polygon_rad(-7, 4) or area_regular_polygon_rad(7, 4.5) or area_regular_polygon_rad(7, -4)


@raises(AttributeError)
def test_area_regular_polygon_apotheon():
    area_regular_polygon_apotheon(None, 5) or area_regular_polygon_apotheon(5, None) or area_regular_polygon_apotheon(
        None, None)


#Circles


@raises(TypeError)
def test_area_circle():
    area_circle("a string")


def test_perimeter_circle():
    perimeter_circle("a string")


@raises(ValueError)
def test_area_circle():
    area_circle(-7)


def test_perimeter_circle():
    perimeter_circle(-5)


@raises(AttributeError)
def test_area_circle():
    area_circle(None)


@raises(AttributeError)
def test_perimeter_circle():
    perimeter_circle(None)


#Cones


@raises(TypeError)
def test_surface_area_cone():
    surface_area_cone("a string", 5) or surface_area_cone(5, "a string") or surface_area_cone("a string", "a string")


def test_volume_cone():
    volume_cone("a string", 5) or volume_cone(5, "a string") or volume_cone("a string", "a string")


@raises(ValueError)
def test_surface_area_cone():
    surface_area_cone("a string", 5) or surface_area_cone(5, "a string") or surface_area_cone("a string", "a string")


@raises(AttributeError)
def test_volume_cone():
    volume_cone(None, 5) or volume_cone(5, None) or volume_cone(None, None)


@raises(AttributeError)
def test_surface_area_cone():
    surface_area_cone(None, 5) or surface_area_cone(5, None) or surface_area_cone(None, None)


#Cylinders


@raises(TypeError)
def test_surface_area_cylinder():
    surface_area_cylinder("a string", 5) or surface_area_cylinder(5, "a string") or surface_area_cylinder("a string",
                                                                                                          "a string")


def test_volume_cylinder():
    volume_cylinder("a string", 5) or volume_cylinder(5, "a string") or volume_cylinder("a string", "a string")


@raises(ValueError)
def test_surface_area_cylinder():
    surface_area_cylinder("a string", 5) or surface_area_cylinder(5, "a string") or surface_area_cylinder("a string",
                                                                                                          "a string")


@raises(AttributeError)
def test_volume_cylinder():
    volume_cylinder(None, 5) or volume_cylinder(5, None) or volume_cylinder(None, None)


@raises(AttributeError)
def test_surface_area_cylinder():
    surface_area_cylinder(None, 5) or surface_area_cylinder(5, None) or surface_area_cylinder(None, None)


# Pyramids


@raises(TypeError)
def test_surface_area_pyramid():
    surface_area_pyramid("a string", 5) or surface_area_pyramid(5, "a string") or surface_area_pyramid("a string",
                                                                                                       "a string")


@raises(TypeError)
def test_volume_cylinder():
    volume_pyramid("a string", 5) or volume_pyramid(5, "a string") or volume_pyramid("a string", "a string")


@raises(ValueError)
def test_surface_area_pyramid():
    surface_area_pyramid("a string", 5) or surface_area_pyramid(5, "a string") or surface_area_pyramid("a string",
                                                                                                       "a string")


@raises(AttributeError)
def test_volume_pyramid():
    volume_pyramid(None, 5) or volume_pyramid(5, None) or volume_pyramid(None, None)


@raises(AttributeError)
def test_surface_area_pyramid():
    surface_area_pyramid(None, 5) or surface_area_pyramid(5, None) or surface_area_pyramid(None, None)


#Triangular prisms


@raises(TypeError)
def test_surface_area_triangular_prism():
    surface_area_triangular_prism("a string", 5, 6) or surface_area_triangular_prism(5, "a string", 6) or \
        surface_area_triangular_prism(5, 6, "a string")


@raises(TypeError)
def test_volume_triangular_prism():
    volume_triangular_prism("a string", 5, 6) or volume_triangular_prism(5, "a string", 6) or \
        volume_triangular_prism(5, 6, "a string")


@raises(ValueError)
def test_surface_area_pyramid():
    surface_area_triangular_prism(-5, 5, 6) or surface_area_triangular_prism(5, -7, 6) or \
        surface_area_triangular_prism(5, 6, -3)


@raises(ValueError)
def test_volume_pyramid():
    volume_triangular_prism(-5, 5, 6) or volume_triangular_prism(5, -7, 6) or \
        volume_triangular_prism(5, 6, -4)


@raises(AttributeError)
def test_surface_area_pyramid():
    surface_area_pyramid(None, 5) or surface_area_pyramid(5, None) or surface_area_pyramid(None, None)


@raises(AttributeError)
def test_volume_pyramid():
    volume_triangular_prism(None, 5, 6) or volume_triangular_prism(5, None, 6) or \
    volume_triangular_prism(5, 6, None)


#Circle Sector


@raises(TypeError)
def test_circle_sector():
    area_circle_sector("a string", 5) or area_circle_sector(5, "a string")


@raises(ValueError)
def test_circle_sector():
    area_circle_sector(-6, 5) or area_circle_sector(5, -8)


@raises(AttributeError)
def test_circle_sector():
    area_circle_sector(None, 5) or area_circle_sector(5, None)


#icosahedron


@raises(TypeError)
def test_surface_area_icosahedron():
    surface_area_icosahedron("a string")


@raises(TypeError)
def test_volume_icosahedron():
    volume_icosahedron("a string")


@raises(ValueError)
def test_surface_area_icosahedron():
    surface_area_icosahedron(-6)


@raises(ValueError)
def test_volume_icosahedron():
    volume_icosahedron(-6)


@raises(AttributeError)
def test_volume_icosahedron():
    volume_icosahedron(None)
