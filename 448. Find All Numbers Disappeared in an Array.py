def sol(nums):
    arr = [0 for _ in range(len(nums))]
    for n in nums:
        if arr[n-1] == 0:
            arr[n-1] += 1
    return [i+1 for i in range(len(arr)) if arr[i]==0]


print(sol([4,3,2,7,8,2,3,1]))