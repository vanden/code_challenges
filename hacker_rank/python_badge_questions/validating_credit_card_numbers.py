# https://www.hackerrank.com/challenges/validating-credit-card-number/problem

import re
p = re.compile(r'(\d*)(\d)\2{3}')
for i in range(int(input())):
    card = input()
    bad = False
    clean = ''.join(c for c in card if c.isdigit() or c == '-')
    striped = ''.join(c for c in clean if c.isdigit())
    if len(striped) != 16:
        bad = True
    elif clean != card:
        bad = True
    elif not(card[0] in '456'):
        bad = True
    elif re.match(p, striped):
        bad = True
    if '-' in card:
        chunks = card.split('-')
        for chunk in chunks:
            if len(chunk) != 4:
                bad = True
    if bad:
        print("Invalid")
    else:
        print("Valid")
