# https://py.checkio.org/mission/ghosts-age/


def fibo():
    f = []
    a, b = 1, 1

    while a <= 5000:
        f.append(a)
        a, b = a + b, a

    return f


def checkio(opacity):
    f = fibo()
    t = 10000

    if opacity == 10000:
        return 0

    for x in range(1, 5001):
        t = t - (x if x in f else -1)

        if t == opacity:
            return x


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(10000) == 0, "Newborn"
    assert checkio(9999) == 1, "1 year"
    assert checkio(9997) == 2, "2 years"
    assert checkio(9994) == 3, "3 years"
    assert checkio(9995) == 4, "4 years"
    assert checkio(9990) == 5, "5 years"
