# https://www.hackerrank.com/challenges/write-a-function/problem


def is_leap(year):
    if year % 4 or ( ! (year % 100) and year % 400):
        return False
    return True
