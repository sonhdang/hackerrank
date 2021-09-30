# https://www.hackerrank.com/challenges/mini-max-sum/problem

def miniMaxSum(arr):
    mi = min(arr)
    ma = max(arr)
    su = sum(arr)
    print("{} {}".format(su-ma, su-mi))