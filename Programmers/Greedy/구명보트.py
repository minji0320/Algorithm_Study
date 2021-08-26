# https://programmers.co.kr/learn/courses/30/lessons/42885?language=python3

def solution(people, limit):
    people.sort()
    answer = 0
    front = 0
    back = len(people) - 1

    while front <= back:
        # 가장 가벼운 사람과 가장 무거운 사람이 함께 탈 수 있는 경우
        if people[front] + people[back] <= limit:
            answer += 1
            front += 1
            back -= 1

        # 함께 탈 수 없는 경우
        else:
            answer += 1
            back -= 1

    return answer

### 정확성  테스트
# 테스트 1 〉	통과 (0.82ms, 10.2MB)
# 테스트 2 〉	통과 (0.67ms, 10.1MB)
# 테스트 3 〉	통과 (0.57ms, 10.1MB)
# 테스트 4 〉	통과 (0.51ms, 10.1MB)
# 테스트 5 〉	통과 (0.30ms, 10.1MB)
# 테스트 6 〉	통과 (0.32ms, 10.2MB)
# 테스트 7 〉	통과 (0.46ms, 10.2MB)
# 테스트 8 〉	통과 (0.05ms, 10.1MB)
# 테스트 9 〉	통과 (0.06ms, 10MB)
# 테스트 10 〉	통과 (0.57ms, 10.1MB)
# 테스트 11 〉	통과 (0.46ms, 10.2MB)
# 테스트 12 〉	통과 (0.52ms, 10MB)
# 테스트 13 〉	통과 (0.59ms, 10MB)
# 테스트 14 〉	통과 (0.74ms, 10.2MB)
# 테스트 15 〉	통과 (0.07ms, 10.2MB)

### 효율성  테스트
# 테스트 1 〉	통과 (8.55ms, 10.5MB)
# 테스트 2 〉	통과 (9.51ms, 10.5MB)
# 테스트 3 〉	통과 (8.43ms, 10.4MB)
# 테스트 4 〉	통과 (8.64ms, 10.6MB)
# 테스트 5 〉	통과 (8.24ms, 10.5MB)