# https://py.checkio.org/mission/the-most-frequent-weekdays/
from datetime import date


def most_frequent_days(year):

    f, l = date(year, 1, 1), date(year, 12, 31)

    if f.weekday() == l.weekday():
        return [f.strftime('%A')]

    return [day.strftime('%A') for day in sorted([f, l], key=lambda x: x.weekday())]


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert most_frequent_days(2399) == ['Friday'], "1st example"
    assert most_frequent_days(1152) == ['Tuesday', 'Wednesday'], "2nd example"
    assert most_frequent_days(56) == ['Saturday', 'Sunday'], "3rd example"
    assert most_frequent_days(2909) == ['Tuesday'], "4th example"
