from collections import deque
from itertools import permutations


def calculate(a, b, operator):
    if operator == "+":
        return a + b
    if operator == "-":
        return a - b
    if operator == "*":
        return a * b


def solution(expression):
    # 숫자, 연산자 저장
    nums = []
    operators = []
    temp = ""
    for i in expression:
        if '0' <= i <= '9':
            temp += i
        else:
            nums.append(int(temp))
            operators.append(i)
            temp = ""
    nums.append(int(temp))

    # 순열로 우선순위를 정하고, 우선순위에 맞게 연산 수행
    n = len(operators)
    priorities = list(permutations(set(operators)))
    max_value = 0
    for priority in priorities:
        temp_nums = deque()
        temp_operators = deque()
        temp_nums.append(nums[-1])
        idx = n - 1
        while idx != -1:
            if temp_operators and priority.index(temp_operators[-1]) < priority.index(operators[idx]):
                a = temp_nums.pop()
                b = temp_nums.pop()
                temp_nums.append(calculate(a, b, temp_operators.pop()))
            else:
                temp_nums.append(nums[idx])
                temp_operators.append(operators[idx])
                idx -= 1

        while temp_operators:
            a = temp_nums.pop()
            b = temp_nums.pop()
            temp_nums.append(calculate(a, b, temp_operators.pop()))

        result = abs(temp_nums.pop())
        if max_value < result:
            max_value = result

    return max_value
