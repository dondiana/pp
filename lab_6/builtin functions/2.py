def countLower(st):
    cnt = 0
    for i in st:
        if i.islower():
            cnt += 1
    return cnt

def countUpper(st):
    cnt = 0
    for i in st:
        if i.isupper():
            cnt += 1
    return cnt

st = input()
print(f'Number of uppercase: {countUpper(st)}')
print(f'Number of lowercase: {countLower(st)}')