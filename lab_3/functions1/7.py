def has_33(n):
    for i in range(len(n) - 1):
        if(n[i] == n[i+1] == 3):
            return True
    return False