#https://www.hackerrank.com/contests/projecteuler/challenges/euler092


getsTo89 = set((89, 145))
doesnotArrive = set((1, 44))
arrivedAt89 = set()

def arrivesAt89(n):
    if n in getsTo89:
        arrivedAt89.add(n)
        return True
    if n in doesnotArrive:
        return False
    seen = set([n])
    m = n
    while True:
        m = sum(i*i for i in (int(c) for c in str(m)))
        seen.add(m)
        if m in getsTo89:
            arrivedAt89.add(n)
            getsTo89.update(seen)
            return True
        if m in doesnotArrive:
            doesnotArrive.update(seen)
            return False

k = 4#int(input())

for i in range(10**k, 1, -1):
    arrivesAt89(i)
print(len(arrivedAt89) % (10**9 + 7))
