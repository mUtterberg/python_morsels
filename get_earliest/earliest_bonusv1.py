def get_earliest(*inputs):
  all_dates = []
  for input in inputs:
    all_dates.append(tuple(input.split('/')))
  print(all_dates)
  earliest = all_dates[0]
  for date in all_dates:
    if date[2] < earliest[2]:
      earliest = date
    elif date[0] < earliest[0]:
      earliest = date
    elif date[1] < earliest[1]:
      earliest = date
  earliest = earliest[0] + '/' + earliest[1] + '/' + earliest[2]
  return earliest
