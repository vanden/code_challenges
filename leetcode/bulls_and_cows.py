# https://leetcode.com/problems/bulls-and-cows/

# Runtime: 44 ms, faster than 95.71% of Python3 online submissions for Bulls
# and Cows.

# Memory Usage: 12.3 MB, less than 0.74% of Python3 online submissions for
# Bulls and Cows.


from collections import defaultdict

class Solution:
    def getHint(self, secret: 'str', guess: 'str') -> 'str':
        trimmedGuess = defaultdict(int)
        trimmedSecret = defaultdict(int)
        bulls = 0

        for i, s in enumerate(secret):
            if guess[i] == s:
                bulls += 1
            else:
                trimmedGuess[guess[i]] += 1
                trimmedSecret[s] += 1

        cows = 0

        for g in trimmedGuess:
            cows += min(trimmedGuess[g], trimmedSecret[g])

        return "%sA%sB" %(bulls, cows)


cases = [
    ("1807", "7810", "1A3B"),
    ("1123", "0111", "1A1B"),
    ("2342", "2334", "2A1B"),
]

if __name__ == "__main__":

    s = Solution()

    for secret, guess, output in cases:
        result = s.getHint(secret, guess)
        if result == output:
            print(True)
        else:
            print(False, secret, guess, result, output)
