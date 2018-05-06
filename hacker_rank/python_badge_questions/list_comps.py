# https://www.hackerrank.com/challenges/list-comprehensions/problem

# Not really proper for a one-liner, and other oddities because hackerrank
x = 2
y = 2
z = 2
n = 2
print([[xc, yc, zc]
       for xc in range(x+1)
       for yc in range(y+1)
       for zc in range(z+1)
       if xc + yc + zc != n])
