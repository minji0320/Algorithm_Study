import sys
from collections import deque


def bfs():
    global M, N, board, q, empty, ripe
    dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    day = 0
    while q:
        if ripe == N * M - empty:
            return day

        n = len(q)
        for _ in range(n):
            x, y = q.popleft()
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < M:
                    if board[nx][ny] == "0":
                        board[nx][ny] = "1"
                        q.append((nx, ny))
                        ripe += 1
        day += 1

    return -1


M, N = map(int, sys.stdin.readline().split())
board = []
q = deque()
empty = 0
ripe = 0
for i in range(N):
    board.append(sys.stdin.readline().split())
    for j in range(M):
        if board[i][j] == "1":
            q.append((i, j))
            ripe += 1
        elif board[i][j] == "-1":
            empty += 1

print(bfs())
