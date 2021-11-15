import sys

readline = sys.stdin.readline
T = int(readline())
for _ in range(T):
    N = int(readline())
    note1 = readline().split()
    M = int(readline())
    note2 = readline().split()

    nums = {}
    for num1 in note1:
        nums[num1] = True
    for num2 in note2:
        if num2 in nums:
            print(1)
        else:
            print(0)
