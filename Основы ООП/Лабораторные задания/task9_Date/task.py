# TODO class Date
class Date:
    """Init class Date"""
    def __init__(self, day: int, month: int, year: int):
        if not isinstance(day, int):
            raise TypeError
        if not isinstance(month, int):
            raise TypeError
        if not isinstance(year, int):
            raise TypeError

        self.day = day
        self.month = month
        self.year = year

    def __str__(self) -> str:
        if self.day / 10 < 1 <= self.month / 10:
            return f"0{str(self.day)}/{str(self.month)}/{str(self.year)}"
        elif self.month / 10 < 1 <= self.day / 10:
            return f"{str(self.day)}/0{str(self.month)}/{str(self.year)}"
        elif self.day / 10 <= 1 and self.month / 10 <= 1:
            return f"0{str(self.day)}/{str(self.month)}/{str(self.year)}"

        return f"{str(self.day)}/{str(self.month)}/{self.year}"

    def __repr__(self) -> str:
        return f"Date({self.day}, {self.month}, {self.year})"


if __name__ == '__main__':
    date_1 = Date(10, 12, 1985)
    # date_2 = Date("asd", 2, 4)
    date_3 = Date(4, 10, 1330)
    date_4 = Date(10, 5, 1000)

    print(date_1)
    print(date_3)
    print(date_4)
