def sol(arr, k):
    sum = 0
    i = 0
    #for i in range(len(arr)):
    while i < len(arr):
        arr[i] %= k
        sum += arr[i]
        if arr[i] == 0:
            del arr[i]
        else:
            i += 1
    if sum % k != 0:
        return False
    if not arr:
        return True
    arr.sort()
    for i in range(int(len(arr)/2)+1):
        if (arr[i]+arr[len(arr)-i-1]) % k != 0:
            print(arr[i])
            print(arr[len(arr)-i-1])
            return False
    return True


def sol2(arr, k):
    freq = [0] * k
    for n in arr:
        freq[n%k] += 1
    if freq[0] % 2 != 0:
        return False
    for i in range(1,int(k/2)+1):
        if i*2==k:
            return freq[i]%2==0
        if freq[i] != freq[k-i]:
            return False
    return True


def sol3(arr, k):
    freq = {}
    for n in arr:
        if str(n%k) in freq:
            freq[str(n%k)] += 1
        else:
            freq[str(n%k)] = 1
    if '0' in freq and freq['0']%2 != 0:
        num = freq['0']
        return False
    for i in freq:
        if i!='0' and int(i) <= k/2 and freq[i] != freq[str(k-int(i))]:
            return False
    return True


def sol4(arr, k):
    freq = {}
    for n in arr:
        if n % k in freq:
            freq[n % k] += 1
        else:
            freq[n % k] = 1
    if 0 in freq and freq[0] % 2 != 0:
        return False
    for i in freq:
        if i <= k / 2 and (k - i not in freq or freq[i] != freq[k - i]):
            return False
    return True

arr = [3,8,17,2,5,6]
print(sol3(arr,10))