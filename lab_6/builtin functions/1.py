def multiply(*arr):
    r = 1
    for i in arr:
        r *= i
    return r
arr = list(map(int, input().split()))
print(multiply(*arr))
