# https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/

# Runtime: 88 ms, faster than 99.75% of Python3 online submissions for Insert
# Delete GetRandom O(1) - Duplicates allowed.

# Memory Usage: 12.2 MB, less than 78.30% of Python3 online submissions for
# Insert Delete GetRandom O(1) - Duplicates allowed.


import random
from collections import defaultdict

class RandomizedCollection1:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []
        self.positions = defaultdict(list)
        self.counts = defaultdict(int)

    def __repr__(self):
        return "RandomizedCollection(data: %s, positions: %s)" %(self.data, self.positions)

    def insert(self, val: 'int') -> 'bool':
        """
        Inserts a value to the collection. Returns true if the collection did
        not already contain the specified element.
        """

        novel = not (val in self.positions and self.positions[val])

        self.data.append(val)
        self.positions[val].append(len(self.data) - 1)
        return novel

    def remove(self, val: 'int') -> 'bool':
        """
        Removes a value from the collection. Returns true if the collection
        contained the specified element.
        """
        if not (val in self.positions and self.positions[val]):
            return False

        valPosition = self.positions[val].pop()
        self.data[valPosition] = None

        return True

    def getRandom(self) -> 'int':
        """
        Get a random element from the collection.
        """
        choice = None
        while choice is None:
            choice = random.choice(self.data)
        return choice

# Attempted memory optimization did not help:

# Runtime: 92 ms, faster than 95.42% of Python3 online submissions for Insert
# Delete GetRandom O(1) - Duplicates allowed.

# Memory Usage: 12.2 MB, less than 79.25% of Python3 online submissions for
# Insert Delete GetRandom O(1) - Duplicates allowed


class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []
        self.positions = defaultdict(list)
        self.counts = defaultdict(int)

        # Attempting a memory optimization. This should help if inserts are
        # somewhat more frequent than removes. But, in a real world
        # application, it would need instrumenting to see if it is better.
        self.freeSlots = []

    def __repr__(self):
        return "RandomizedCollection(data: %s, positions: %s)" %(self.data, self.positions)


    def insert(self, val: 'int') -> 'bool':
        """
        Inserts a value to the collection. Returns true if the collection did
        not already contain the specified element.
        """

        novel = not (val in self.positions and self.positions[val])

        if self.freeSlots:
            slot = self.freeSlots.pop()
            self.data[slot] = val
            self.positions[val].append(slot)
        else:
            self.data.append(val)
            self.positions[val].append(len(self.data) - 1)

        return novel


    def remove(self, val: 'int') -> 'bool':
        """
        Removes a value from the collection. Returns true if the collection
        contained the specified element.
        """
        if not (val in self.positions and self.positions[val]):
            return False

        valPosition = self.positions[val].pop()
        self.data[valPosition] = None
        self.freeSlots.append(valPosition)
        return True


    def getRandom(self) -> 'int':
        """
        Get a random element from the collection.
        """
        choice = None
        while choice is None:
            choice = random.choice(self.data)
        return choice


if __name__ == "__main__":

    # ["RandomizedCollection","insert","insert","insert","insert","insert","remove","remove","remove","remove"]
    # [[],[4],[3],[4],[2],[4],[4],[3],[4],[4]]
    a = RandomizedCollection()
    a.insert(4)
    a.insert(3)
    a.insert(4)
    #print(repr(a))
    a.insert(2)
    a.insert(4)
    #print(repr(a))
    a.remove(4)
    #print(repr(a))
    a.remove(3)
    #print(repr(a))
    #print("_--------------------")
    print(a.remove(4))
    #print(repr(a))
    print(a.remove(4))
    #print(repr(a))
    print()


    # #["RandomizedCollection","insert","remove","insert"]
    # #[[],[1],[1],[1]]
    #
    # r = RandomizedCollection()
    # r.insert(1)
    # print(repr(r))
    # r.remove(1)
    # print(repr(r))
    # r.insert(1)
    # print(repr(r))


    # ["RandomizedCollection","insert","insert","insert","getRandom","remove","getRandom"]
    # [[],[1],[1],[2],[],[1],[]]

    #["RandomizedCollection","insert","remove","insert","remove","getRandom","getRandom","getRandom",
    # "getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom"]
    #[[],[0],[0],[-1],[0],[],[],[],[],[],[],[],[],[],[]]
    #
    # r = RandomizedCollection()
    # print(r.insert(0))
    # print(r.remove(0))
    # print(r.insert(-1))
    # print(r.insert(0))
    # print(r.getRandom())
    # print(r.getRandom())
    # print(r.getRandom())
    # print(r.getRandom())

    print()
    s = RandomizedCollection()
    print(s.insert(1))
    print(s.insert(1))
    print(s.insert(2))
    print(s.getRandom())
    print(s.remove(1))
    print(s.getRandom())


    t = RandomizedCollection()
    print(t.insert(0))
    print(t.remove(0))
    print(t.insert(-1))
    print(t.remove(0))
    print(t.getRandom())
    print(t.getRandom())
    print(t.getRandom())
    print(t.getRandom())
    print(t.getRandom())
    print(t.getRandom())
    print(t.getRandom())
    print(t.getRandom())

    ["RandomizedCollection","insert","remove","insert", "remove", "getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom"]
    [[], [0], [0], [-1], [0], [], [], [], [], [], [], [], [], [], []]
