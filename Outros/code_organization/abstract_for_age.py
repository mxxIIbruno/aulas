from datetime import datetime
from abc import ABC, abstractmethod
import locale


class ABCForAge(ABC):
    locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')
    _date = datetime.now()

    def __init__(self):
        self._birth_date = datetime(
            self.set_year(),
            self.set_month(),
            self.set_day()
        )

    @property
    def date(self):
        return self._date

    @property
    def birth_date(self):
        return self._birth_date

    @abstractmethod
    def message(self): ...

    @abstractmethod
    def set_year(self) -> int: ...

    @abstractmethod
    def set_month(self) -> int: ...

    @abstractmethod
    def set_day(self) -> int: ...

    @abstractmethod
    def display_solution(self): ...
