from dataclasses import dataclass


@dataclass
class Vector:
    """3-dimensional object"""
    __slots__ = ['x', 'y', 'z']
    x: int
    y: int
    z: int

    def __iter__(self):
        yield self.x
        yield self.y
        yield self.z
