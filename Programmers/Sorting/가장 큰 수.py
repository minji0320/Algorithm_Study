# https://programmers.co.kr/learn/courses/30/lessons/42746

import functools

def comparator(a, b):
    t1 = a + b
    t2 = b + a
    if int(t1) > int(t2):
        return 1
    elif int(t1) < int(t2):
        return -1
    else:
        return 0

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=functools.cmp_to_key(comparator), reverse=True)

    answer = str(int(''.join(numbers)))
    return answer

### 정확성  테스트
# 테스트 1 〉	통과 (1565.09ms, 21.2MB)
# 테스트 2 〉	통과 (598.19ms, 16.2MB)
# 테스트 3 〉	통과 (2457.96ms, 24.5MB)
# 테스트 4 〉	통과 (13.39ms, 10.5MB)
# 테스트 5 〉	통과 (1561.32ms, 19.8MB)
# 테스트 6 〉	통과 (1192.70ms, 18.8MB)
# 테스트 7 〉	통과 (0.06ms, 10.4MB)
# 테스트 8 〉	통과 (0.04ms, 10.4MB)
# 테스트 9 〉	통과 (0.05ms, 10.4MB)
# 테스트 10 〉	통과 (0.06ms, 10.4MB)
# 테스트 11 〉	통과 (0.06ms, 10.4MB)