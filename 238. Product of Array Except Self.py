def sol(nums):
    ans = [1 for _ in range(len(nums))]
    left, right = 1, 1
    for i in range(1,len(nums)):
        ans[i] *= (nums[i-1]*left)
        left *= nums[i-1]
    for i in range(len(nums)-2,-1,-1):
        ans[i] *= (nums[i+1]*right)
        right *= nums[i+1]
    return ans


nums = [1,2,3,4]
print(sol(nums))