# https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/

import random
from collections import defaultdict

# For some reason, this example
# ["RandomizedCollection","insert","insert","insert","getRandom","remove","getRandom"]
# [[],[1],[1],[2],[],[1],[]]
# runs fine locally, but on the leetcode site the line
#    valPosition = self.positions[val].pop()
# raises an IndexError. And, the local Python version is identical to the one on leetcode. Wat. Putting this aside, for now. Especially as I am
# quite certain it won't work even if it runs

class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []
        self.positions = defaultdict(list)
        self.counts = defaultdict(int)

    def __repr__(self):
        return("RandomizedCollection(data: %s, positions: %s)" %(self.data, self.positions))

    def insert(self, val: 'int') -> 'bool':
        """
        Inserts a value to the collection. Returns true if the collection did
        not already contain the specified element.
        """

        novel = not val in self.positions

        self.data.append(val)
        self.positions[val].append(len(self.data) - 1)
        return novel

    def remove(self, val: 'int') -> 'bool':
        """
        Removes a value from the collection. Returns true if the collection
        contained the specified element.
        """
        if not val in self.positions:
            return False

        valPosition = self.positions[val].pop()
        self.data[valPosition] = None

        last = self.data[-1]

        return True

    def getRandom(self) -> 'int':
        """
        Get a random element from the collection.
        """
        choice = None
        while choice is None:
            choice = random.choice(self.data)
        return choice


# ["RandomizedCollection","insert","insert","insert","insert","insert","remove","remove","remove","remove"]
# [[],[4],[3],[4],[2],[4],[4],[3],[4],[4]]


# r = RandomizedCollection()
# r.insert(4)
# r.insert(3)
# r.insert(4)
# #print(repr(r))
# r.insert(2)
# r.insert(4)
# #print(repr(r))
# r.remove(4)
# #print(repr(r))
# r.remove(3)
# #print(repr(r))
# #print("_--------------------")
# print(r.remove(4))
# #print(repr(r))
# print(r.remove(4))
# #print(repr(r))

# r = RandomizedCollection()
# r.insert(1)
# print(repr(r))
# r.remove(1)
# print(repr(r))
# r.insert(1)
# print(repr(r))

# #["RandomizedCollection","insert","remove","insert"]
# #[[],[1],[1],[1]]


r = RandomizedCollection()
print(r.insert(0))
print(r.remove(0))
print(r.insert(-1))
print(r.insert(0))
print(r.getRandom())
print(r.getRandom())
print(r.getRandom())
print(r.getRandom())
#["RandomizedCollection","insert","remove","insert","remove","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom"]
#[[],[0],[0],[-1],[0],[],[],[],[],[],[],[],[],[],[]]
