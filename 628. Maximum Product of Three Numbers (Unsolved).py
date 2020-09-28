def sol(nums):
    first_i = 0
    second_i = 1
    if nums[0] < nums[1]:
        first_i, second_i = second_i, first_i
    for i in range(3,len(nums)):
        if abs(nums[i]) > nums[first_i]:
            first_i, second_i = i, first_i
        elif abs(nums[i]) > nums[second_i]:
            second_i = i
    if nums[first_i]*nums[second_i] > 0:
        third_i = -999999
        for i in range(len(nums)):
            if nums[i] > third_i and i != first_i and i != second_i:
                third_i = i
    else:
        print('idk')
    return nums[first_i]*nums[second_i]*nums[third_i]


print(sol([-1,-2,-3,-4,60]))