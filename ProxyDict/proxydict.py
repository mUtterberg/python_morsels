from collections.abc import Mapping


class ProxyDict(Mapping):
    def __init__(self, map_dict) -> None:
        self.elements = map_dict

    def __getitem__(self, k):
        return self.elements[k]

    def __iter__(self):
        for value in self.elements:
            yield value

    def __len__(self) -> int:
        return len(self.elements)

    def __repr__(self) -> str:
        return f'ProxyDict({self.elements})'


if __name__ == "__main__":
    seed_dict = {'first': 1, 'second': 2}
    proxy_dict = ProxyDict(seed_dict)
    print(proxy_dict)
