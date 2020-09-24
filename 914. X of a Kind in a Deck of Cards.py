def sol(deck):
    factors = []
    size = len(deck)
    if size==0:
        return False
    for i in range(2,int(size**0.5)+2):
        if size%i==0:
            factors.append(i)
    if len(factors)==0:
        return False
    occu = {}
    for n in deck:
        if n in occu:
            occu[n] += 1
        else:
            occu[n] = 1
    for f in factors:
        solved = True
        for n in occu:
            if occu[n] % f != 0 and occu[n] % f != 0:
                solved = False
                break
        if solved:
            return True
    return False


deck = [0,0,0,0,0,1,1,1,1,1]
print(sol(deck))