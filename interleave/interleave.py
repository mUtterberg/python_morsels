

def interleave(list_1, list_2):
    for (item_1, item_2) in zip(list_1, list_2):
        yield item_1
        yield item_2


if __name__ == "__main__":
    pass
