# https://programmers.co.kr/learn/courses/30/lessons/42842?language=python3

def solution(brown, yellow):
    total = brown + yellow
    for i in range(total // 3, 2, -1):
        if total % i == 0 and (i + (total // i) - 2) * 2 == brown:
            return [i, total // i]

### 정확성  테스트
# 테스트 1 〉	통과 (0.00ms, 10.2MB)
# 테스트 2 〉	통과 (0.00ms, 10.2MB)
# 테스트 3 〉	통과 (17.06ms, 10.1MB)
# 테스트 4 〉	통과 (0.03ms, 10.1MB)
# 테스트 5 〉	통과 (0.19ms, 10.2MB)
# 테스트 6 〉	통과 (5.81ms, 10.2MB)
# 테스트 7 〉	통과 (21.88ms, 10.2MB)
# 테스트 8 〉	통과 (17.13ms, 10.2MB)
# 테스트 9 〉	통과 (21.73ms, 10.2MB)
# 테스트 10 〉	통과 (25.71ms, 10.2MB)
# 테스트 11 〉	통과 (0.00ms, 10.1MB)
# 테스트 12 〉	통과 (0.00ms, 10.2MB)
# 테스트 13 〉	통과 (0.00ms, 10.3MB)