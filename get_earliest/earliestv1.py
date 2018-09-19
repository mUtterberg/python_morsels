def get_earliest(input1, input2):
  ''' Return earliest of two dates (MM/DD/YYYY) '''
  month1, day1, year1 = input1.split('/')
  month2, day2, year2 = input2.split('/')
  if (year1, month1, day1) < (year2, month2, day2):
    return input1
  else:
    return input2