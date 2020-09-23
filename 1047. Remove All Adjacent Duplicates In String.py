def sol(S):
    stack = []
    for c in S:
        if len(stack)==0 or c != stack[len(stack)-1]:
            stack.append(c)
        else:
            stack.pop()
    return ''.join(stack)


def sol2(S):
    stack = ''
    for c in S:
        if len(stack) == 0 or c != stack[len(stack) - 1]:
            stack += c
        else:
            stack = stack[:len(stack)-1]
    return stack


print(sol2('abbaca'))