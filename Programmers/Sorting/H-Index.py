# https://programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    citations.sort(reverse=True)
    for i, citation in enumerate(citations):
        if i + 1 > citation:
            return i

    # 모든 논문의 인용 횟수가 전체 논문의 개수 이상인 경우
    return len(citations)

### 정확성  테스트
# 테스트 1 〉	통과 (0.12ms, 10.2MB)
# 테스트 2 〉	통과 (0.21ms, 10.3MB)
# 테스트 3 〉	통과 (0.18ms, 10.2MB)
# 테스트 4 〉	통과 (0.10ms, 10.3MB)
# 테스트 5 〉	통과 (0.14ms, 10.3MB)
# 테스트 6 〉	통과 (0.13ms, 10.3MB)
# 테스트 7 〉	통과 (0.07ms, 10.2MB)
# 테스트 8 〉	통과 (0.01ms, 10.2MB)
# 테스트 9 〉	통과 (0.02ms, 10.2MB)
# 테스트 10 〉	통과 (0.06ms, 10.1MB)
# 테스트 11 〉	통과 (0.14ms, 10.2MB)
# 테스트 12 〉	통과 (0.03ms, 10.2MB)
# 테스트 13 〉	통과 (0.14ms, 10.2MB)
# 테스트 14 〉	통과 (0.18ms, 10.2MB)
# 테스트 15 〉	통과 (0.20ms, 10.2MB)
# 테스트 16 〉	통과 (0.00ms, 10.2MB)