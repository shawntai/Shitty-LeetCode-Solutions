def sol(s):

    occu = {}

    for c in s:
        if c in occu:
            occu[c] += 1
        else:
            occu[c] = 1

    ans = 0
    odd_occu = False

    for o in occu:
        if occu[o] % 2 == 0:
            ans += occu[o]
        else:
            ans += occu[o] - 1
            if not odd_occu:
                odd_occu = True

    if odd_occu:
        ans += 1

    return ans


print(sol("bb"))