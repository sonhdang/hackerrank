# https://www.hackerrank.com/challenges/python-lists/problem

if __name__ == '__main__':
    N = int(raw_input())
    nums = []
    for i in range(N):
        command = raw_input().split()
        if len(command) == 1:
            if command[0] == "print":
                print(nums)
            elif command[0] == "sort":
                nums.sort()
            elif command[0] == "pop":
                if len(nums) != 0:
                    nums = nums[0:len(nums) - 1]
            else:
                nums.reverse()
        elif len(command) == 2:
            if command[0] == "remove":
                nums.remove(int(command[1]))
            else:
                nums.append(int(command[1]))
        else:
            nums.insert(int(command[1]), int(command[2]))