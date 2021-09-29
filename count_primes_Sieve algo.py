def is_prime(num):

    prime_list = [True for i in range(num)]
    i = 2
    while(i * i < num):
        if(prime_list[i] == True):
            for p in range(i*i, num, i):
                prime_list[p] = False
        i += 1

    counter = 0
    for i in range(2, len(prime_list)):
        if prime_list[i]:
            counter += 1
    return counter

print(is_prime(10000000))