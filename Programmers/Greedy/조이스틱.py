# https://programmers.co.kr/learn/courses/30/lessons/42860?language=python3

def solution(name):
    # 상하 조작 횟수 구하기
    answer = 0
    for i in name:
        if i < "N":
            answer += ord(i) - ord("A")
        else:
            answer += ord("Z") - ord(i) + 1

    # 좌우 조작 횟수 구하기
    n = len(name)
    left_count = 0
    right_count = 0
    half_left_count = 0
    half_right_count = 0
    for i in range(1, n):
        if name[i] != "A":
            left_count = i
            if i <= n // 2:
                half_left_count = i

        if name[-i] != "A":
            right_count = i
            if i <= n // 2:
                half_right_count = i

    answer += min(left_count, right_count,
                  half_left_count * 2 + half_right_count,
                  half_left_count + half_right_count * 2)
    return answer

### 정확성  테스트
# 테스트 1 〉	통과 (0.01ms, 10.1MB)
# 테스트 2 〉	통과 (0.01ms, 10MB)
# 테스트 3 〉	통과 (0.01ms, 10.1MB)
# 테스트 4 〉	통과 (0.01ms, 10MB)
# 테스트 5 〉	통과 (0.01ms, 10.1MB)
# 테스트 6 〉	통과 (0.01ms, 10.1MB)
# 테스트 7 〉	통과 (0.01ms, 10.1MB)
# 테스트 8 〉	통과 (0.01ms, 10.2MB)
# 테스트 9 〉	통과 (0.01ms, 10.1MB)
# 테스트 10 〉	통과 (0.01ms, 10.1MB)
# 테스트 11 〉	통과 (0.01ms, 10.1MB)
