# https://www.hackerrank.com/challenges/swap-case/problem

def swap_case(s):
    swapped = ""
    for c in s:
        if c.isupper():
            swapped += c.lower()
        elif c.islower():
            swapped += c.upper()
        else:
            swapped += c
    return swapped