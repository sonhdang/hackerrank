# https://www.hackerrank.com/challenges/plus-minus/problem

def plusMinus(arr):
    pos = 0
    neg = 0
    for i in arr:
        if i > 0:
            pos += 1
        elif i < 0:
            neg += 1
    print("{0:.6}".format(float(pos)/len(arr)))
    print("{0:.6}".format(float(neg)/len(arr)))
    print("{0:.6}".format(float(len(arr)-pos-neg)/len(arr)))