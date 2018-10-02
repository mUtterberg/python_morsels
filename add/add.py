def add(matrix1, matrix2):
    '''
    Takes two lists of lists.
    Returns one element-wise summed list of lists.
    '''
    shape = matrix1
    sum = []
    j = 0
    for row in matrix1:
        working_row = []
        for i in range(len(matrix1[j])):
            working_row.append(matrix1[j][i] + matrix2[j][i])
        sum.append(working_row)
        j += 1
    return sum