def sol(stones):
    import heapq
    for i in range(len(stones)):
        stones[i] *= -1
    heapq.heapify(stones)
    while len(stones) > 1:
        result = heapq.heappop(stones) - heapq.heappop(stones)
        if result < 0:
            heapq.heappush(stones, result)
    return 0 if len(stones) == 0 else -stones[0]


def sol2(stones): # slight amendment
    import heapq
    stones = [-s for s in stones]
    heapq.heapify(stones)
    while len(stones) > 1 and stones[0] != 0:
        heapq.heappush(stones, heapq.heappop(stones) - heapq.heappop(stones))
    return 0 if len(stones) == 0 else -stones[0]


stns = [2,2]
print(sol2(stns))