def sol(nums):
    import math
    return len([num for num in nums if int(math.log(num, 10)+0.0000000001)%2==1])


def sol2(nums):
    ans = 0
    for n in nums:
        if (9<n and n<100) or (999<n and n < 10000) or n == 100000:
            ans += 1
    return ans


import math
#print(int(2.9))

print(sol([1000]))

print(math.log(1000,10))
