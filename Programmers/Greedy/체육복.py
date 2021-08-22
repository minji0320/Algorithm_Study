# https://programmers.co.kr/learn/courses/30/lessons/42862?language=python3

def solution(n, lost, reserve):
    # 여벌의 체육복을 챙긴 학생이 도난당한 경우 제외
    intersection = list(set(lost) & set(reserve))
    lost = list(set(lost) - set(intersection))
    reserve = list(set(reserve) - set(intersection))
    answer = n - len(lost)

    # 여벌을 빌려줄 수 있는 학생 리스트
    isReserve = [False] * (n + 2)
    for i in reserve:
        isReserve[i] = True

    # 주변에 빌려줄 학생이 있는 경우
    for i in lost:
        if isReserve[i - 1]:
            isReserve[i - 1] = False
            answer += 1
        elif isReserve[i + 1]:
            isReserve[i + 1] = False
            answer += 1

    return answer

### 정확성  테스트
# 테스트 1 〉	통과 (0.01ms, 10.1MB)
# 테스트 2 〉	통과 (0.01ms, 10.3MB)
# 테스트 3 〉	통과 (0.01ms, 10.2MB)
# 테스트 4 〉	통과 (0.01ms, 10.3MB)
# 테스트 5 〉	통과 (0.01ms, 10.3MB)
# 테스트 6 〉	통과 (0.01ms, 10.3MB)
# 테스트 7 〉	통과 (0.01ms, 10.3MB)
# 테스트 8 〉	통과 (0.01ms, 10.3MB)
# 테스트 9 〉	통과 (0.01ms, 10.2MB)
# 테스트 10 〉	통과 (0.01ms, 10.1MB)
# 테스트 11 〉	통과 (0.01ms, 10.3MB)
# 테스트 12 〉	통과 (0.01ms, 10.3MB)
# 테스트 13 〉	통과 (0.01ms, 10.2MB)