__author__ = 'bemsibom'


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