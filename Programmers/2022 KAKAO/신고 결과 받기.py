# https://programmers.co.kr/learn/courses/30/lessons/92334

def solution(id_list, report, k):
    n = len(id_list)
    id_index = dict(zip(id_list, range(n)))
    result = dict()
    for r in report:
        a, b = r.split()
        if b not in result:
            result[b] = set()
        result[b].add(id_index[a])

    answer = [0 for _ in range(n)]
    for ids in result.values():
        if len(ids) >= k:
            for i in ids:
                answer[i] += 1
    return answer

# 정확성  테스트
# 테스트 1 〉	통과 (0.01ms, 10.4MB)
# 테스트 2 〉	통과 (0.02ms, 10.4MB)
# 테스트 3 〉	통과 (107.82ms, 34MB)
# 테스트 4 〉	통과 (0.03ms, 10.3MB)
# 테스트 5 〉	통과 (0.04ms, 10.3MB)
# 테스트 6 〉	통과 (0.77ms, 10.4MB)
# 테스트 7 〉	통과 (1.72ms, 10.7MB)
# 테스트 8 〉	통과 (3.26ms, 10.8MB)
# 테스트 9 〉	통과 (48.18ms, 21.8MB)
# 테스트 10 〉	통과 (40.16ms, 21.6MB)
# 테스트 11 〉	통과 (96.20ms, 33.7MB)
# 테스트 12 〉	통과 (0.19ms, 10.3MB)
# 테스트 13 〉	통과 (0.19ms, 10.4MB)
# 테스트 14 〉	통과 (42.10ms, 20.4MB)
# 테스트 15 〉	통과 (87.82ms, 33.9MB)
# 테스트 16 〉	통과 (0.13ms, 10.2MB)
# 테스트 17 〉	통과 (0.18ms, 10.3MB)
# 테스트 18 〉	통과 (0.33ms, 10.3MB)
# 테스트 19 〉	통과 (0.54ms, 10.4MB)
# 테스트 20 〉	통과 (41.94ms, 20.4MB)
# 테스트 21 〉	통과 (90.34ms, 33.9MB)
# 테스트 22 〉	통과 (0.01ms, 10.2MB)
# 테스트 23 〉	통과 (0.01ms, 10.3MB)
# 테스트 24 〉	통과 (0.01ms, 10.2MB)
# 채점 결과
# 정확성: 100.0
# 합계: 100.0 / 100.
