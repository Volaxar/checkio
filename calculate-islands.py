# https://py.checkio.org/mission/calculate-islands/solve/

from math import sqrt


def is_neighbor(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) < 2


def get_island(point, land):
    island = [point]

    for piece in land.copy():
        if is_neighbor(*point, *piece) and piece not in island:
            land.remove(piece)
            island.extend(get_island(piece, land))

    return island


def checkio(land_map):
    land = []
    islands = []

    for y, row in enumerate(land_map):
        for x, col in enumerate(row):
            if col:
                land.append((x, y))

    while land:
        islands.append(len(get_island(land.pop(), land)))

    return sorted(islands)


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([[0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 0],
                    [0, 1, 0, 0, 0],
                    [0, 0, 0, 0, 0]]) == [1, 3], "1st example"
    assert checkio([[0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 0],
                    [0, 1, 1, 0, 0]]) == [5], "2nd example"
    assert checkio([[0, 0, 0, 0, 0, 0],
                    [1, 0, 0, 1, 1, 1],
                    [1, 0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 1, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0]]) == [2, 3, 3, 4], "3rd example"
