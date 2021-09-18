# https://www.hackerrank.com/challenges/piling-up/problem

for i in range(int(raw_input())):
    n = int(raw_input())
    arr = map(int, raw_input().split())
    
    highest = 0
    flag = True
    head_i = 0
    tail_i = n - 1
    
    # Initial step
    if (arr[head_i] >= arr[tail_i]):
        highest = arr[head_i]
        head_i += 1
    else:
        highest = arr[tail_i]
        tail_i -= 1
    
    
    while (tail_i - head_i > 0):
        if (arr[head_i] >= arr[tail_i]):
            if (arr[head_i] <= highest):
                highest = arr[head_i]
                head_i += 1
            else:
                flag = False
                print("No")
                break
        else:
            if (arr[tail_i] <= highest):
                highest = arr[tail_i]
                tail_i -= 1
            else:
                flag = False
                print("No")
                break
    
    if flag:
        if (highest >= arr[tail_i]):
            print("Yes")
        else:
            print("No")
    
