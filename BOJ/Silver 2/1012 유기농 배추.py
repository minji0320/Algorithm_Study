import sys

def dfs(i, j):
    farm[i][j] = -1
    for k in range(4):
        ni, nj = i + dirs[k][0], j + dirs[k][1]
        if 0 <= ni < N and 0 <= nj < M and farm[ni][nj] == 1:
            dfs(ni, nj)

sys.setrecursionlimit(10000)
dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
T = int(sys.stdin.readline())
for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    farm = [[0] * M for _ in range(N)]
    for _ in range(K):
        X, Y = map(int, sys.stdin.readline().split())
        farm[Y][X] = 1

    cnt = 0
    for y in range(N):
        for x in range(M):
            if farm[y][x] == 1:
                dfs(y, x)
                cnt += 1

    print(cnt)
