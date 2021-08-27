# https://programmers.co.kr/learn/courses/30/lessons/42861?language=python3

def solution(n, costs):
    # 건설 가능한 모든 다리들
    bridges = list(list() for _ in range(n))
    for i in costs:
        bridges[i[0]].append((i[1], i[2]))
        bridges[i[1]].append((i[0], i[2]))

    # 아직 연결되지 않은 섬과 연결하는 다리 중 건설 비용이 가장 적게 드는 다리 선택
    visited = [0]
    candidates = bridges[0]
    answer = 0
    cnt = 1
    while cnt < n:
        min = 10000000000
        min_idx = -1

        for i, candidate in enumerate(candidates):
            if min > candidate[1] and candidate[0] not in visited:
                min = candidate[1]
                min_idx = candidate[0]

        answer += min
        visited.append(min_idx)
        candidates += bridges[min_idx]
        cnt += 1

    return answer

### 정확성  테스트
# 테스트 1 〉	통과 (0.01ms, 10.3MB)
# 테스트 2 〉	통과 (0.01ms, 10.2MB)
# 테스트 3 〉	통과 (0.03ms, 10.2MB)
# 테스트 4 〉	통과 (0.07ms, 10.1MB)
# 테스트 5 〉	통과 (0.03ms, 10.1MB)
# 테스트 6 〉	통과 (0.08ms, 10.2MB)
# 테스트 7 〉	통과 (0.12ms, 10.2MB)
# 테스트 8 〉	통과 (0.05ms, 10.2MB)
