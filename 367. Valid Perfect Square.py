def sol(num):
    perfect_square = []
    for i in range(1,46341):
        perfect_square.append(i*i)
    return num in perfect_square


n = 1776

print(sol(979*979))