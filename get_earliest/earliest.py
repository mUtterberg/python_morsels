def get_earliest(*dates):
    ''' Return earliest of given MM/DD/YYYY-formatted date strings '''
    def date_key(date):
        (month, day, year) = date.split('/')
        return (year, month, day)
    return min(dates, key=date_key)
