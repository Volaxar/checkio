# https://py.checkio.org/mission/friends/


class Friends:
    def __init__(self, connections):
        self.links = list(connections)

    def add(self, connection):
        if connection not in self.links:
            self.links.append(connection)
            return True

        return False

    def remove(self, connection):
        if connection in self.links:
            self.links.remove(connection)
            return True

        return False

    def names(self):
        return set().union(*self.links)

    def connected(self, name):
        return set().union(*filter({name}.intersection, self.links)) - {name}


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    letter_friends = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
    digit_friends = Friends([{"1", "2"}, {"3", "1"}])
    assert letter_friends.add({"c", "d"}) is True, "Add"
    assert letter_friends.add({"c", "d"}) is False, "Add again"
    assert letter_friends.remove({"c", "d"}) is True, "Remove"
    assert digit_friends.remove({"c", "d"}) is False, "Remove non exists"
    assert letter_friends.names() == {"a", "b", "c"}, "Names"
    assert letter_friends.connected("d") == set(), "Non connected name"
    assert letter_friends.connected("a") == {"b", "c"}, "Connected name"
