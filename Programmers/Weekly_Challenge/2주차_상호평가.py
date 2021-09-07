# https://programmers.co.kr/learn/courses/30/lessons/83201

def solution(scores):
    n = len(scores)
    answer = ''
    for i in range(n):
        # 자신을 평가한 점수가 유일한 최고점/최저점인지 판단
        total = 0
        mean = 0
        max_i, min_i = i, i
        for j in range(n):
            if max_i != -1 and i != j and scores[i][i] <= scores[j][i]:
                max_i = -1
            if min_i != -1 and i != j and scores[i][i] >= scores[j][i]:
                min_i = -1
            total += scores[j][i]

        # 평균 구하기
        if max_i == i or min_i == i:
            mean = (total - scores[i][i]) / (n - 1)
        else:
            mean = total / n

        # 학점 구하기
        if mean >= 90:
            answer += 'A'
        elif mean >= 80:
            answer += 'B'
        elif mean >= 70:
            answer += 'C'
        elif mean >= 50:
            answer += 'D'
        else:
            answer += 'F'

    return answer

# 정확성  테스트
# 테스트 1 〉	통과 (0.01ms, 10.3MB)
# 테스트 2 〉	통과 (0.01ms, 10.3MB)
# 테스트 3 〉	통과 (0.01ms, 10.1MB)
# 테스트 4 〉	통과 (0.01ms, 10.3MB)
# 테스트 5 〉	통과 (0.02ms, 10.2MB)
# 테스트 6 〉	통과 (0.02ms, 10.1MB)
# 테스트 7 〉	통과 (0.02ms, 10.1MB)
# 테스트 8 〉	통과 (0.02ms, 10.2MB)
# 테스트 9 〉	통과 (0.02ms, 10.2MB)
# 테스트 10 〉	통과 (0.03ms, 10.1MB)
# 테스트 11 〉	통과 (0.01ms, 10.3MB)
# 테스트 12 〉	통과 (0.01ms, 10.3MB)
# 테스트 13 〉	통과 (0.01ms, 10.1MB)
# 테스트 14 〉	통과 (0.01ms, 10.3MB)
# 테스트 15 〉	통과 (0.01ms, 10.1MB)
# 테스트 16 〉	통과 (0.01ms, 10.2MB)
# 테스트 17 〉	통과 (0.02ms, 10.1MB)
# 테스트 18 〉	통과 (0.02ms, 10.1MB)
# 테스트 19 〉	통과 (0.02ms, 10.3MB)
# 테스트 20 〉	통과 (0.03ms, 10.2MB)
# 테스트 21 〉	통과 (0.01ms, 10.2MB)
