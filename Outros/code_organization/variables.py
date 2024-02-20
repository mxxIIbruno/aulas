from datetime import datetime
from dateutil.relativedelta import relativedelta


class Variables:
    _birth_year = None
    _birth_month = None
    _birth_day = None

    _month_day = None
    _age = None

    @property
    def birth_year(self):
        return self._birth_year

    @birth_year.setter
    def birth_year(self, value: int):
        try:
            self._birth_year = int(value)
            if not self._birth_year <= datetime.now().year:
                self._birth_year = None
        except ValueError:
            self._birth_year = None

    @property
    def birth_month(self):
        return self._birth_month

    @birth_month.setter
    def birth_month(self, value: int):
        try:
            self._birth_month = int(value)
            if not 1 <= self._birth_month <= 12:
                self._birth_month = None
        except ValueError:
            self._birth_month = None

    @property
    def birth_day(self):
        return self._birth_day

    @birth_day.setter
    def birth_day(self, value):
        self._month_day = self.get_month_day()
        try:
            self._birth_day = int(value)
            if not 1 <= self._birth_day <= self._month_day:
                self._birth_day = None
        except ValueError:
            self._birth_day = None

    def get_month_day(self):
        if self._birth_month is None or self._birth_year is None:
            return

        february = 29 if self._is_leap_year(self._birth_year) else 28
        list_months = (
            31, february, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
        )

        return list_months[self._birth_month - 1]

    @staticmethod
    def _is_leap_year(year: int):
        return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

    @property
    def month_day(self):
        return self._month_day

    @property
    def age(self):
        birth_date = datetime(
            self._birth_year,
            self._birth_month,
            self._birth_day
        )
        self._age = relativedelta(
            datetime.now(), birth_date
        )
        return self._age
