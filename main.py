def znajdz(s, p):
    n = len(s)
    m = len(p)
    ans = []
    for i in range(n):
        if s[i: i + m] == p:
            ans.append(i)
    return ans

print(znajdz("ababaabaababaabaaabaabaa", "abaaba"))
