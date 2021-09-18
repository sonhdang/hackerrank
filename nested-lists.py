# https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':
    arr = []
    lowest = 100
    second_lowest = 100
    for _ in range(int(raw_input())):
        name = raw_input()
        score = float(raw_input())
        
        if score < lowest:
            second_lowest = lowest
            lowest = score
        elif score > lowest:
            if score < second_lowest:
                second_lowest = score
        arr.append([name,score])
    
    result = []
    for i in arr:
        if i[1] == second_lowest:
            result.append(i[0])
    result.sort()
    for i in result:
        print(i)