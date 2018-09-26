def compact(iterable):
    ''' Return new iterable with adjacent duplicate values removed. '''
    deduped = []
    latest = object()
    for item in iterable:
        if item != latest:
            deduped.append(item)
            latest = item
    return deduped