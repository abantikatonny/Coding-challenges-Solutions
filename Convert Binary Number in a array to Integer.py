import math
def getDecimalValue(head):

    new_list = []
    for i in range(len(head) -1, -1, -1):
        # new_list = []
        new_list.append(head[i])
    # print(new_list)

    count = 0
    for i in range(len(new_list)):

        # print("kk", head[i])
        print("kkk", i)
        print("pppp", new_list[i])
        p = new_list[i] * (2 ** i)
        print("you", p)
        count += p
        # print("mmm", count)
    # print("lllll", count)


print(getDecimalValue([1, 1, 0]))