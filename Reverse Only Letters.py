def reverseOnlyLetters(s):
    s = list(s)
    new_list = []
    for i in range(len(s)):
        if s[i].isalpha():
            new_list.append(s[i])

    new_list.reverse()
    # print(new_list)
    z = 0
    for i in range(len(s)):
        if s[i].isalpha():
            s[i] = new_list[z]
            z = z +1
    print("".join(s))




        # print(new_list)

print(reverseOnlyLetters("a/-cd"))