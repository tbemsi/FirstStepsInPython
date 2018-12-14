__author__ = 'bemsibom'

from objects import *

print("Welcome to this program!!! I will help you calculate the geometric properties of certain shapes and solids")

set = {'circle', 'rhombus', 'parallelogram', 'polygon', 'cone', 'cylinder', 'pyramid', 'prism', 'sector',
              'icosahedron'}

print("The following are the shapes in my library:", set)

def main():
    shape = None
    while shape != 'quit':
        shape = input("Please enter the shape whose properties you want: ")
        if shape == 'circle' or shape == 'Circle':
            try:
                radius = float(input("Enter radius of circle: "))
                circle = Circle(radius)
                print(circle)
            except ValueError as err:
                print(err.args[0])
            finally:
                return main()
        elif shape == 'rhombus' or shape == 'Rhombus':
            try:
                side_length = float(input("Enter side length of rhombus: "))
                rhombus = Rhombus(side_length)
                print(rhombus)
            except ValueError as err:
                print(err.args[0])
            finally:
                return main()
        elif shape == 'parallelogram' or shape == 'Parallelogram':
            try:
                side_length = float(input("Enter side length of parallelogram: "))
                base_length = float(input("Enter base length of parallelogram: "))
                para = Parallelogram(base_length, side_length)
                print(para)
            except ValueError as err:
                print(err.args[0])
            finally:
                return main()


main()
