# https://py.checkio.org/mission/unlucky-days/
import datetime


def checkio(year):
    return sum(datetime.date(year, month, 13).weekday() == 4 for month in range(1, 13))


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(2015) == 3, "First - 2015"
    assert checkio(1986) == 1, "Second - 1986"
