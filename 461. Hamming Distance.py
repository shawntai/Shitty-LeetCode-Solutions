def sol(x, y):
    x = list(bin(x)[2:])
    y = list(bin(y)[2:])
    if len(x) > len(y):
        y = ['0' for _ in range(len(x)-len(y))] + y
    elif len(x) < len(y):
        x = ['0' for _ in range(len(y) - len(x))] + x
    ans = 0
    for d in range(len(x)):
        if x[d] != y[d]:
            ans += 1
    return ans


def sol2(x, y):
    x = bin(x)[2:]
    y = bin(y)[2:]
    if len(x) > len(y):
        y = '0'*(len(x) - len(y)) + y
    elif len(x) < len(y):
        x = '0' * (len(y) - len(x)) + x
    ans = 0
    return sum(x[i]!=y[i] for i in range(len(x)))


print(sol2(1,4))