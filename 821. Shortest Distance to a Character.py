def sol(S, C):
    INF = 99999
    ans = [INF for _ in range(len(S))]
    for i in range(len(S)):
        if S[i] == C:
            ans[i] = 0
            # left
            for j in range(i-1,-1,-1):
                if ans[i] + (i-j) < ans[j]:
                    ans[j] = ans[i] + (i-j)
                else:
                    break
            # right
            for j in range(i+1, len(S)):
                if ans[i] + (j-i) < ans[j]:
                    ans[j] = ans[i] + (j-i)
                else:
                    break
    return ans


S = "loveleetcode"
C = 'e'
print(sol(S, C))