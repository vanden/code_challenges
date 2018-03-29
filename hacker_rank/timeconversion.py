#!/bin/python3

# https://www.hackerrank.com/challenges/time-conversion/problem


def timeConversion(s):
    hours, minutes, rest = s.split(':')
    hours = int(hours)
    seconds = rest[:2]
    ampm = rest[2:]
    if hours == 12:
        if ampm == 'AM':
            hours = 0
    else:
        if ampm == 'PM':
            hours = (hours + 12)

    return "%02d:%s:%s" %(hours, minutes, seconds)

def tests():
    """
    >>> timeConversion("10:13:14AM")
    '10:13:14'
    >>> timeConversion("10:13:14PM")
    '22:13:14'
    >>> timeConversion("12:00:00AM")
    '00:00:00'
    >>> timeConversion("12:00:00PM")
    '12:00:00'
    >>> timeConversion("12:00:01AM")
    '00:00:01'
    >>> timeConversion("12:00:01PM")
    '12:00:01'
    """
if __name__ == "__main__":
    import doctest
    doctest.testmod()
