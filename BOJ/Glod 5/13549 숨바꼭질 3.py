from collections import deque


def solution():
    N, K = map(int, input().split())
    visited = [False] * 200001
    q = deque()
    q.append((N, 0))
    visited[N] = True
    while q:
        now_num, sec = q.popleft()
        visited[now_num] = True
        if now_num == K:
            return sec

        if (now_num * 2) <= 200000 and not visited[(now_num * 2)]:
            q.appendleft((now_num * 2, sec))

        if now_num - 1 >= 0 and not visited[now_num - 1]:
            q.append((now_num - 1, sec + 1))

        if now_num + 1 <= 100000 and not visited[now_num + 1]:
            q.append((now_num + 1, sec + 1))


print(solution())