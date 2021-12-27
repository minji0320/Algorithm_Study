import sys

# 입력 받기 (board : 0 = 방문 X, -1 = 장애물, 1 : 방문 O)
R, C = map(int, sys.stdin.readline().split())
board = [[0] * C for _ in range(R)]

k = int(sys.stdin.readline())
for _ in range(k):
    r, c = map(int, sys.stdin.readline().split())
    board[r][c] = -1

x, y = map(int, sys.stdin.readline().split())
board[x][y] = 1

dirs = list(map(int, sys.stdin.readline().split()))

# 이동
idx = 0
try_cnt = 0
dirs_len = len(dirs)
dx, dy = [0, -1, 1, 0, 0], [0, 0, 0, -1, 1]
while dirs_len != try_cnt:
    while True:
        nx, ny = x + dx[dirs[idx % dirs_len]], y + dy[dirs[idx % dirs_len]]
        if 0 <= nx < R and 0 <= ny < C and board[nx][ny] == 0:
            x, y = nx, ny
            board[x][y] = 1
            try_cnt = 0
        else:
            try_cnt += 1
            break
    idx += 1

print(x, y)
