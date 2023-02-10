def u(n):
    d = {}
    l = []
    for i in n:
        if(i not in d):
            d[i] = 1
        else:
            d[i] += 1

    for x, y in d.items():
        if(y == 1):
            l.append(x)
    return l