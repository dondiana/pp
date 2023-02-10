def comb(n: list):
    ans = ""
    for i in n:
        if i == 0 or i == 7:
            ans+=str(i)
    return True if ans.find("007") >=0 else False