# https://py.checkio.org/mission/cipher-map2/


def recall_password(cg, cp):
    result = ''
    
    for x in range(4):
        result += ''.join([cp[i][j] for i in range(4) for j in range(4) if cg[i][j] == 'X'])
        cg = list(zip(*cg[::-1]))
    
    return result


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example'
    
    assert recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'
