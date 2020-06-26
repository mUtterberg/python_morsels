

class EasyDict:
    def __init__(self, easy_dict={}, normalize=False, **kwargs):
        self._normalize = normalize
        for key, value in easy_dict.items():
            self[key] = value
        for key, value in kwargs.items():
            self[key] = value

    def __getitem__(self, attr):
        return getattr(self, self.normalized(attr))

    def __setitem__(self, attr, val):
        setattr(self, self.normalized(attr), val)
    
    def __eq__(self, easy_dict):
        return self.__dict__ == easy_dict.__dict__

    def normalized(self, key):
        if self._normalize:
            return key.replace(' ', '_')
        return key
    
    def get(self, attr, default_value=None):
        try:
            return getattr(self, self.normalized(attr))
        except AttributeError:
            return default_value


if __name__ == "__main__":
    test_dict = EasyDict({'first': 1, 'final':7})
    print(test_dict)
    print(test_dict['first'])
