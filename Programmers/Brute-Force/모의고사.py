# https://programmers.co.kr/learn/courses/30/lessons/42840?language=python3

def solution(answers):
    # 3명의 찍는 패턴
    patterns = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]

    # 3명의 점수 구하기
    score_list = [0, 0, 0]
    for i, answer in enumerate(answers):
        if answer == patterns[0][i % 5]:
            score_list[0] += 1
        if answer == patterns[1][i % 8]:
            score_list[1] += 1
        if answer == patterns[2][i % 10]:
            score_list[2] += 1

    # 가장 많이 맞춘 사람 구하기
    max_score = max(score_list)
    answer = []
    for i, score in enumerate(score_list):
        if max_score == score:
            answer.append(i + 1)
    return answer

### 정확성  테스트
# 테스트 1 〉	통과 (0.01ms, 10.3MB)
# 테스트 2 〉	통과 (0.01ms, 10.3MB)
# 테스트 3 〉	통과 (0.01ms, 10.2MB)
# 테스트 4 〉	통과 (0.01ms, 10.3MB)
# 테스트 5 〉	통과 (0.02ms, 10.3MB)
# 테스트 6 〉	통과 (0.03ms, 10.3MB)
# 테스트 7 〉	통과 (2.29ms, 10.4MB)
# 테스트 8 〉	통과 (0.46ms, 10.4MB)
# 테스트 9 〉	통과 (2.51ms, 10.4MB)
# 테스트 10 〉	통과 (1.27ms, 10.3MB)
# 테스트 11 〉	통과 (2.69ms, 10.3MB)
# 테스트 12 〉	통과 (2.41ms, 10.3MB)
# 테스트 13 〉	통과 (0.15ms, 10.3MB)
# 테스트 14 〉	통과 (2.75ms, 10.4MB)
