def sol(n):

    def combination(a, b):
        ans = 1
        if b > a//2+1:
            b = a-b
        for i in range(1, b + 1):
            ans *= (i + a - b)
        for i in range(1, b + 1):
            ans /= i
        return int(ans)

    ans = 0
    no2 = 0
    while no2*2 <= n:
        ans += combination(n-no2, no2)
        no2 += 1

    return ans


def sol2(n):
    if n<=2:
        return n
    second2last = 1
    last = 2
    for i in range(2,n):
        second2last, last = last, second2last+last
    return last


for i in range(1,10):
    print(sol2(i))