def sol(n: int) -> bool:
    visited = []
    def solve(n: int, visited: list) -> bool:
        if n==1:
            return True
        if n not in visited:
            visited.append(n)
            next = 0
            while n > 0:
                next += (n%10)**2
                n = n//10
            return solve(next, visited)
        return False
    return solve(n, visited)


def sol2(n):
    visited = []
    while n not in visited:
        if n==1:
            return True
        visited.append(n)
        next = 0
        while n > 0:
            next += (n % 10) ** 2
            n = n // 10
        n = next
    return False

print(sol2(191))