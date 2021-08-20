# https://programmers.co.kr/learn/courses/30/lessons/42839?language=python3

import itertools

# 소수 판별 함수
def isPrime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    # 만들 수 있는 모든 숫자 조합 구하기
    permutations = set()
    for i in range(1, len(numbers) + 1):
        permutations |= set(map(int, map(''.join, itertools.permutations(numbers, i))))

    # 만든 숫자 조합에서 소수의 개수 구하기
    answer = 0
    for num in permutations:
        if isPrime(num):
            answer += 1

    return answer

### 정확성  테스트 : 속도 느림
# 테스트 1 〉	통과 (0.23ms, 10.3MB)
# 테스트 2 〉	통과 (144.02ms, 10.4MB)
# 테스트 3 〉	통과 (0.02ms, 10.3MB)
# 테스트 4 〉	통과 (11.59ms, 10.3MB)
# 테스트 5 〉	통과 (2.64ms, 10.3MB)
# 테스트 6 〉	통과 (0.03ms, 10.3MB)
# 테스트 7 〉	통과 (0.09ms, 10.4MB)
# 테스트 8 〉	통과 (2.62ms, 10.3MB)
# 테스트 9 〉	통과 (0.03ms, 10.3MB)
# 테스트 10 〉	통과 (2115.52ms, 10.4MB)
# 테스트 11 〉	통과 (66.72ms, 10.4MB)
# 테스트 12 〉	통과 (0.55ms, 10.3MB)


import itertools
import math

# 소수 판별 함수
def isPrime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    # 만들 수 있는 모든 숫자 조합 구하기
    permutations = set()
    for i in range(1, len(numbers) + 1):
        permutations |= set(map(int, map(''.join, itertools.permutations(numbers, i))))

    # 만든 숫자 조합에서 소수의 개수 구하기
    answer = 0
    for num in permutations:
        if isPrime(num):
            answer += 1

    return answer

### 정확성  테스트 : 소수 판별 범위를 "n -> int(math.sqrt(n)) + 1"로 변경하였더니 속도 빨라짐!
# 테스트 1 〉	통과 (0.05ms, 10.3MB)
# 테스트 2 〉	통과 (2.28ms, 10.4MB)
# 테스트 3 〉	통과 (0.02ms, 10.4MB)
# 테스트 4 〉	통과 (0.55ms, 10.3MB)
# 테스트 5 〉	통과 (4.57ms, 10.4MB)
# 테스트 6 〉	통과 (0.03ms, 10.3MB)
# 테스트 7 〉	통과 (0.05ms, 10.3MB)
# 테스트 8 〉	통과 (2.79ms, 10.3MB)
# 테스트 9 〉	통과 (0.04ms, 10.3MB)
# 테스트 10 〉	통과 (5.06ms, 10.5MB)
# 테스트 11 〉	통과 (0.55ms, 10.4MB)
# 테스트 12 〉	통과 (0.16ms, 10.4MB)