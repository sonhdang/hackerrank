# https://www.hackerrank.com/challenges/python-print/problem

if __name__ == '__main__':
    n = int(raw_input())
    result = ""
    for i in range(n):
        result += str(i+1)
    print(result)