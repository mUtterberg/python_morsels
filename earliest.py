def get_earliest(input1, input2):
  earliest = ''
  array1 = input1.split('/')
  array2 = input2.split('/')
  if array1[2] < input2[2]:
    earliest = input1
  elif array2[2] < input1[2]:
    earliest = input2
  elif array1[0] < input2[0]:
    earliest = input1
  elif array2[0] < input1[0]:
    earliest = input2
  elif array1[1] < input1[1]:
    earliest = input1
  elif array2[1] < input1[1]:
    earliest = input2
  else:
    earliest = input1
  return earliest
