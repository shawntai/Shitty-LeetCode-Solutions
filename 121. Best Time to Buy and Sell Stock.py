def sol(prices):
    ans = 0
    for i in range(len(prices)-1):
        if max(prices[i+1:]) - prices[i] > ans:
            ans = max(prices[i+1:]) - prices[i]
    return ans

def sol2(prices):
    maxOfSuffixArr = []
    for i in range(len(prices)-2,-1,-1):
        if i == len(prices)-2 or prices[i+1] > maxOfSuffixArr[0]:
            maxOfSuffixArr.insert(0,prices[i+1])
        else:
            maxOfSuffixArr.insert(0,maxOfSuffixArr[0])
    ans = 0
    for i in range(len(prices)-1):
        if maxOfSuffixArr[i]-prices[i]>ans:
            ans = maxOfSuffixArr[i] - prices[i]
    return ans


print(sol2([7,1,5,3,6,4]))

