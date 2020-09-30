def sol(arr):
    arr.sort()
    min_diff = 999999
    for i in range(1, len(arr)):
        if arr[i]-arr[i-1] < min_diff:
            min_diff = arr[i]-arr[i-1]
    return [(arr[i-1], arr[i]) for i in range(1, len(arr)) if arr[i]-arr[i-1] == min_diff]


a = [4,2,1,3]
print(sol(a))