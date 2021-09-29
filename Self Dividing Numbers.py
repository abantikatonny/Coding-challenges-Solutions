
def selfdividingnumbers(left, right):
    list1 = []
    value = 0

    for i in range(left, right + 1):
        f = i
        while f > 0:
            remainder = f % 10
            if remainder != 0 and i % remainder == 0:
                value = 1
                f = f // 10
            else:
                value = 0
                break

        if value == 1:
            list1.append(i)
    return list1

print(selfdividingnumbers(2, 10))

