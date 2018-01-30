# https://py.checkio.org/mission/triangle-angles/solve/


from math import acos, degrees


def get_angle(x, y, z):
    angle = acos((y * y + z * z - x * x) / (2 * y * z))
    return round(degrees(angle))


def checkio(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return [0, 0, 0]

    angles = []
    for line in [(a, b, c), (b, c, a), (c, a, b)]:
        angles.append(get_angle(*line))

    return sorted(angles)


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"

