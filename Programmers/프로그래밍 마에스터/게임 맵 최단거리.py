from collections import deque


def solution(maps):
    answer = -1
    q = deque()
    q.append((0, 0, 1))
    maps[0][0] = 0
    dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    n = len(maps)
    m = len(maps[0])
    while q:
        x, y, move = q.popleft()

        if x == n - 1 and y == m - 1:
            answer = move
            break

        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                q.append((nx, ny, move + 1))
                maps[nx][ny] = 0

    return answer
