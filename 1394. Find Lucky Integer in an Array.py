def sol(arr):

    occu = {}

    for n in arr:
        if n in occu:
            occu[n] += 1
        else:
            occu[n] = 1

    ans = -1

    for n in occu:
        if n==occu[n] and n > ans:
            ans = n

    return ans


print(sol([1,2,3,3]))