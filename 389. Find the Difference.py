def sol(s, t):
    s = list(s)
    t = list(t)
    s.sort()
    t.sort()

    for i in range(len(t)):
        if i < len(s) and s[i] != t[i]:
            return t[i]
    return t[len(t)-1]

print(sol('abcd', 'abcde'))