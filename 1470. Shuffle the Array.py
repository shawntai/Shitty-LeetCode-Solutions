def sol(nums: list, n: int) -> list:
    for i in range(0, 2*n, 2):
        nums.insert(i+1, nums[i+n])

    return nums[:2*n]


def sol2(nums, n):
    ans = []
    for i in range(n):
        ans.append(nums[i])
        ans.append(nums[i+n])
    return ans


arr = [2, 5, 1, 3, 4, 7]
print(sol2(arr, int(len(arr)/2)))