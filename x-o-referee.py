# https://py.checkio.org/mission/x-o-referee/


def check(line):
    return len(line) == 1 and '.' not in line


def checkio(game_result):
    gr = sum(map(list, game_result), [])

    for rb, re, b, s in [[0, 3, 3, 1], [0, 3, 1, 3], [0, 1, 0, 4], [1, 2, 2, 2]]:
        winner = list(*filter(check, [set(gr[i * b::s][:3]) for i in range(rb, re)]))

        if winner:
            return winner[0]

    return 'D'


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
