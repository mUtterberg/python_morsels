from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
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

    def __add__(self, o: object):
        try:
            return Vector(self.x + o.x, self.y + o.y, self.z + o.z)
        except AttributeError:
            raise TypeError(f'Unable to add object of type {type(o)}')

    def __sub__(self, o: object):
        try:
            return Vector(self.x - o.x, self.y - o.y, self.z - o.z)
        except AttributeError:
            raise TypeError(f'Unable to subtract object of type {type(o)}')

    def __mul__(self, o: object):
        if isinstance(o, (int, float, Decimal)):
            return Vector(self.x * o, self.y * o, self.z * o)
        raise TypeError(f'Multiplication by type {type(o)} not yet supported')

    def __rmul__(self, o: object):
        if isinstance(o, (int, float, Decimal)):
            return Vector(self.x * o, self.y * o, self.z * o)
        raise TypeError(f'Multiplication by type {type(o)} not yet supported')

    def __truediv__(self, o: object):
        if isinstance(o, (int, float, Decimal)) and (o != 0):
            return Vector(self.x / o, self.y / o, self.z / o)
        raise TypeError(f'Division by type {type(o)} not yet supported')

    def __rtruediv__(self, o: object):
        if isinstance(o, (int, float, Decimal)) and (o != 0):
            return Vector(self.x / o, self.y / o, self.z / o)
        raise TypeError(f'Division by type {type(o)} not yet supported')
