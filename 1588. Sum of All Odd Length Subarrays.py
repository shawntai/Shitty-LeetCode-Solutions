def sol(arr):
    arr_sum = sum(arr)
    subset_size = 1
    ans = 0
    while subset_size <= len(arr):
        ans += arr_sum*subset_size
        for i in range(subset_size):
            ans -= arr[i]*(subset_size-i-1)
            ans -= arr[len(arr)-1-i]*(subset_size-i-1)
        subset_size += 2
    return ans


a = [1,4,2,5,3]
print(sol(a))