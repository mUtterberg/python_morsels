def add(matrix1, matrix2):
    '''
    Takes two lists of lists.
    Returns one element-wise summed list of lists.
    '''
    sum = []
    i = 0
    for row in matrix1:
        working_row = []
        for j in range(len(matrix1[i])):
            working_row.append(matrix1[i][j] + matrix2[i][j])
        sum.append(working_row)
        i += 1
    return sum
