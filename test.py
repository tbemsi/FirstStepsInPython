__author__ = 'bemsibom'
from scipy.misc import *
from math import *
from numpy import *

def power_digit(n):
    number = str(2**n)
    sum = 0
    for i in range(len(number)):
        sum += int(number[i])
    return [0]*n

if __name__ == "__main__":
    n_ex = 1001
    print(power_digit(2))
