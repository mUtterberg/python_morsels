def get_earliest(*dates):
    ''' Return earliest of given MM/DD/YYYY-formatted date strings '''
    def date_key(date):
        (m, d, y) = date.split('/')
        return (y, m, d)
    return min(dates, key=date_key)
    