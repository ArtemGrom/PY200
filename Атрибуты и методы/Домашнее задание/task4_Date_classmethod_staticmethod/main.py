class Date:
    """Класс для работы с датами"""
    DAY_OF_MONTH = (
        (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),  # обычный год
        (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)  # високосный
    )

    __slots__ = ('day', 'month', 'year')

    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

        self.is_valid_date(self.day, self.month, self.year)

    @staticmethod
    def is_leap_year(year: int) -> bool:
        """Проверяет, является ли год високосным"""
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            return True
        return False

    def get_max_day(self, month: int, year: int):
        """Возвращает максимальное количество дней в месяце для указанного года"""
        if self.is_leap_year(year):
            return self.__class__.DAY_OF_MONTH[1][month - 1]
        return self.__class__.DAY_OF_MONTH[0][month - 1]

    @staticmethod
    def is_valid_date(day: int, month: int, year: int):
        """Проверяет, является ли дата корректной"""
        if not isinstance(day, int) and not isinstance(month, int) and not isinstance(year, int):
            raise TypeError
        if not 0 < day < 32 or not 0 < month < 12 or year < 0:
            raise IndexError


if __name__ == "__main__":
    data_1 = Date(15, 2, 1589)
    data_2 = Date(3, 10, 1666)
    data_3 = Date(31, 5, 1589)
    # data_4 = Date(10, 5, -300)
    # data_5 = Date(31, "5", 1589)
    # data_6 = Date(35, 5, 1589)
    # data_7 = Date(12, 15, 1589)
    print(data_1.get_max_day(2, 1633))


