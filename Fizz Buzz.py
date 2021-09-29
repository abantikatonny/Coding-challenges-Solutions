def fizzBuzz(n):
    list_1 = []
    
    for i in range(1, n+1):
        if i > 0:
            list_1.append(i)
    answer = [str(i) for i in list_1]
    # print(answer)

    for j in range(len(answer)):
        print(j)
        if (j+1) % 3 == 0 and (j+1) % 5 == 0:
            answer[j] = "FizzBuzz"
        elif (j+1) % 3 != 0 and (j+1) % 5 == 0:
            answer[j] = "Buzz"
        elif (j+1) % 3 == 0 and (j+1) % 5 != 0:
            answer[j] = "Fizz"

    print(answer)

        #     print(list_1)

        # print(list_1)


print(fizzBuzz(5))