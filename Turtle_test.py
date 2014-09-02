

import turtle
from turtle import *
from numbers import Number
from math import *


def draw_rhombus(side: Number):
    """
    Draws a rhombus using turtle
    :param side: length of side of rhombus
    :return: plot of rhombus
    """
    turtle.right(45)
    turtle.forward(side)
    turtle.right(90)
    turtle.forward(side)
    turtle.right(90)
    turtle.forward(side)
    turtle.right(90)
    turtle.forward(side)
    turtle.done()

if __name__ == "__main__":
    draw_rhombus(100)


def draw_parallelogram(side_1: Number, side_2: Number):
    """
    Draws a parallelogram using turtle
    :param side_1: Length of one side
    :param side_2: Length of adjacent side to side 1
    :return: plot of parallelogram
    """
    turtle.forward(side_1)
    turtle.left(45)
    turtle.forward(side_2)
    turtle.left(135)
    turtle.forward(side_1)
    turtle.left(45)
    turtle.forward(side_2)
    turtle.done()

if __name__ == "__main__":
    draw_parallelogram(50, 100)


def draw_decagon(side: Number):
    """
    Plots a decagon using turtle
    :param side: Length of side of decagon
    :return: plot of decagon
    """
    i = 0
    while i < 10:
        turtle.forward(side)
        turtle.left(36)
        i = i+1
    turtle.done()

if __name__ == "__main__":
    draw_decagon(50)


def draw_circle(radius: Number):
    """
    Plots a circle using turtle
    :param radius: Radius of circle
    :return: Plot of circle
    """
    turtle.circle(radius)
    turtle.done()

if __name__ == "__main__":
    draw_circle(50)


def draw_pyramid(side: Number):
    """
    Plots a pyramid using turtle
    :param side: length of side
    :return: Plot of pyramid
    """
    turtle.forward(side)
    turtle.left(45)
    turtle.forward(side)
    turtle.left(135)
    turtle.forward(side)
    turtle.left(45)
    turtle.forward(side)
    turtle.goto(0, 0)
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.goto(side/2, 200)
    turtle.penup()
    turtle.goto(side, 0)
    turtle.pendown()
    turtle.goto(side/2, 200)
    turtle.penup()
    turtle.goto(side*cos(pi/4), side*sin(pi/4))
    turtle.pendown()
    turtle.goto(side/2, 200)
    turtle.penup()
    turtle.goto(side*(1+cos(pi/4)), side*sin(pi/4))
    turtle.pendown()
    turtle.goto(side/2, 200)
    turtle.done()

if __name__ == "__main__":
    draw_pyramid(100)


def draw_figures(area: Number):
    """
    Plots figures of the same area
    :param area: Area of figures
    :return:Plot of figures
    """
    begin_fill()
    turtle.right(45)
    turtle.forward(sqrt(area))
    turtle.right(90)
    turtle.forward(sqrt(area))
    turtle.right(90)
    turtle.forward(sqrt(area))
    turtle.right(90)
    turtle.forward(sqrt(area))
    i = 0
    while (i < 4):
        turtle.forward(sqrt(area))
        turtle.left(90)
        i = i+1
    turtle.circle(sqrt(area/pi))
    turtle.forward(sqrt(2*area))
    turtle.left(135)
    turtle.forward(sqrt(2)*sqrt(2*area))
    turtle.left(135)
    turtle.forward(sqrt(2*area))

    turtle.done()

if __name__ == "__main__":
    draw_figures(10000)

