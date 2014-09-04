__author__ = 'bemsibom'
from scipy.misc import *
from math import *
from numpy import *


def findFib(n):
    first, last = 0, 1
    sum = 0
    while last <= n:
        temp = last
        last += first
        first = temp
        #if last % 2 == 0:
        sum = +last
    return sum

if __name__ == "__main__":
    print(findFib(3))
