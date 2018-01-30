# https://py.checkio.org/mission/pangram/solve/


import re


def check_pangram(text):
    return len(set(re.sub(r'\W+|_|\d+', '', text).lower())) == 26


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_pangram("The quick brown fox jumps over the lazy dog."), "brown fox"
    assert not check_pangram("ABCDEF"), "ABC"
    assert check_pangram("Bored? Craving a pub quiz fix? Why, just come to the Royal Oak!"), "Bored?"
    print('If it is done - it is Done. Go Check is NOW!')
