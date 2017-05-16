# https://py.checkio.org/mission/pawn-brotherhood/


def safe_pawns(pawns):
    count = 0
    
    for p in pawns:
        g = int(p[1]) - 1
        v = ord(p[0])
        
        if g > 0:
            count += int(v > 97 and chr(v - 1) + str(g) in pawns or v < 104 and chr(v + 1) + str(g) in pawns)
    
    return count


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
