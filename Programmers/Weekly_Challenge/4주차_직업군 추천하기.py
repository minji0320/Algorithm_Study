# https://programmers.co.kr/learn/courses/30/lessons/84325

def solution(table, languages, preference):
    jobs = ["SI", "CONTENTS", "HARDWARE", "PORTAL", "GAME"]
    n = len(languages)
    scores = [0] * 5
    max_score = 0
    answer = ''
    for i in range(5):
        # 직업군 별 점수 총합 구하기
        job_languages = list(table[i].split()[1:])
        for j in range(n):
            if languages[j] not in job_languages:
                continue
            scores[i] += (5 - job_languages.index(languages[j])) * preference[j]

        # 총합이 가장 높은 직업군 구하기
        if max_score < scores[i]:
            answer = jobs[i]
            max_score = scores[i]
        elif max_score == scores[i] and (answer == '' or answer > jobs[i]):
            answer = jobs[i]

    return answer

# 정확성  테스트
# 테스트 1 〉	통과 (0.01ms, 10.3MB)
# 테스트 2 〉	통과 (0.02ms, 10.2MB)
# 테스트 3 〉	통과 (0.02ms, 10.1MB)
# 테스트 4 〉	통과 (0.02ms, 10.1MB)
# 테스트 5 〉	통과 (0.02ms, 10.1MB)
# 테스트 6 〉	통과 (0.02ms, 10.3MB)
# 테스트 7 〉	통과 (0.02ms, 10.3MB)
# 테스트 8 〉	통과 (0.01ms, 10.1MB)
# 테스트 9 〉	통과 (0.01ms, 10.3MB)
# 테스트 10 〉	통과 (0.01ms, 10.2MB)
