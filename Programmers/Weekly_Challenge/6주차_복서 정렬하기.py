import functools

def comparator(a, b):
    if a[0] == b[0]:
        if a[1] == b[1]:
            if a[2] == b[2]:
                return a[3] - b[3]
            else:
                return b[2] - a[2]
        else:
            return b[1] - a[1]
    else:
        return b[0] - a[0]

def solution(weights, head2head):
    # result에 각 선수의 승률, 더 무거운 선수를 이긴 횟수, 자신의 몸무게, 번호 저장
    n = len(weights)
    result = []
    for i in range(n):
        cnt = 0
        win = 0
        heavier = 0
        for j in range(n):
            if head2head[i][j] != 'N':
                cnt += 1
            if head2head[i][j] == 'W':
                win += 1
                if weights[i] < weights[j]:
                    heavier += 1
        if cnt == 0:
            result.append([0, heavier, weights[i], i + 1])
        else:
            result.append([win/cnt, heavier, weights[i], i + 1])

    # 문제 기준에 맞게 정렬하기
    result.sort(key=functools.cmp_to_key(comparator))
    answer = []
    for r in result:
        answer.append(r[3])

    return answer

# 정확성  테스트
# 테스트 1 〉	통과 (0.02ms, 10.3MB)
# 테스트 2 〉	통과 (0.04ms, 10.3MB)
# 테스트 3 〉	통과 (0.03ms, 10.4MB)
# 테스트 4 〉	통과 (0.05ms, 10.4MB)
# 테스트 5 〉	통과 (0.03ms, 10.3MB)
# 테스트 6 〉	통과 (79.51ms, 11MB)
# 테스트 7 〉	통과 (109.19ms, 11.5MB)
# 테스트 8 〉	통과 (127.33ms, 11.7MB)
# 테스트 9 〉	통과 (36.00ms, 10.7MB)
# 테스트 10 〉	통과 (32.53ms, 10.8MB)
# 테스트 11 〉	통과 (142.07ms, 11.5MB)
# 테스트 12 〉	통과 (75.85ms, 11.1MB)

def solution(weights, head2head):
    # result에 각 선수의 승률, 더 무거운 선수를 이긴 횟수, 자신의 몸무게, 번호 저장
    n = len(weights)
    result = []
    for i in range(n):
        cnt = 0
        win = 0
        heavier = 0
        for j in range(n):
            if head2head[i][j] != 'N':
                cnt += 1
            if head2head[i][j] == 'W':
                win += 1
                if weights[i] < weights[j]:
                    heavier += 1
        if cnt == 0:
            result.append([0, heavier, weights[i], i + 1])
        else:
            result.append([win/cnt, heavier, weights[i], i + 1])

    # 문제 기준에 맞게 정렬하기
    result.sort(key=lambda x: (-x[0], -x[1], -x[2], x[3]))
    answer = []
    for r in result:
        answer.append(r[3])

    return answer

# 정확성  테스트
# 테스트 1 〉	통과 (0.02ms, 10.1MB)
# 테스트 2 〉	통과 (0.03ms, 10.2MB)
# 테스트 3 〉	통과 (0.03ms, 10.3MB)
# 테스트 4 〉	통과 (0.02ms, 10.2MB)
# 테스트 5 〉	통과 (0.02ms, 10.2MB)
# 테스트 6 〉	통과 (80.85ms, 10.8MB)
# 테스트 7 〉	통과 (105.61ms, 11.4MB)
# 테스트 8 〉	통과 (124.28ms, 11.5MB)
# 테스트 9 〉	통과 (35.03ms, 10.4MB)
# 테스트 10 〉	통과 (29.36ms, 10.4MB)
# 테스트 11 〉	통과 (116.82ms, 11.3MB)
# 테스트 12 〉	통과 (55.64ms, 10.8MB)