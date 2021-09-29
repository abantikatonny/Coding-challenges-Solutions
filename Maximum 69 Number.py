def number69(num):

    value = False
    list1 = [int(i) for i in str(num)]
    # print((list1))
    for i in range(len(list1)):
        if value == False:
            if (list1[i]) == 6:
                list1[i]  = 9
                value = True
        else:
            continue

    # print(list1)

    # print(str(list1))
    result = [str(i) for i in list1]
    final_result = ''.join(result)
    print((final_result))

print(number69(9669))




