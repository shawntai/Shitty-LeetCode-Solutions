def sol(folder):
    isSub = [False for _ in range(len(folder))]
    for i in range(len(folder)):
        if not isSub[i]:
            f = folder[i].split('/')
            f = f[len(f)-1]
            for j in range(len(folder)):
                if i != j and f in folder[j].split('/'):
                    isSub[j] = True
    ans = []
    for i in range(len(folder)):
        if not isSub[i]:
            ans.append(folder[i])
    return ans


print(sol(["/a/b/c","/a/b/ca","/a/b/d"]))
