# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

# First attempt
if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    highest = 0
    runner_up = 0
    if arr[0] > arr[1]:
        highest = arr[0]
        runner_up = arr[1]
    else:
        highest = arr[1]
        runner_up = arr[0]
        
    for x in arr:
        if highest > x:
            if runner_up < x:
                runner_up = x
        elif highest < x:
            runner_up = highest
            highest = x
            
        print(runner_up)

# Second attempt
if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    arr.sort(reverse=True)
    highest = arr[0]
    runner_up = highest
    for i in arr:
        if runner_up > i:
            runner_up = i
            break
    print(runner_up)