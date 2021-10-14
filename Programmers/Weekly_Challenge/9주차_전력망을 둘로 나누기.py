from collections import deque

connection = {}


def bfs(n, a, b):
    global connection
    q = deque()
    visited = [False] * (n + 1)
    q.append(a)
    cnt = 0
    while q:
        now = q.popleft()
        visited[now] = True
        cnt += 1
        if now in connection:
            for tower in connection[now]:
                if not visited[tower] and tower != b:
                    q.append(tower)

    return abs(2 * cnt - n)


def solution(n, wires):
    # 각 송전탑에 연결된 다른 송전탑 dict에 저장
    global connection
    for i in range(1, n + 1):
        connection[i] = []
    for a, b in wires:
        connection[a].append(b)
        connection[b].append(a)

    # 전선을 하나씩 끊어보며 두 전력망의 최소 차이 구하기
    min_diff = 100
    for a, b in wires:
        diff = bfs(n, a, b)
        if min_diff > diff:
            min_diff = diff

    return min_diff

# 정확성  테스트
# 테스트 1 〉	통과 (0.11ms, 10.3MB)
# 테스트 2 〉	통과 (1.38ms, 10.2MB)
# 테스트 3 〉	통과 (2.15ms, 10.3MB)
# 테스트 4 〉	통과 (2.10ms, 10.2MB)
# 테스트 5 〉	통과 (2.43ms, 10.3MB)
# 테스트 6 〉	통과 (0.02ms, 10.3MB)
# 테스트 7 〉	통과 (0.01ms, 10.3MB)
# 테스트 8 〉	통과 (0.08ms, 10.3MB)
# 테스트 9 〉	통과 (0.05ms, 10.4MB)
# 테스트 10 〉	통과 (1.28ms, 10.3MB)
# 테스트 11 〉	통과 (1.38ms, 10.3MB)
# 테스트 12 〉	통과 (1.34ms, 10.3MB)
# 테스트 13 〉	통과 (1.20ms, 10.3MB)
