__author__ = 'bemsibom'

from math import *
from numpy import *
from scipy.misc import *
from input_validation import *
from pylab import *
import pylab


def midpoint(f: callable, a: (int, float), b: (int, float), n: int) -> float:
    """
    Integrates a function using the midpoint method
    :param f: The function to be integrated
    :param a: The lower bound of the integral
    :param b: The upper bound of the integral
    :param n: The number of iterations
    :return: The value of the integral
    """
    if dim_validate_argument(a) and dim_validate_argument(b):
        if dim_validate_number(a) and dim_validate_number(b):
            if dim_validate_positive(n):
                h = (b-a)/n
                x = linspace(a, b, n+1)
                mid = [0] * n
                y = [0] * n
                sum = 0
                for i in range(1, n+1):
                    mid[i-1] = (x[i] - x[i-1])/2 + x[i-1]
                    y[i-1] = f(mid[i-1])
                    sum += y[i-1]
                return sum * h
            else:
                raise ValueError("number of iterations can only be a positive integer: "+str(n))
        else:
            raise TypeError("Only numbers accepted for integral limits: "+str(a)+str(" ")+str(b)+str(" "))
    else:
        raise AttributeError("Argumentation incomplete. Please input all parameters")


if __name__ == "__main__":
    def f(x):
        return x**2-1
    sample_a = -2
    sample_b = 2
    sample_n = 10
    print("Integral of f(x) using midpoint method: ",
          midpoint(f, sample_a, sample_b, sample_n))

if __name__ == "__main__":
    def f(x):
        return x**2-1
    sample_a = -2
    sample_b = 2
    sample_n = 10000
    print("Integral of f(x) using midpoint method: ",
          midpoint(f, sample_a, sample_b, sample_n))

if __name__ == "__main__":
    def g(x):
        return 1/x
    sample_a = 0.1
    sample_b = 2
    sample_n = 100
    print("Integral of g(x) using midpoint method: ",
          midpoint(g, sample_a, sample_b, sample_n))


def trapezoidal(f: callable, a: (int, float), b: (int, float), n: int) -> float:
    """
    Calculates integral using trapezoidal rule
    :param f: function to be integrated
    :param a: start point
    :param b: end point
    :param n: number of divisions
    :return: approximate integral of f
    """
    if dim_validate_argument(a) and dim_validate_argument(b):
        if dim_validate_number(a) and dim_validate_number(b) and dim_validate_int_float(n):
            if dim_validate_positive(n):
                x = linspace(a, b, n+1)
                y = f(x)
                h = (b - a)/(2*n)
                sum1 = 0
                for i in range(1, n):
                    sum1 += + 2*y[i]
                integral = h * (f(a) + f(b) + sum1)
                return integral
            else:
                raise ValueError("number of iterations can only be a positive integer: "+str(n))
        else:
            raise TypeError("Only numbers accepted for integral limits, only positive integers for iterations:"+str(a) +
                            str(" ")+str(b)+str(" ")+str(" ")+str(n))
    else:
        raise AttributeError("Argumentation incomplete. Please input all parameters")


if __name__ == "__main__":
    def f(x):
        return x**2-1
    sample_a = -2
    sample_b = 2
    sample_n = 10
    print("Integral of f(x) using trapezoidal method:",
          trapezoidal(f, sample_a, sample_b, sample_n))

if __name__ == "__main__":
    def f(x):
        return x**2-1
    sample_a = -2
    sample_b = 2
    sample_n = 10000
    print("Integral of f(x) using trapezoidal method:",
          trapezoidal(f, sample_a, sample_b, sample_n))

if __name__ == "__main__":
    def g(x):
        return 1/x
    sample_a = 0.1
    sample_b = 2
    sample_n = 100
    print("Integral of g(x) using trapezoidal method: ",
          trapezoidal(g, sample_a, sample_b, sample_n))

# Simpson's method


