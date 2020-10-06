def sol(s):
    ans = []
    start, end = 0, 1
    for i in range(len(s)):
        if end >= len(s):
            if end - start >= 3:
                ans.append([start, end-1])
            break
        if s[end] == s[start]:
            end += 1
        else:
            if end - start >= 3:
                ans.append([start, end-1])
            start, end = i+1, i+2

    return ans


print(sol('aaaabbb'))