def compact(iterable):
    try:
        latest = iterable[0]
        sender = [latest]
    except:
        latest = None
        sender = []
    for next_ in range(1, len(iterable)):
        if iterable[next_] != latest:
            sender.append(iterable[next_])
        latest = iterable[next_]
    return sender
