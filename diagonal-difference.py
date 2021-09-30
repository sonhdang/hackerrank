# https://www.hackerrank.com/challenges/diagonal-difference/problem

def diagonalDifference(arr):
    diagonal1 = 0
    diagonal2 = 0
    for i,j in zip(range(len(arr)),range(len(arr)-1, -1, -1)):
        diagonal1 += arr[i][i]
        diagonal2 += arr[i][j]
    return abs(diagonal1-diagonal2)
