def get_earliest(input1, input2):
    ''' Return earliest of two dates (MM/DD/YYYY) '''
    earliest = ''
    array1 = input1.split('/')
    array2 = input2.split('/')
    if array1[2] < array2[2]:
        earliest = input1
    elif array2[2] < array1[2]:
        earliest = input2
    elif array1[0] < array2[0]:
        earliest = input1
    elif array2[0] < array1[0]:
        earliest = input2
    elif array1[1] < array1[1]:
        earliest = input1
    elif array2[1] < array1[1]:
        earliest = input2
    else:
        earliest = input1
    return earliest
