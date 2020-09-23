def sol(s):
    arr = s.split()
    row = 0 # 3
    for str in arr:
        if len(str) > row:
            row = len(str)

    col = len(arr)       # 6
    ans = ["" for _ in range(row)]

    for c in range(col):
        for r in range(row):
            if r < len(arr[c]):
                ans[r] += arr[c][r]
            else:
                ans[r] += ' '

    actual_ans = []
    for str in ans:
        n_trail = 0
        for i in range(len(str)-1, -1, -1):
            if str[i] == ' ':
                n_trail += 1
            else:
                break
        actual_ans.append(str[:len(str)-n_trail])

    return actual_ans


print(sol("TO BE OR NOT TO BE"))