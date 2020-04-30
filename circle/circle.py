from math import pi


class Circle():

    def __init__(self, radius=1):
        self.radius = radius
        self.diameter = radius * 2

    def __repr__(self):
        if self.radius % 1 == 0:
           return f"Circle({int(self.radius)})"
        else:
            return f"Circle({self.radius})"

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius):
        if radius >= 0:
            self.__radius = radius
        else:
            raise ValueError('Radius cannot be negative')

    @property
    def diameter(self):
        return self.__radius * 2

    @diameter.setter
    def diameter(self, diameter):
        if diameter >= 0:
            self.__diameter = diameter
            self.radius = diameter / 2
        else:
            raise ValueError('Diameter cannot be negative')

    @property
    def area(self):
        return self.__radius ** 2 * pi


if __name__ == "__main__":
    d = Circle()
    print(f"Testing {d}")
    print(d.radius, d.diameter, d.area)

    c = Circle(5)
    print(f"Testing {c}")
    print(c.radius, c.diameter, c.area)

    print(f"Updating {c}")
    c.radius = 1
    print(c.radius, c.diameter, c.area)

    print(f"Updating diameter for {c} to 10")
    c.diameter = 10
    print(c.radius, c.diameter, c.area)

    try:
        c.area = 5
        print("FAILURE: expected an AttributeError on c.area = 5")
    except AttributeError as attr_e:
        print(f"SUCCESS: raised expected error on c.area = 5! {attr_e}")

    try:
        d.radius = -2
        print("FAILURE: expected a ValueError on d.radius = -2")
    except ValueError as val_e:
        print(f"SUCCESS: raised expected ValueError on d.radius = -2! {val_e}")

    try:
        c.diameter = -2
        print("FAILURE: expected a ValueError on c.diameter = -2")
    except ValueError as val_e:
        print(f"SUCCESS: raised expected ValueError on c.diameter = -2! {val_e}")

    f = Circle(1.5)
    print(f"Testing string formatting of float radius: {f}")
    print(f.radius, f.diameter, f.area)
