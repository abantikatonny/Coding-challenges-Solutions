def restoreString(s, indices):
    array_s = list(s)
    # print(array_s)
    new_list = [0 for i in range(len(s))]
    for i in range(len(s)):
        new_list[indices[i]] = s[i]

    return ''.join(new_list)



    # print(array_s)

print(restoreString("aiohn", [3,1,4,2,0]))
