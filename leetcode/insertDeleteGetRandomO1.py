# https://leetcode.com/problems/insert-delete-getrandom-o1/description/

# Not really sure I understand the bounds of what I can use.

import random

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []
        self.positions = {}

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.positions:
            return False
        self.data.append(val)
        self.positions[val] = len(self.data) - 1
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if not val in self.positions:
            return False
        last = self.data[-1]
        self.data[self.positions[val]] = last
        self.positions[last] = self.positions[val]
        self.positions.pop(val)
        self.data.pop()
        return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return random.choice(self.data)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

# r = RandomizedSet()
# print(r.insert(0))
# print(r.insert(1))
# print(r.remove(0))
# print(r.insert(2))
# print(r.remove(1))
# print(r.getRandom())

# ["RandomizedSet","insert","insert","remove","insert","remove","getRandom"]
# [[],[0],[1],[0],[2],[1],[]]
