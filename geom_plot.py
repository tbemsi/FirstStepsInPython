__author__ = 'bemsibom'

from pylab import *
import pylab
import numpy as np
from geom_formulae import *

#plotting properties of a rhombus


def plot_rhombus(side):
    v_rhombus_perimeter = vectorize(rhombus_perimeter)
    v_rhombus_area_bh = vectorize(rhombus_area_bh)

    s = np.linspace(0, side, 50)
    h = 5
    p = v_rhombus_perimeter(s)
    a = v_rhombus_area_bh(s, h)

    plot(s, a, '-r', label='Area')
    plot(s, p, '-b', label='Perimeter')
    xlabel('Length of side')
    legend(loc='upper right')
    title('Geometric properties of a rhombus as a function of side length')
    pylab.savefig('/home/bemsibom/PycharmProjects/Figures/rhombus_properties.png')
    show()

if __name__ == "__main__":
    plot_rhombus(5)

#plotting area of a regular polygon, varying length of sides


def plot_regular_polygon(side):
    v_area_regular_polygon_sd = vectorize(area_regular_polygon_sd)

    s = linspace(0, side)
    n = 20
    area = v_area_regular_polygon_sd(n, s)

    plot(s, area, '-r', label='Area of regular polygon')
    legend(loc='upper right')
    xlabel('Length of side')
    ylabel('Area of polygon')
    title('Variation of area of polygon with side length')
    pylab.savefig('/home/bemsibom/PycharmProjects/Figures/Regular_polygon_side_sl.png')
    show()

if __name__ == "__main__":
    plot_regular_polygon(5)


#plotting area of a regular polygon, varying number of sides


#plotting circle parameters


def plot_circle(radius: Number):
    v_area_circle = vectorize(area_circle)
    v_perimeter_circle = vectorize(perimeter_circle)

    rad = linspace(0, radius, 50)
    a = v_area_circle(rad)
    p = v_perimeter_circle(rad)

    plot(rad, a, '-b', label='Area')
    plot(rad, p, '-r', label='Perimeter')
    legend(loc='upper right')
    title('Geometrical properties of circles')
    xlabel('Radius')
    pylab.savefig('/home/bemsibom/PycharmProjects/Figures/circle_properties.png')
    show()

if __name__ == "__main__":
    plot_area_circle(5)


#plotting properties of cone


def plot_cone(radius: Number):
    v_surface_area_cone = vectorize(surface_area_cone)
    v_volume_cone = vectorize(volume_cone)

    side = 3
    height = 5
    rad = linspace(0, radius, 50)
    a = v_surface_area_cone(rad, side)
    v = v_volume_cone(rad, height)
    plot(rad, a, '-b', label='Surface Area')
    plot(rad, v, '-r', label='Volume')
    legend(loc='upper right')
    xlabel('Radius')
    title('Variation of geometrical properties of cones with radius')
    savefig('/home/bemsibom/PycharmProjects/Figures/Cone_properties.png')
    show()

if __name__ == "__main__":
    plot_cone(5)


    #plotting properties of cylinders


def plot_cylinder(radius: Number):
    v_surface_area_cylinder = vectorize(surface_area_cylinder)
    v_volume_cylinder = vectorize(volume_cylinder)

    rmax = 50
    height = 5
    radius = linspace(0, rmax, 100)
    A = v_surface_area_cylinder(radius, height)
    V = v_volume_cylinder(radius, height)

    plot(radius, A, '-b', label='Surface Area')
    plot(radius, V, '-r', label='Volume')
    legend(loc='upper right')
    xlabel('Radius')
    title('Variation of geometrical properties of cylinders with radius')
    savefig('/home/bemsibom/PycharmProjects/Figures/Cylinder_properties.png')
    show()

if __name__ == "__main__":
    plot_cone(5)

    #plotting properties of pyramid


def plot_pyramid(base_max: Number):
    v_surface_area_pyramid = vectorize(surface_area_pyramid)
    v_volume_pyramid = vectorize(volume_pyramid)

    base = linspace(0, base_max, 100)
    height = 5
    a = v_surface_area_pyramid(base, height)
    v = v_volume_pyramid(base, height)

    plot(base, a, '-g', label='Surface Area')
    plot(base, v, '-r', label='Volume')
    legend(loc='upper right')
    xlabel('base')
    title('Variation of Area and Perimeter of pyramids with base')
    savefig('/home/bemsibom/PycharmProjects/Figures/Pyramid_properties.png')
    show()

if __name__ == "__main__":
    plot_pyramid(5)

    #plotting properties of triangular prism

def plot_triangular_prism(base_max: Number):
    v_surface_area_triangular_prism = vectorize(surface_area_triangular_prism)
    v_volume_triangular_prism = vectorize(volume_triangular_prism)
    height = 10
    length = 5

    base = linspace(0, base_max, 100)
    a = v_surface_area_triangular_prism(base, height, length)
    v = v_volume_triangular_prism(base, height, length)

    plot(base, a, '-g', label='Surface Area')
    plot(base, v, '-r', label='Volume')
    xlabel('base')
    title('Variation of surface area and volume of a triangular prism with base length')
    savefig('/home/bemsibom/PycharmProjects/Figures/Prism_properties.png')
    show()

if __name__ == "__main__":
    plot_triangular_prism(5)


    #plotting area of icosahedron

def plot_icosahedron(sidemax: Number):
    v_surface_area_icosahedron = vectorize(surface_area_icosahedron)
    v_volume_icosahedron = vectorize(volume_icosahedron)

    side = linspace(0, sidemax)
    a = v_surface_area_icosahedron(side)
    v = v_volume_icosahedron(side)

    plot(side, a, '-g', label='Surface Area')
    plot(side, v, '-r', label='Volume')
    title('Variation of surface area and volume of icosahedron with side length')
    savefig('/home/bemsibom/PycharmProjects/Figures/Icosahedron_properties.png')
    show()

if __name__ == "__main__":
    plot_icosahedron(5)



