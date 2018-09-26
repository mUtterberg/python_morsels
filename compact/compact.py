def compact(iterable):
    ''' Return new iterable with adjacent duplicate values removed. '''
    latest = object()
    for item in iterable:
        if item != latest:
            yield item
            latest = item