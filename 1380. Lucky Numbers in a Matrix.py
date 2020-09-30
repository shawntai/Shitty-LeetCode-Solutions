def sol(matrix):

    min_arr = []
    col_max = []
    for r in range(len(matrix)):
        row_min = min(matrix[r])
        for c in range(len(matrix[0])):
            if r==0:
                col_max.append(matrix[r][c])
            else:
                if col_max[c] < matrix[r][c]:
                    col_max[c] = matrix[r][c]
            if matrix[r][c] == row_min:
                min_arr.append((r, c))

    return [matrix[coor[0]][coor[1]] for coor in min_arr if matrix[coor[0]][coor[1]] == col_max[coor[1]]]


mat = [[36376,85652,21002,4510],
       [68246,64237,42962,9974],
       [32768,97721,47338,5841],
       [55103,18179,79062,46542]]
print(sol(mat))