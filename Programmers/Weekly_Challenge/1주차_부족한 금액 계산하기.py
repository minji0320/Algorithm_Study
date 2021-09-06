# https://programmers.co.kr/learn/courses/30/lessons/82612?language=python3

def solution(price, money, count):
    answer = count * (count + 1) / 2 * price - money

    if answer > 0:
        return answer
    else:
        return 0

### 정확성  테스트
# 테스트 1 〉	통과 (0.00ms, 10.2MB)
# 테스트 2 〉	통과 (0.00ms, 10.2MB)
# 테스트 3 〉	통과 (0.00ms, 10.2MB)
# 테스트 4 〉	통과 (0.00ms, 10.2MB)
# 테스트 5 〉	통과 (0.00ms, 10.1MB)
# 테스트 6 〉	통과 (0.00ms, 10.2MB)
# 테스트 7 〉	통과 (0.00ms, 10.2MB)
# 테스트 8 〉	통과 (0.00ms, 10.1MB)
# 테스트 9 〉	통과 (0.00ms, 10.2MB)
# 테스트 10 〉	통과 (0.00ms, 10.2MB)
# 테스트 11 〉	통과 (0.01ms, 10.2MB)
# 테스트 12 〉	통과 (0.00ms, 10.2MB)
# 테스트 13 〉	통과 (0.00ms, 10.2MB)
# 테스트 14 〉	통과 (0.00ms, 10.2MB)
# 테스트 15 〉	통과 (0.00ms, 10.2MB)
# 테스트 16 〉	통과 (0.00ms, 10.2MB)
# 테스트 17 〉	통과 (0.00ms, 10.2MB)
# 테스트 18 〉	통과 (0.00ms, 10.2MB)
# 테스트 19 〉	통과 (0.00ms, 10.2MB)
# 테스트 20 〉	통과 (0.00ms, 10.2MB)
# 테스트 21 〉	통과 (0.00ms, 10.2MB)
# 테스트 22 〉	통과 (0.00ms, 10.2MB)
# 테스트 23 〉	통과 (0.00ms, 10.2MB)