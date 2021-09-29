def ishappy(n):

    import math
    # n = 19
    seen = set()
    while n not in seen:
        seen.add(n)
        sum = 0
        while n > 0:
            p = n % 10
            sum += p * p
            n = math.floor(n / 10)
            if sum == 1:
                return True

            else:
                n = sum
    return False

if __name__ == '__main__':
    print(ishappy(19))

