def lengthOfLastWord(s):
    left = -1
    right = len(s)
    for i in range(len(s)-1, -1, -1):
        if s[i] == ' ':
            if right - i <= 1:
                right = i
            else:
                left = i
                break
    return right-left-1


print(lengthOfLastWord('   Hello Wor ld  '))

def sol2(s):
    ans = 0
    for i in range(len(s)-1,-1,-1):
        if s[i] == ' ':
            if ans > 0:
                break
        else:
            ans += 1
    return ans


print(sol2('   Hello Wor ld  '))
