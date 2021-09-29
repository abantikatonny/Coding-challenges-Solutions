import math

def is_primes(num):

    flag = True

    if num == 0 or num == 1:
        flag = False

    for i in range(2, math.ceil(math.sqrt(num + 1))):
        # print(i)
        if num % i == 0:
            flag = False

    return flag

def countPrimes(self, n: int) -> int:

    count = 0

    for i in range(2, n):
        if is_primes(i):
            # primes.append(i)
            count += 1

    return count

print(is_primes(10))















