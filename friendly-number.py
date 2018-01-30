# https://py.checkio.org/mission/friendly-number/solve/


from math import log


def friendly_number(number, base=1000, decimals=0, suffix='', powers=None):
    """
    Format a number as friendly text, using common suffixes.
    """

    if powers is None:
        powers = ['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']

    tmp_power = int(log(abs(number), base)) if number else 0
    power = min(tmp_power, len(powers) - 1)

    tmp_result = number / base ** power
    result = tmp_result if decimals else int(tmp_result)

    return '{:.{}f}{}{}'.format(result, decimals, powers[power], suffix)


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert friendly_number(102) == '102', '102'
    assert friendly_number(10240) == '10k', '10k'
    assert friendly_number(12341234, decimals=1) == '12.3M', '12.3M'
    assert friendly_number(12461, decimals=1) == '12.5k', '12.5k'
    assert friendly_number(1024000000, base=1024, suffix='iB') == '976MiB', '976MiB'
