__author__ = 'bemsibom'

import csv
from objects import *


myfile = open("shapes_and_dimensions.csv", 'r')

shape_dict = {'circle': 2, 'rhombus': 3, 'parallelogram': 3, 'polygon': 2, 'cone': 3, 'cylinder': 3, 'pyramid': 4,
              'prism': 4, 'sector': 3, 'icosahedron': 2}

with open("shapes_and_dimensions.csv", 'r') as csvfile:
    shapes = csv.reader(csvfile, delimiter=' ')
    for row in shapes:
        if len(row) == 0:
            print("EMPTY ROW")
        else:
            try:
                length_check = shape_dict[row[0]] == len(row)
            except KeyError as err:
                print("I don't understand", err.args[0], "; it is not in my dictionary")
            if length_check is True:
                if row[0] == 'circle':
                    try:
                        cir = Circle(float(row[1]))
                        print(cir)
                    except ValueError as err:
                        print(err.args[0])
                    #cir.draw()
                elif row[0] == 'rhombus':
                    try:
                        rh = Rhombus(float(row[1]))
                        print(rh)
                        #rh.draw()
                    except ValueError as err:
                        print(err.args[0])
                elif row[0] == 'parallelogram':
                    try:
                        para = Parallelogram(float(row[1]), float(row[2]))
                        print(para)
                        #para.draw()
                    except ValueError as err:
                        print(err.args[0])
                elif row[0] == 'polygon':
                    try:
                        octa = Octagon(float(row[1]))
                        print(octa)
                        #octa.draw()
                    except ValueError as err:
                        print(err.args[0])
                elif row[0] == 'pyramid':
                    try:
                        py = Pyramid(float(row[1]), float(row[2]))
                        print(py)
                        #py.draw()
                    except ValueError as err:
                        print(err.args[0])
                elif row[0] == 'prism':
                    try:
                        pr = Prism(float(row[1]), float(row[2]), float(row[3]))
                        print(pr)
                        #pr.draw()
                    except ValueError as err:
                        print(err.args[0])
                elif row[0] == 'cone':
                    try:
                        co = Cone(float(row[1]), float(row[2]))
                        #print(co)
                    except ValueError as err:
                        print(err.args[0])
                elif row[0] == 'sector':
                    try:
                        sec = Sector(float(row[1]), float(row[2]))
                        print(sec)
                        #sec.draw()
                    except ValueError as err:
                        print(err.args[0])
                elif row[0] == 'cylinder':
                    try:
                        cy = Cylinder(float(row[1]), float(row[2]))
                        print(cy)
                        #cy.draw()
                    except ValueError as err:
                        print(err.args[0])
            else:
                print("Tell me something more")