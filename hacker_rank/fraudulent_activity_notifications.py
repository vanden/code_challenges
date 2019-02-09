# https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem

from collections import deque

def activityNotifications(expenditure, d):
    window = deque(expenditure[:d], d)
    notifications = 0
    for day in expenditure[d:]:
        median = getMedian(window)
        if day >= 2 * median:
            notifications += 1
        window.append(day)
    return notifications

def getMedian(window):
    spends = sorted(window)
    length = len(spends)
    if length%2:
        return spends[int(length/2)]
    return (spends[int(length/2)] + spends[int(length/2)-1])/2


case0 = ([2, 3, 4, 2, 3, 6, 8, 4, 5], 5, 2)
case1 = ([1, 2, 3, 4, 4], 4, 0)
case2 = ([10, 20, 30, 40, 50], 3, 1)

def test(case):
    result = activityNotifications(case[0], case[1])
    print(result == case[-1], result, case[-1])


if __name__ == "__main__":
    for case in [case0, case1, case2]:
        test(case)
