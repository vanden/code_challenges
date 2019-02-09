# https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem

from collections import defaultdict

def sherlockAndAnagrams(s):
    seen = defaultdict(int)
    count = 0
    for sub in substrings(s):
        sub = ''.join(sorted(sub))
        count += seen[sub]
        seen[sub] += 1
    return count


def substrings(s):
    for length in range(len(s), 0, -1):
        for offset in range(0, len(s)-length+1):
            yield s[offset:length+offset]


if __name__ == "__main__":
    print(sherlockAndAnagrams("cdcd"))
