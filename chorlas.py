i = 56482685

while True:
    num = i

    while not num == 1:
        if num%2 == 0:
            num = num/2
        else:
            num = num*3+1
        if num == 1:
            res = True
            i += 1
        else:
            res = False
    print("%d:" %i, res)
    