# Solution 1

import sys

n = int(input())
S = {}
for i in range(1, 21):
    S[i] = False

for _ in range(n):
    input_value = sys.stdin.readline().strip()
    if input_value == "all":
        for i in range(1, 21):
            S[i] = True
    elif input_value == "empty":
        for i in range(1, 21):
            S[i] = False
    else:
        operation, num = input_value.split()
        num = int(num)

        if operation == "add":
            S[num] = True
        elif operation == "remove":
            S[num] = False
        elif operation == "check":
            if S[num]:
                print(1)
            else:
                print(0)
        elif operation == "toggle":
            S[num] = not S[num]


# Solution 2

import sys

n = int(input())
S = set()
S_all = set(range(1, 21))

for _ in range(n):
    input_value = sys.stdin.readline().strip()
    if input_value == "all":
        S = S_all
    elif input_value == "empty":
        S = set()
    else:
        operation, num = input_value.split()
        num = int(num)

        if operation == "add":
            S.add(num)
        elif operation == "remove":
            if num in S:
                S.remove(num)
        elif operation == "check":
            if num in S:
                print(1)
            else:
                print(0)
        elif operation == "toggle":
            if num in S:
                S.remove(num)
            else:
                S.add(num)
