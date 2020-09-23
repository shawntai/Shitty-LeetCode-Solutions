def sol(A,K):
    #sum = 0
    K_left = K
    A.sort()
    for i in range(K):
        if A[i] < 0:
            A[i] *= -1
            K_left -= 1
        else:
            break
    if K_left % 2 == 1:
        A.sort()
        A[0] *= -1
    return sum(A)

A = [4,2,3]
print(sol(A,1))