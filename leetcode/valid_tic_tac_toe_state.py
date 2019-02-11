# https://leetcode.com/problems/valid-tic-tac-toe-state/

# Damn. Fails on the case (["XXX", "OOX", "OOX"], True) because I'm taking
# multiple winning lines to be illegal. But, of course, one play can cause 2
# 3-in-a-rows.

# I was already thinking that this was not elegant. To deal with that on the
# present approach is going to have to be even worse!

# Seems I was wrong. A count of xWon did it. But, this is not elegant!

# And, I still hadn't attended to the sort of case as represented by
# (["OXX","XOX","OXO"], False)

# Runtime: 24 ms, faster than 37.76% of Python online submissions for Valid
# Tic-Tac-Toe State.

# Memory Usage: 7 MB, less than 35.48% of Python online submissions for Valid
# Tic-Tac-Toe State.

# That was beastly!

class Solution():
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        chars = ''.join(board)
        xCount = chars.count("X")
        oCount = chars.count("O")

        if oCount > xCount or ((xCount - oCount) > 1):
            return False

        xWon = 0

        modBoard = []
        for row in board:
            modRow = []
            for char in row:
                if char == "X":
                    modRow.append(1)
                elif char == "O":
                    modRow.append(-1)
                else:
                    modRow.append(0)
            modBoard.append(modRow)

        wins = 0

        for row in modBoard:
            rowSum = sum(row)
            if rowSum in [3, -3]:
                wins += 1
                if sum(row) == 3:
                    xWon += 1

        if wins > 1:
            # Not clear the early bail is worth it. But, safe as it cannot be
            # at this stage (only having examined horizontals) that X has two
            # legal three-in-a-rows.
            return False

        for colIdx in (0, 1, 2):
            colSum = 0
            for rowIdx in (0, 1, 2):
                colSum += modBoard[rowIdx][colIdx]
            if colSum in (3, -3):
                wins += 1
                if colSum == 3:
                    xWon += 1

        diagsum = sum([modBoard[i][i] for i in (0, 1, 2)])
        if diagsum in (3, -3):
            wins += 1
            if diagsum == 3:
                xWon += 1
        diagsum = sum([modBoard[r][c] for r, c in [(0, 2), (1, 1), (2, 0)]])
        if diagsum in (3, -3):
            wins += 1
            if diagsum == 3:
                xWon += 1

        if xWon:
            if xCount == oCount or xWon > 2:
                return False
            return True

        if wins and (xCount > oCount) and not xWon:
            return False

        return wins < 2


cases = [
    (["XXX", "XOO", "OO "], False),
    (["XO ", "XO ", "XO "], False),
    (["   ", "   ", "   "], True),
    (["O  ", "   ", "   "], False),
    (["XOX", " X ", "   "], False),
    (["XXX", "   ", "OOO"], False),
    (["XOX", "O O", "XOX"], True),
    (["XXX", "OOX", "OOX"], True),
    (["OXX","XOX","OXO"], False)
]


if __name__ == "__main__":
    s = Solution()
    for inPut, outPut in cases:
        print(s.validTicTacToe(inPut) == outPut)
