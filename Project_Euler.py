__author__ = 'bemsibom'
"""
#Problem number 1
def multiples_3_5(n):
    i = 0
    j = 0
    k = 0
    sum1 = 0
    sum2 = 0
    sum3 = 0
    while i < n:
        sum1 = sum1 + i
        i = i + 3
    while j < n:
        sum2 = sum2 + j
        j = j + 5
    while k < n:
        sum3 = sum3 + k
        k = k + 15
    return sum1 + sum2 - sum3

if __name__ == "__main__":
    sample_n = 1000
    print("Sum:",
        multiples_3_5(sample_n))

#problem number 6
def sum_square(n):
    i=0
    j = 0
    sum1 = 0
    sum2 = 0
    sum3 = 0
    while i <= n:
        sum1 = sum1+ i**2
        i = i + 1
    while j <= n:
        sum2 = sum2 + j
        j = j+1
    sum3 = sum2**2
    return sum3 - sum1
if __name__ == "__main__":
    sample_n = 100
    print("Sum:",
        sum_square(sample_n))
"""
#problem number 2: Fibonacci stuff

def Sum_even_Fibonacci(n):
    sum_1 = 1
    sum_2 = 2
    sum = 3
    for i in range(n):
        sum_1 = sum_2
        sum_2 = sum
        sum = sum_1 + sum_2
    return sum

if __name__ == "__main__":
    sample_n = 8
    print("Sum:",
        Sum_even_Fibonacci(sample_n))


#problem number 3: Palindrome

def largest_palindrome():
    greatest = 0
    for i in range(10):
        for j in range(10):
            for k in range(10):
                product = i*100001 + j*10010 + k * 1100
                for l in range(100, 999):
                    if product % l == 0 and product/l <= 999 and product > greatest:
                        greatest = product

    return greatest

if __name__ == "__main__":
    sample_n = 8
    print("Greatest:",
          largest_palindrome())

#evenly divisible


def evenly_divisible():
    number = 0
    if number % 1 != 0 and number % 2 != 0 and number % 3 != 0 and number % 4 != 0 and number % 5 != 0 and number %\
            6 != 0 and number % 7 != 0 and number % 8 != 0 and number % 9 != 0 and number % 10 != 0:
            number += 2
    return number

if __name__ == "__main__":
    sample_n = 8
    print("Evenly divisible:",
          evenly_divisible())