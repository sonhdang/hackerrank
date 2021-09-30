# https://www.hackerrank.com/challenges/time-conversion/problem

def timeConversion(s):
    arr = s.split(':')
    if (arr[2][2:] == "PM" and arr[0] != "12"):
        arr[0] = str(int(arr[0]) + 12).zfill(2)
    elif (arr[2][2:] == "AM" and arr[0] == "12"):
        arr[0] = "00"
    arr[2] = arr[2][:2]
    return ':'.join(arr)