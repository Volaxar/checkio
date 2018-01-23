# https://py.checkio.org/mission/ethernet-ring-dimensioning/
from collections import defaultdict
from math import ceil

ETHERNET = (100, 40, 10, 1, 0.1)  # Ethernet bandwidth capacity in Gbps


def checkio(ring, *flows):
    links = defaultdict(int)

    for (rb, re), bw in [*flows]:
        b, e = sorted([ring.find(rb), ring.find(re)])
        route_l, route_r = ring[b:e + 1], ring[e:] + ring[:b + 1]

        if len(route_l) == len(route_r) and route_l[0] == rb or len(route_l) < len(route_r):
            route = route_l
        else:
            route = route_r

        for l, r in [*zip(route[:-1], route[1:])]:
            links[l + r] += bw

    links_list = []

    for v in links.values():
        if v > ETHERNET[0]:
            links_list += [ETHERNET[0]] * int(ceil(v / 100))
        else:
            links_list.append(v)

    result = []

    for l, r in [*zip(ETHERNET, ETHERNET[1:] + (0,))]:
        result.append(len([v for v in links_list if l >= v > r]))

    return result


if __name__ == '__main__':
    # These "asserts" are used only for self-checking and not necessary for auto-testing
    assert checkio("AEFCBG", ("AC", 5), ("EC", 10), ("AB", 60)) == [2, 2, 1, 0, 0]
    assert checkio("ABCDEFGH", ("AD", 4)) == [0, 0, 3, 0, 0]
    assert checkio("ABCDEFGH", ("AD", 4), ("EA", 41)) == [4, 0, 3, 0, 0]
