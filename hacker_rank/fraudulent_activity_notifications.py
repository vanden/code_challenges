# https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem

from collections import deque

class Median():
    def __init__(self, seed):
        self.size = len(seed)
        self.deque = deque(seed, len(seed))
        self.counts = [0] * 201
        for val in seed:
            self.counts[val] += 1

    def push(self, val):
        self.counts[self.deque[0]] -= 1
        self.deque.append(val)
        self.counts[val] += 1

    def median(self):
        midpoint = int(self.size)/2
        totalCountSeen = 0
        if self.size % 2:
            for i, count in enumerate(self.counts):
                totalCountSeen += count
                if totalCountSeen >= midpoint:
                    return i
        else:
            low = None
            for i, count in enumerate(self.counts):
                totalCountSeen += count
                if low is None and (totalCountSeen >= midpoint):
                    low = i
                elif totalCountSeen >= (midpoint + 1):
                    return (low + i)/2

def activityNotifications(expenditure, d):
    window = Median(expenditure[:d])
    notifications = 0

    for day in expenditure[d:]:
        median = window.median()
        if day >= (2 * median):
            notifications += 1
        window.push(day)
    return notifications

case0 = ([2, 3, 4, 2, 3, 6, 8, 4, 5], 5, 2)
case1 = ([1, 2, 3, 4, 4], 4, 0)
case2 = ([10, 20, 30, 40, 50], 3, 1)

def test(case):
    result = activityNotifications(case[0], case[1])
    print(result == case[-1], result, case[-1])


if __name__ == "__main__":
    for case in [
            case0,
            case1,
            case2
    ]:
        test(case)
