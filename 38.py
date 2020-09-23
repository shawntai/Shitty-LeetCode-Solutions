def count_and_say(n):
    ans = ''
    if n == 1:
        return '1'
    prev = count_and_say(n-1)
    curr_streak = 1
    curr = ''
    for i in range(len(prev)+1):
        if i == len(prev) or prev[i] != curr:
            if curr != '': ans += (str(curr_streak) + curr)
            curr_streak = 1
            if i<len(prev): curr = prev[i]
        else:
            curr_streak += 1
    return ans


for i in range(1,6):
    print(count_and_say(i))

