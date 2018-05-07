# https://www.hackerrank.com/challenges/ginorts/problem

# All sorted lowercase letters are ahead of uppercase letters.
# All sorted uppercase letters are ahead of digits.
# All sorted odd digits are ahead of sorted even digits.

import string

def sortF(c):
    if c in string.ascii_lowercase:
        return (0, c)
    if c in string.ascii_uppercase:
        return (1, c)
    if c in string.digits:
        c = int(c)
        if c%2:
            return (2, c)
        else:
            return (3, c)
    return c

print(''.join(sorted(list(input()),key=sortF)))
