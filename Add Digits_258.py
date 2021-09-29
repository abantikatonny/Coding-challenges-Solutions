def add_digit(num):
    while True:
        if num < 9:
            break
        else:
            value = str(num)
            print("vvvvv", value)
            sum = 0

            for i in value:
                print("iiii", i)
                # print(ele)
                sum += int(i)
                print("kkkk", sum)

            num = sum

    return num

print(add_digit(38))