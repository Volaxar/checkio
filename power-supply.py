# https://py.checkio.org/mission/power-supply/


class Node:
    __nodes = {}

    def __init__(self, name):
        self.name = name
        self.links = []

    @staticmethod
    def get_node(name):
        if name in Node.__nodes:
            node = Node.__nodes[name]

        else:
            node = Node(name)
            Node.__nodes[name] = node

        return node

    @staticmethod
    def clear():
        Node.__nodes = {}


def build_route(city, enabled, power):
    if power == 0:
        return

    for link in city.links:
        if link.name in enabled and enabled[link.name] >= power:
            continue

        enabled[link.name] = power

        build_route(link, enabled, power - 1)


def power_supply(network, power_plants):
    Node.clear()

    for link in network:
        for i, l in enumerate(link):
            if link[1 - i] not in power_plants:
                Node.get_node(l).links.append(Node.get_node(link[1 - i]))

    enabled = {}

    for plant, power in power_plants.items():
        build_route(Node.get_node(plant), enabled, power)

    return set([node for link in network for node in link if node not in power_plants]).difference(enabled.keys())


if __name__ == '__main__':
    assert power_supply([['p1', 'c1'], ['c1', 'c2']], {'p1': 1}) == set(['c2']), 'one blackout'
    assert power_supply([['c0', 'c1'], ['c1', 'p1'], ['c1', 'c3'], ['p1', 'c4']], {'p1': 1}) == set(
        ['c0', 'c3']), 'two blackout'
    assert power_supply([['p1', 'c1'], ['c1', 'c2'], ['c2', 'c3']], {'p1': 3}) == set([]), 'no blackout'
    assert power_supply([['c0', 'p1'], ['p1', 'c2']], {'p1': 0}) == set(['c0', 'c2']), 'weak power-plant'
    assert power_supply([['p0', 'c1'], ['p0', 'c2'], ['c2', 'c3'], ['c3', 'p4'], ['p4', 'c5']],
                        {'p0': 1, 'p4': 1}) == set([]), 'cooperation'
    assert power_supply([['c0', 'p1'], ['p1', 'c2'], ['c2', 'c3'], ['c2', 'c4'], ['c4', 'c5'],
                         ['c5', 'c6'], ['c5', 'p7']],
                        {'p1': 1, 'p7': 1}) == set(['c3', 'c4', 'c6']), 'complex cities 1'
    assert power_supply([['p0', 'c1'], ['p0', 'c2'], ['p0', 'c3'],
                         ['p0', 'c4'], ['c4', 'c9'], ['c4', 'c10'],
                         ['c10', 'c11'], ['c11', 'p12'], ['c2', 'c5'],
                         ['c2', 'c6'], ['c5', 'c7'], ['c5', 'p8']],
                        {'p0': 1, 'p12': 4, 'p8': 1}) == set(['c6', 'c7']), 'complex cities 2'
    assert power_supply([['c1', 'c2'], ['c2', 'c3']], {}) == set(['c1', 'c2', 'c3']), 'no power plants'
    assert power_supply([['p1', 'c2'], ['p1', 'c4'], ['c4', 'c3'], ['c2', 'c3']], {'p1': 1}) == set(['c3']), 'circle'
    assert power_supply([['p1', 'c2'], ['p1', 'c4'], ['c2', 'c3']], {'p1': 4}) == set([]), 'more than enough'
    print("Looks like you know everything. It is time for 'Check'!")
