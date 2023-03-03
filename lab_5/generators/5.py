def seq(n):
    i = n
    while(i >= 0):
        yield i
        i -= 1
n = int(input())
for i in seq(n):
    print(i)