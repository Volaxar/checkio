# https://py.checkio.org/mission/speechmodule/
FIRST = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
         "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"
         ]

SECOND = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

HUNDRED = "hundred"


def checkio(number):
    data = []

    if number > 99:
        data.append('{} {}'.format(FIRST[number // 100 - 1], HUNDRED))
        number %= 100

    if number > 19:
        data.append(SECOND[number // 10 - 2])
        number %= 10

    if number != 0:
        data.append(FIRST[number - 1])

    return ' '.join(data)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
