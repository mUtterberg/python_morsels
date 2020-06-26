import cmath
import decimal
import math


def is_perfect_square(number, **kwargs):
    if kwargs.get('complex'):
        sqrt = cmath.sqrt(number)
        if sqrt.real.is_integer() and sqrt.imag.is_integer():
            return True
        return False
    if number < 0:
        return False
    if not isinstance(number, (int, float, decimal.Decimal)):
        raise TypeError
    with decimal.localcontext() as c:
        c.prec = len(str(number)) * 2
        return int(decimal.Decimal(number).sqrt()) ** 2 == number


if __name__ == "__main__":
    is_perfect_square(13j, complex=True)
    for num in range(10):
        is_perfect_square(num)
