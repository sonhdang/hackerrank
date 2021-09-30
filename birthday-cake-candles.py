# https://www.hackerrank.com/challenges/birthday-cake-candles/problem

def birthdayCakeCandles(candles):
    height = 0
    count = 0
    for candle in candles:
        if candle > height:
            height = candle
            count = 1
        elif candle == height:
            count += 1
    return count