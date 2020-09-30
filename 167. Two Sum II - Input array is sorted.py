def sol(numbers, target):
    for i in range(len(numbers)):
        if i < len(numbers) and not (i>0 and numbers[i]==numbers[i-1]):
            for j in range(i+1,len(numbers)):
                if not (j > i+1 and numbers[j]==numbers[j-1]):
                    if numbers[i] + numbers[j] == target:
                        return [i+1, j+1]
                    elif numbers[i] + numbers[j] > target:
                        numbers = numbers[:j]
                        break


def sol2(numbers, target):
    left, right = 0, len(numbers)-1
    while True:
        if numbers[left]+numbers[right]==target:
            return [left+1, right+1]
        elif numbers[left]+numbers[right] > target:
            right -= 1
        else:
            left +=1


nums = []
for i in range(30):
    nums.append(0)
nums += [2,3]
for i in range(30):
    nums.append(9)

targ = 5
print(sol2(nums, targ))