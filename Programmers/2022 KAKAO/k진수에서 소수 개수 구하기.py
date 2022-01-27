# https://programmers.co.kr/learn/courses/30/lessons/92335

import math


def convert_to_base_k(num, k):
    result = []
    while num > 0:
        digit = str(num % k)
        result.append(digit)
        num //= k
    return ''.join(result[::-1])


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return False
    return True


def solution(n, k):
    nums = convert_to_base_k(n, k).split('0')
    answer = 0
    for num in nums:
        if num != '' and is_prime(int(num)):
            answer += 1
    return answer

# 정확성  테스트
# 테스트 1 〉	통과 (97.13ms, 10.4MB)
# 테스트 2 〉	통과 (0.03ms, 10.4MB)
# 테스트 3 〉	통과 (0.03ms, 10.4MB)
# 테스트 4 〉	통과 (0.03ms, 10.4MB)
# 테스트 5 〉	통과 (0.03ms, 10.5MB)
# 테스트 6 〉	통과 (0.03ms, 10.4MB)
# 테스트 7 〉	통과 (0.03ms, 10.4MB)
# 테스트 8 〉	통과 (0.03ms, 10.4MB)
# 테스트 9 〉	통과 (0.03ms, 10.4MB)
# 테스트 10 〉	통과 (0.03ms, 10.5MB)
# 테스트 11 〉	통과 (0.04ms, 10.4MB)
# 테스트 12 〉	통과 (0.03ms, 10.5MB)
# 테스트 13 〉	통과 (0.03ms, 10.4MB)
# 테스트 14 〉	통과 (0.03ms, 10.4MB)
# 테스트 15 〉	통과 (0.02ms, 10.4MB)
# 테스트 16 〉	통과 (0.03ms, 10.5MB)
# 채점 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0
