import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

board = [[float("inf")] * N for _ in range(N)]
for i in range(N):
    board[i][i] = 0

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    board[a - 1][b - 1] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            board[i][j] = min(board[i][j], board[i][k] + board[k][j])

for i in range(N):
    cnt = 0
    for j in range(N):
        if board[i][j] == float("inf") and board[j][i] == float("inf"):
            cnt += 1
    print(cnt)
