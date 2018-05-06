#!/bin/python3
# https://www.hackerrank.com/challenges/python-time-delta/problem

import datetime
import sys

def time_delta(t1, t2):
    t1 = getDateTime(t1)
    t2 = getDateTime(t2)
    return int(abs((t1 - t2).total_seconds()))

def getDateTime(stamp):
    months = {"Jan": 1, "January": 1,
              "Feb": 2, "February": 2,
              "Mar": 3, "March": 3,
              "Apr": 4, "April": 4,
              "May": 5,
              "Jun": 6, "June": 6,
              "Jul" : 7, "July": 7,
              "Aug": 8, "August": 8,
              "Sep": 9, "September": 9,
              "Oct": 10, "October": 10,
              "Nov": 11, "November": 11,
              "Dec": 12, "December": 12
             }
    ts = stamp.split()
    hrs, mins, secs = (int(x) for x in ts[4].split(':'))
    tzone = ts[-1]
    tzmin = int(tzone[-2:])
    tzhs = int(tzone[-4:-2])
    tdelta = datetime.timedelta(seconds=tzhs*60*60 + tzmin*60)
    if tzone[0] == '+':
        tdelta *= -1
    d, m, y = (int(x) for x in (ts[1], months[ts[2]], ts[3]))
    return datetime.datetime(y, m, d, hrs, mins, secs) + tdelta

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        t1 = input().strip()
        t2 = input().strip()
        delta = time_delta(t1, t2)
        print(delta)
