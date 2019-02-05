# https://www.hackerrank.com/challenges/the-minion-game/problem

def minion_game(string):
    string = string.upper()
    vstrings = 0
    cstrings = 0
    for i in range(len(string)):
        if string[i] in "AEIOU":
            vstrings += len(string) - i
        else:
            cstrings += len(string) - i

    if cstrings == vstrings:
        print("Draw")
    elif cstrings > vstrings:
        print("Stuart %s" %(cstrings))
    else:
        print("Kevin %s" %(vstrings))
