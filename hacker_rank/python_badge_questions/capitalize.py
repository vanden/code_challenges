# https://www.hackerrank.com/challenges/capitalize/problem

def solve(s):
    lastWasSpace = True
    new = list(s)
    for i in range(len(s)):
        if s[i] == " ":
            lastWasSpace = True
        elif lastWasSpace:
            new[i] = new[i].upper()
            lastWasSpace = False
    return "".join(new)