def simpson(f: callable, a: (int, float), b: (int, float), n: int) -> float:
    """
    Approximates the integral to a function using Simpson's method
    :param f: function to be integrated
    :param a: lower integration bound
    :param b: upper integration bound
    :param n: number of divisions
    :return: Approximate value of integral
    """
    if dim_validate_argument(a) and dim_validate_argument(b):
        if dim_validate_number(a) and dim_validate_number(b) and dim_validate_int_float(n):
            if dim_validate_positive(n):
                x = linspace(a, b, n+1)
                y = f(x)
                h = (b - a)/n
                sum1 = 0
                sum2 = 0
                for i in range(1, n-1, 2):
                    sum1 += 4 * y[i]
                for i in range(2, n, 2):
                    sum2 += 2 * y[i]
                integral = h/3 * (f(a) + f(b) + sum1 + sum2)
                return integral
            else:
                raise ValueError("number of iterations can only be a positive integer: "+str(n))
        else:
            raise TypeError("Only numbers accepted for integral limits, only positive integers for iterations:"+str(a) +
                            str(" ")+str(b)+str(" ")+str(" ")+str(n))
    else:
        raise AttributeError("Argumentation incomplete. Please input all parameters")

if __name__ == "__main__":
    def f(x):
        return x**2-1
    sample_a = -2
    sample_b = 2
    sample_n = 10
    print("Integral of f(x) using simpson's method: ",
          simpson(f, sample_a, sample_b, sample_n))

if __name__ == "__main__":
    def f(x):
        return x**2-1
    sample_a = -2
    sample_b = 2
    sample_n = 10000
    print("Integral of f(x) using Simpson's method: ",
          simpson(f, sample_a, sample_b, sample_n))

if __name__ == "__main__":
    def g(x):
        return 1/x
    sample_a = 0.1
    sample_b = 2
    sample_n = 1000000
    print("Integral of g(x) using Simpson's method: ",
          simpson(g, sample_a, sample_b, sample_n))


def integral_calculator(f: callable, a: (int, float), b: (int, float), n: int, method: str) -> float:
    """
    Calculates integral of a function by one of three methods
    :param f: function to be integrated
    :param a: lower bound of integral
    :param b: upper bound of integral
    :param n: number of iterations
    :return: value of integral
    """
    integral = 0
    if method != "midpoint" and method != "simpson" and method != "trapezoidal":
        raise TypeError("Integral type must be either midpoint, simpson or trapezoidal")
    if method == "midpoint":
        integral = midpoint(f, a, b, n)
    if method == "simpson":
        integral = simpson(f, a, b, n)
    if method == "trapezoidal":
        integral = trapezoidal(f, a, b, n)

    return integral

if __name__ == "__main__":
    def f(x):
        return x**2+2
    sample_a = -2
    sample_b = 2
    sample_n = 10000
    sample_method = "simpson"
    print("Integral from the integral calculator using the", sample_method, "method: ",
          integral_calculator(f, sample_a, sample_b, sample_n, sample_method))


def plot_integral(f: callable, a: (int, float), b: (int, float), n: int):
    """
    Plots the integral of a function against the resolution
    :param f: function to be integrated
    :param a:lower bound of integral
    :param b: upper bound of integral
    :param n: number of iteration
    :return: plot of integral
    """
    x = range(1,n+1)
    I_midpoint = [1]*n
    I_simpson = [1]*n
    I_trapezoidal = [1]*n
    for i in range(1, n):
        I_midpoint[i] = integral_calculator(f, a, b, x[i], "midpoint")
        I_simpson[i] = integral_calculator(f, a, b, x[i], "simpson")
        I_trapezoidal[i] = integral_calculator(f, a, b, x[i], "trapezoidal")
    plot(x, I_midpoint, '-r', label='Midpoint method')
    plot(x, I_simpson, '-b', label='Simpson method')
    plot(x, I_trapezoidal, '-g', label='Trapezoidal method')
    legend(loc='lower left')
    title('Variation of integral values with number of iterations for different numerical methods')
    pylab.savefig('/home/bemsibom/PycharmProjects/Figures/integrals.png')
    show()

if __name__ == "__main__":
    def f(x):
        return sin(x)+cos(x)
    sample_a = -2
    sample_b = 2
    sample_n = 90
    sample_method = "midpoint"
    plot_integral(f, sample_a, sample_b, sample_n)

