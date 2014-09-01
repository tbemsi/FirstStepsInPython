__author__ = 'bemsibom'

from geom_formulae import *
from nose.tools import *


def test_rhombus_perimeter_int():
    assert rhombus_perimeter(1) == 4
    assert rhombus_perimeter(4) == 16
    s = 5
    assert rhombus_perimeter(s*2) == 2*rhombus_perimeter(s)


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