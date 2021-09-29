def addBinary(a, b):

    p = int(a)
    q = int(b)

    if p == 0 and q == 0:
        return "0"

    s = ""
    c = 0
    if p!= 0 or q!=0:
        s += (p % 10 + q % 10 + c)%10
        c  = (p % 10 + q % 10+c) //2
        p = p//10
        q = q//10

    print(s)

print(addBinary(1010, 1011))


