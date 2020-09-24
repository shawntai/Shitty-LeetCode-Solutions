def sol(nums):
    occurrances = {}
    for n in nums:
        if n in occurrances:
            occurrances[n] += 1
        else:
            occurrances[n] = 1
    ans = 0
    for o in occurrances:
        ans += occurrances[o]*(occurrances[o]-1)/2
    return int(ans)


nums = [1,1,1,1]
print(sol(nums))