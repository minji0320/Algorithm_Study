import sys
from collections import deque

N, M, K, X = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    start, end = map(int, sys.stdin.readline().split())
    graph[start].append(end)

visited = [False] * (N+1)
q = deque([X])
visited[X] = True
for _ in range(K):
    now_len = len(q)
    for _ in range(now_len):
        now = q.popleft()
        for dest in graph[now]:
            if not visited[dest]:
                visited[dest] = True
                q.append(dest)

if len(q) == 0:
    print(-1)
else:
    answer = sorted(list(q))
    for a in answer:
        print(a)
        