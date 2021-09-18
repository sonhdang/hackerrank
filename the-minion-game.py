# https://www.hackerrank.com/challenges/the-minion-game/problem

s = "BANANA"

def minion_game(string):
    def isvowel(c):
        vowel = "aeiouAEIOU"
        return c in vowel

    stuart = 0
    kevin = 0

    for i in range(len(s)):
        if isvowel(s[i]):
            kevin += len(s) - i
        else:
            stuart += len(s) - i
    
    if stuart > kevin:
        print("Stuart " + str(stuart))
    elif stuart == kevin:
        print("Draw")
    else:
        print("Kevin " + str(kevin))
    
minion_game(s)