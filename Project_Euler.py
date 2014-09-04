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

def findFib(n):
    first, last = 0, 1
    sum = 0
    while last <= n:
        if last % 2 == 0:
            sum += last
        temp = last
        last += first
        first = temp

    return sum

if __name__ == "__main__":
    print(findFib(4000000))

def multiplier():


    a = str(7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843)
    b = str(8586156078911294949545950173795833195285320880551112540698747158523863050715693290963295227443043557)
    c = str(6689664895044524452316173185640309871112172238311362229893423380308135336276614282806444486645238749)
    d = str(3035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776)
    e = str(6572733300105336788122023542180975125454059475224352584907711670556013604839586446706324415722155397)
    f = str(5369781797784617406495514929086256932197846862248283972241375657056057490261407972968652414535100474)
    g = str(8216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586)
    h = str(17866458359124566529476545682848912883142607690042242190226710556263211111093705442175069416589)
    i = str(604080719840385096245544436298123098787992724428490918884580156166097919133875499200524063689912560717606)
    j = str(76060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450)

    number = a+b+c+d+e+f+g+h+i+j
    greatest = 0
    for i in range(986):
        product = int(number[i]) * int(number[i+1]) * int(number[i+2]) * int(number[i+3])* int(number[i+4]) * int(number[i+5]) * int(number[i+6]) * int(number[i+7]) * int(number[i+8]) *int(number[i+9]) * int(number[i+10]) * int(number[i+11]) * int(number[i+12])
        if product > greatest:
            greatest = int(product)
    return greatest

if __name__ == "__main__":
    print(multiplier())

def power_digit(n):
    number = str(2**n)
    sum = 0
    for i in range(len(number)):
        sum += int(number[i])
    return sum

if __name__ == "__main__":
    n_ex = 1001
    print(power_digit(1000))
