# https://py.checkio.org/mission/double-substring/solve/


def double_substring(line):
    line_len = len(line)

    for subs_size in range(line_len // 2, 0, -1):
        for subs_start in range(line_len - subs_size * 2 + 1):
            subs_end = subs_start + subs_size

            if line[subs_start:subs_end] in line[subs_end:]:
                return subs_size

    return 0


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert double_substring('aaaa') == 2, "First"
    assert double_substring('abc') == 0, "Second"
    assert double_substring('aghtfghkofgh') == 3, "Third"
    print('"Run" is good. How is "Check"?')
