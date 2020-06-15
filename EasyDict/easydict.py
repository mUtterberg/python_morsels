

class EasyDict:
    def __init__(self, easy_dict={}):
        for item in easy_dict:
            self.__setattr__(item, easy_dict[item])

    def __getitem__(self, attr):
        return self.__getattribute__(attr)

    def __setitem__(self, attr, val):
        return self.__setattr__(attr, val)


if __name__ == "__main__":
    test_dict = EasyDict({'first': 1, 'final':7})
    print(test_dict)
    print(test_dict['first'])
