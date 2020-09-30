def sol(A):
    import heapq
    for i in range(len(A)):
        A[i] = -A[i]
    heapq.heapify(A)
    a = -heapq.heappop(A)
    b = -heapq.heappop(A)
    c = -heapq.heappop(A)
    if a < b+c:
        return a+b+c
    else:
        while len(A) != 0:
            a, b, c = b, c, -heapq.heappop(A)
            if a < b + c:
                return a+b+c
    return 0


A = [3,2,3,4]
print(sol(A))