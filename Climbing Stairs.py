# given x, compute 1 + 2 + ..... + x

def recursive_sum(x):

    if x == 1:
        return 1
    else:
        print(x, x + recursive_sum(x - 1))
        return x + recursive_sum(x - 1)



if __name__ == '__main__':
    print(recursive_sum(5))