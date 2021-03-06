# https://py.checkio.org/mission/striped-words/
import re

VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"


def checkio(text):
    pattern = r"""
    (
    \b(?:(?:[%(v)s][%(c)s])+)+[%(v)s]?\b
    |
    \b(?:(?:[%(c)s][%(v)s])+)+[%(c)s]?\b
    )+
    """ % {'v': VOWELS, 'c': CONSONANTS}
    
    return len(re.findall(pattern, text, re.VERBOSE | re.IGNORECASE))


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("My name is ...") == 3, "All words are striped"
    assert checkio("Hello world") == 0, "No one"
    assert checkio("A quantity of striped words.") == 1, "Only of"
    assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"
