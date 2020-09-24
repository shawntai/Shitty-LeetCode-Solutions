def sol(nums):
    if len(nums) == 0:
        return 0
    ans = 0
    curr = 1
    last_num = nums[0]
    for i in range(1,len(nums)):
        if nums[i] > last_num:
            curr += 1
        else:
            if curr > ans:
                ans = curr
            curr = 1
        last_num = nums[i]
    if curr > ans:
        ans = curr
    return ans


print(sol([1,3,5,4,2,3,4,5]))