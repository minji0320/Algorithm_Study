import sys
from collections import deque


def bfs():
    visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
    q = deque()
    q.append((0, 0, 0))
    visited[0][0][0] = 1
    dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    while q:
        x, y, is_break = q.popleft()

        # 목적지 도착
        if x == N - 1 and y == M - 1:
            return visited[x][y][is_break]

        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny][is_break] == 0:
                if board[nx][ny] == '0':
                    q.append((nx, ny, is_break))
                    visited[nx][ny][is_break] = visited[x][y][is_break] + 1
                elif is_break == 0:
                    q.append((nx, ny, 1))
                    visited[nx][ny][1] = visited[x][y][is_break] + 1

    return -1


N, M = map(int, sys.stdin.readline().split())
board = []
for i in range(N):
    board.append(sys.stdin.readline().strip())

print(bfs())


