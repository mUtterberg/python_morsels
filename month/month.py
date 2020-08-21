import datetime
from typing import Any


class Month:

    __slots__ = ('month', 'year', 'first_day', 'last_day')
    def __init__(self, year: int, month: int) -> None:
        super(Month, self).__setattr__('month', month)
        super(Month, self).__setattr__('year', year)
        super(Month, self).__setattr__('first_day', datetime.date(year, month, 1))
        if month in [1, 3, 5, 7, 8, 10, 12]:
            last_day = 31
        elif month in [4, 6, 9, 11]:
            last_day = 30
        elif month == 2:
            last_day = 29
        else:
            raise ValueError
        try:
            super(Month, self).__setattr__('last_day', datetime.date(year, month, last_day))
        except ValueError:
            super(Month, self).__setattr__('last_day', datetime.date(year, month, last_day-1))

    @classmethod
    def from_date(cls, in_date):
        """Create Month from datetime.date"""
        out_month = cls(in_date.year, in_date.month)
        return out_month

    def __setattr__(self, name: str, value: Any) -> None:
        """Make immutable"""
        raise AttributeError("Months cannot be modified")

    def __delattr__(self, name: str) -> None:
        """Make immutable"""
        raise AttributeError("Months cannot be modified")

    def __hash__(self) -> int:
        return hash((self.year, self.month))

    def strftime(self, str_format: str):
        start_pos = 0
        fmt_pos = str_format.find('%', start_pos)
        start_pos = fmt_pos + 1
        fmt_one = str_format[start_pos]
        if fmt_one in ['Y', 'y', 'm', 'b', 'B']:
            format_one = self.first_day.strftime(f'%{fmt_one}')
        else:
            format_one = ''
        out_str = str_format[:fmt_pos] + format_one
        new_pos = str_format.find('%', fmt_pos+1)
        fmt_two = str_format[new_pos+1]
        if fmt_two in ['Y', 'y', 'm', 'b', 'B']:
            format_two = self.first_day.strftime(f'%{fmt_two}')
        else:
            format_two = ''
        out_str = out_str + str_format[fmt_pos+2:new_pos] + format_two
        return out_str

    def __repr__(self) -> str:
        return f'Month({self.year}, {self.month:0o})'

    def __str__(self) -> str:
        return f'{self.year}-{self.month:02d}'

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, Month):
            return False
        try:
            m_eq = self.month == o.month
            y_eq = self.year == o.year
            return m_eq and y_eq
        except:
            return False

    def __lt__(self, o: object) -> bool:
        if not isinstance(o, Month):
            raise TypeError
        try:
            y_lt = self.year < o.year
            if y_lt:
                return True
            y_lt = self.year <= o.year
            m_lt = self.month < o.month
            return m_lt and y_lt
        except:
            raise TypeError

    def __le__(self, o: object) -> bool:
        if isinstance(o, (datetime.date, datetime.datetime)):
            raise TypeError
        try:
            y_lte = self.year <= o.year
            if y_lte:
                return True
            m_lte = self.month <= o.month
            return m_lte and y_lte
        except:
            raise TypeError

    def __gt__(self, o: object) -> bool:
        if isinstance(o, (datetime.date, datetime.datetime)):
            raise TypeError
        try:
            y_gt = self.year > o.year
            if y_gt:
                return True
            y_gt = self.year >= o.year
            m_gt = self.month > o.month
            return m_gt and y_gt
        except:
            raise TypeError

    def __ge__(self, o: object) -> bool:
        if isinstance(o, (datetime.date, datetime.datetime)):
            raise TypeError
        try:
            y_gte = self.year >= o.year
            if y_gte:
                return True
            m_gte = self.month >= o.month
            return m_gte and y_gte
        except:
            raise TypeError


if __name__ == "__main__":
    demo = Month(1999, 2)
    print(demo)
    date_time = datetime.date(1999, 2, 1)
    print(demo == date_time)
    print(Month(1900, 2))
