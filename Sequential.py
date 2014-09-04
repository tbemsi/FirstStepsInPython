__author__ = 'bemsibom'

from math import *
from numpy import *
from scipy.misc import *
from input_validation import *


def secant(f: callable, a: (int, float), b: (int, float), epsilon: float) -> float:
    """
    Finds the root of a function using the secant method
    :param f: Function whose roots are looked for
    :param a: first guess
    :param b: second guess
    :param epsilon: accepted tolerance
    :return:
    """
    if dim_validate_argument(a) and dim_validate_argument(b):
        if dim_validate_int_float(a) and dim_validate_int_float(b) and dim_validate_float(epsilon):
            if dim_validate_positive(epsilon):
                while fabs(f(b)) > epsilon and f(a) != f(b):
                    root = b - (f(b)*(a - b)/(f(a) - f(b)))
                    a = b
                    b = root
                return root
            else:
                raise ValueError("Error can only be positive: "+str(epsilon))
        else:
            raise TypeError("Only float values accepted for integral limits: "+str(a)+str(" ")+str(b)+str(" ")+str(epsilon))
    else:
        raise AttributeError("Argumentation incomplete. Please input all parameters")


if __name__ == "__main__":
    def f(x):
        return x**2-2
    sample_a = pi
    sample_b = 6.5
    sample_error = 1e-6
    print("Root from Secant method: ",
          secant(f, sample_a, sample_b, sample_error))

#Newton Raphson Method


def newton_raphson(f: callable, x0: (int, float), error: float) -> float:
    """
    Newton's method
    :param f: function whose roots are to be determined
    :param x0: initial guess
    :param error: tolerance
    :return: approximate root of function according to Newton's method
    """
    if dim_validate_argument(x0) and dim_validate_argument(error):
        if dim_validate_float(x0) and dim_validate_float(error):
                while f(x0) >= error and derivative(f, x0, dx=1e-6) != 0:
                    x0 = x0 - f(x0)/derivative(f, x0, dx=1e-6)
                return x0
        else:
            raise TypeError("Only float values accepted for integral limits: "+str(x0)+str(" ")+str(error))
    else:
        raise AttributeError("Argumentation incomplete. Please input all parameters")


if __name__ == "__main__":
    def f(x):
        return x**2 - 2
    sample_a = 1.9
    sample_b = 6.5
    sample_error = 1e-30
    print("Root from Newton-Raphson's method: ",
          newton_raphson(f, sample_a, sample_error))


def root_finder(f: callable, guess0: None, guess1: None, error: float) -> float:
    """
    #Finds the roots using different methods
    #:param f: function whose roots are to be calculated
    #:param guess0: first initial guess
    #:param guess1: second intial guess
    #:param error: tolerance
    #:return: approximate root of function

    """
    if guess1 is None:
        return newton_raphson(f, guess0, error)
    else:
        return secant(f, guess0, guess1, error)

if __name__ == "__main__":
    def f(x):
        return x**2 - 2
    sample_a = 1.4
    sample_b = None
    sample_error = 1e-6
    print("Root from the root finder: ",
          root_finder(f, sample_a, sample_b, sample_error))


#Midpoint Method


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
        return 3*x**2
    sample_a = 0
    sample_b = 5
    sample_n = 6
    print("Integral: ",
          midpoint(f, sample_a, sample_b, sample_n))

# trapezoidal rule


def trapezoidal(f: callable, a: (int, float), b: (int, float), n: int) -> float:
    """
    Calculates integral using trapezoidal rule
    :param f: function to be integrated
    :param a: start point
    :param b: end point
    :param n: number of divisions
    :return: approximate integral of f
    """
    x = linspace(a, b, n+1)
    y = f(x)
    h = (b - a)/(2*n)
    sum = 0
    for i in range(1, n):
        sum += + 2*y[i]
    integral = h * (f(a) + f(b) + sum)
    return integral


if __name__ == "__main__":
    def f(x):
        return 3*x**2
    sample_a = 1
    sample_b = 5
    sample_n = 100000
    print("Integral: ",
          trapezoidal(f, sample_a, sample_b, sample_n))


# Simpson's method


def simpson(f, a, b, n) -> float:
    """

    :param f:
    :param a:
    :param b:
    :param n:
    :return:
    """
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


if __name__ == "__main__":
    def f(x):
        return 3*x**2
    sample_a = 1
    sample_b = 5
    sample_n = 100
    print("Integral: ",
          simpson(f, sample_a, sample_b, sample_n))