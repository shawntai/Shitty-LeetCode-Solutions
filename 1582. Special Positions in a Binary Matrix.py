def sol(mat):
    row_num_arr = []
    col_num_arr = []
    ans = []
    for r in range(len(mat)):
        for c in range(len(mat[0])):
            if mat[r][c] == 1:

                if r in row_num_arr or c in col_num_arr:
                    if r not in row_num_arr:
                        row_num_arr.append(r)
                    if c not in col_num_arr:
                        col_num_arr.append(c)
                    i = 0
                    while i < len(ans):
                        coor = ans[i]
                        if coor[0] == r or coor[1] == c:
                            ans.remove(coor)
                        else:
                            i+=1

                if r not in row_num_arr and c not in col_num_arr:
                    ans.append((r,c))
                    row_num_arr.append(r)
                    col_num_arr.append(c)

    return len(ans)


mat = [[0,0,0,0,1,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,1,0,0],
       [0,0,0,0,0,0,0,0,1,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,1,0],
       [0,0,0,0,0,0,0,0,0,1,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,1,0,0,1,0]]

print(sol(mat))