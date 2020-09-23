def sol(words):
    key_dict  = {}
    ans = []
    for c in 'qwertyuiop':
        key_dict[c] = 0
    for c in 'asdfghjkl':
        key_dict[c] = 1
    for c in 'zxcvbnm':
        key_dict[c] = 2
    for w in words:
        one_row = True
        for i in range(len(w)-1):
            if key_dict[w[i].lower()] != key_dict[w[i+1].lower()]:
                one_row = False
                break
        if one_row:
            ans.append(w)

    return ans


words = ["Hello", "Alaska", "Dad", "Peace"]
print(sol(words))



